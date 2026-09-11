"""
RAG 知识库问答系统

工作方式（2026-09 已实测可用）：
1. Embedding 用本地的 sentence-transformers 模型，不花钱、不依赖云端；
   第一次运行会自动下载模型（约 470MB），之后走本地缓存。
2. 回答用 DeepSeek 的对话模型（HTTP 直连，不依赖 openai SDK 版本）。

运行前：
- 把知识放进 knowledge_base/ 目录的 .txt 文件（UTF-8 编码）。
- 可自定义 API：设置环境变量 RAG_API_KEY、RAG_API_BASE、RAG_CHAT_MODEL，
  默认使用脚本下方填写的 DeepSeek key。
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

import numpy as np
import requests


# huggingface.co 在国内常连不上，默认走 hf-mirror.com 下载模型。
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

# 换成你自己的 DeepSeek key；想用其它 OpenAI 兼容服务时，
# 改 RAG_API_BASE 和 RAG_CHAT_MODEL 即可。
API_KEY = os.environ.get("RAG_API_KEY")
API_BASE = os.environ.get("RAG_API_BASE", "https://api.deepseek.com/v1")
CHAT_MODEL = os.environ.get("RAG_CHAT_MODEL", "deepseek-v4-flash")

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge_base"

_model = None

def chunk_text(text,chunk_size=500,overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap
    return chunks



def read_question():
    """读取一行用户问题，兼容控制台和 UTF-8/GBK 管道输入。"""
    try:
        return input("\n请输入你的问题：").strip()
    except UnicodeDecodeError:
        raw = sys.stdin.buffer.readline()
        for enc in ("utf-8", "gbk"):
            try:
                return raw.decode(enc).strip()
            except UnicodeDecodeError:
                continue
        return ""


def get_embedding_model():
    """延迟加载本地 embedding 模型，避免脚本一启动就卡在下载上。"""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer

        print("正在加载本地 embedding 模型（第一次会自动下载）...")
        _model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return _model


# ====== 1. 读取文档并预计算 embedding ======
def load_documents(folder_path):
    all_chunks = []
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"警告：知识库目录不存在：{folder}")
        return all_chunks

    for file_path in sorted(folder.glob("*.txt")):
        try:
            content = file_path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError:
            print(f"跳过 {file_path.name}：不是 UTF-8 编码")
            continue
        if not content:
            print(f"跳过 {file_path.name}：文件为空")
            continue

        # ✅ 分块（在循环内部）
        raw_chunks = chunk_text(content, chunk_size=500, overlap=50)
        for i, chunk in enumerate(raw_chunks):
            all_chunks.append({
                "content": chunk,
                "source": f"{file_path.name} (块 {i+1})",
                "embedding": get_embedding(chunk),
            })

    return all_chunks


# ====== 2. 生成 embedding（本地模型，不联网） ======
def get_embedding(text):
    """把文本转成 384 维向量。"""
    model = get_embedding_model()
    return model.encode(text)


# ====== 3. 检索最相似的 chunk（余弦相似度） ======
def find_top_k(query_embedding, chunks, k=3):
    """返回最相似的k个chunk"""
    scored = []
    for chunk in chunks:
        chunk_embedding = chunk["embedding"]
        norm = np.linalg.norm(query_embedding) * np.linalg.norm(chunk_embedding)
        score = float(np.dot(query_embedding, chunk_embedding) / norm)
        scored.append((score,chunk))

    #按分数从高到低排序， 取前 k 个
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:k]


# ====== 4. 生成回答（OpenAI 兼容接口，默认 DeepSeek） ======
def ask_question(question, context):
    prompt = f"""
你是一个知识问答助手。请严格根据以下参考信息回答用户的问题。

【参考信息】
{context}

【用户问题】
{question}

【回答要求】
1. 只根据参考信息回答，不要编造内容
2. 如果参考信息中没有答案，请直接说"参考信息中没有相关内容"
3. 回答要简洁、准确，直接回答问题
4. 如果参考信息中有多个相关点，可以分点列出

请回答：
"""
    response = requests.post(
        f"{API_BASE}/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": CHAT_MODEL,
            "messages": [
                {"role": "system", "content": "你是一个严格基于参考信息回答问题的助手。"},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 1000,
        },
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"API 请求失败（{response.status_code}）：{response.text[:500]}"
        )
    data = response.json()
    return data["choices"][0]["message"]["content"]


# ====== 5. 主程序 ======
def main():
    print("RAG 知识库问答系统（本地 embedding + DeepSeek）")
    print("=" * 40)

    chunks = load_documents(KNOWLEDGE_DIR)
    if not chunks:
        print(f"知识库没有可用内容，请先往 {KNOWLEDGE_DIR} 里放非空的 .txt 文件。")
        return

    print(f"已加载 {len(chunks)} 个文档")
    question = read_question()
    if not question:
        print("问题不能为空。")
        return

    print("正在检索...")
    query_embedding = get_embedding(question)
    top_chunks = find_top_k(query_embedding, chunks, k=3)

    #打印检索到的3个来源
    print("找到以下相关文档：")
    for score, chunk in top_chunks:
        print(f"  - {chunk['source']}(相似度：{score:.4f})")

    #把3个块的内容拼接起来，一起发给大模型
    context = "\n\n---\n\n".join([chunk["content"] for score, chunk in top_chunks])

    print("正在生成回答...")
    answer = ask_question(question, context)

    print("\n" + "=" * 40)
    print("回答：")
    print(answer)


if __name__ == "__main__":
    main()
