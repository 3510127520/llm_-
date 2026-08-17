# 365 天 LLM Engineer 执行手册

目标：一年后能通过大部分 AI 应用工程实习面试，具备初级 LLM Engineer 能力。
定位：做 LLM 应用，不做研究。学 30%，做 70%。

---

## 一、铁律（比计划本身重要）

1. 计划外的新内容不学。先完成手头任务，再谈兴趣。
2. 每天先写代码，再补理论。代码行数是硬指标。
3. 视频只看目标章节；书按需查，不从头啃到尾。
4. 每周至少 3 次 `git add / commit / push`，GitHub 活跃度是硬指标。
5. 卡住超过 30 分钟就换任务或求助，不空耗。
6. 每个阶段达到"完成标准"才进入下一阶段，时间到了没达到就加班补齐。

---

## 二、每日模板

普通日 3 小时：

| 时段 | 内容 | 要求 |
| --- | --- | --- |
| 30 分钟 | 理论学习 | 只学当日任务对应内容，记笔记 |
| 90 分钟 | 写代码 | 完成今日最小任务，禁止只看视频 |
| 30 分钟 | 读优秀项目 | 看 1 个 GitHub 项目或官方文档 |
| 30 分钟 | 总结/提交 | 更新笔记，commit + push |

周末 6 小时：

| 时段 | 内容 | 要求 |
| --- | --- | --- |
| 2 小时 | 学习 | 补本周卡住的知识点 |
| 3 小时 | 项目开发 | 推进一个完整功能 |
| 1 小时 | 技术总结 | 写周记、更新 README、下周计划 |

每日结束 30 秒打卡：

- 今天写了多少行代码？
- 今天 push 了吗？
- 今天卡在哪个点？
- 明天第一件事是什么？

---

## 三、每周检查表（每周日晚上 30 分钟）

- [ ] 写代码 >= 5 天
- [ ] GitHub 提交 >= 3 次
- [ ] 读/看 1 篇技术文章或论文
- [ ] 项目推进 1 个功能
- [ ] 更新学习笔记
- [ ] 记录本周卡点和下周计划

---

## 四、阶段总览与完成标准

### 阶段 0（Day 1-14）：恢复写代码能力

目标：从"会考试的学生"变成"能写代码的人"。

完成标准：

- [ ] 独立写出 100 行以上、有完整功能的 Python 工具
- [ ] 熟练使用 `git add / commit / push`，有 GitHub 仓库
- [ ] 会用 `ls / cd / grep / vim / ssh` 等命令
- [ ] 项目有 README、使用说明、requirements.txt
- [ ] 工具能扫描自己电脑的真实文件夹并给出报告

### 阶段 1（Day 15-90）：LLM 基础 + RAG

目标：做出第一个简历级项目"企业知识库 RAG"。

完成标准：

- [ ] 能解释 Token、Embedding、Transformer、Attention
- [ ] 调用过 OpenAI / Qwen / HuggingFace 至少一种 API
- [ ] RAG 全流程亲手搭过：解析、Chunk、Embedding、检索、生成
- [ ] 项目支持 PDF / Word / Markdown 上传和问答
- [ ] 做过 Query Rewrite、Hybrid Search、Rerank 中的至少两项
- [ ] 有评测结果：能回答 20 个测试问题，记录命中率

### 阶段 2（Day 91-180）：Agent + 微调

目标：从 RAG 工程师升级为 LLM Engineer。

完成标准：

- [ ] 理解 Tool Calling、ReAct、Planning，能讲清楚
- [ ] 用 LangGraph 搭出 AI 工作助手：读 Excel -> 分析 -> 生成报告
- [ ] 用 LoRA / PEFT 微调过一个小模型（不用训练大模型）
- [ ] 完成"AI 企业助手 2.0"：RAG + Agent + 微调 + 权限
- [ ] 前端 + FastAPI + Agent + RAG + LLM 的完整架构

### 阶段 3（Day 181-270）：工程化 + Infra

目标：拉开和普通 Agent 学生的差距。

完成标准：

- [ ] 理解 CPU / GPU / 内存 / 网络，能解释模型部署时的瓶颈
- [ ] 用 Docker 独立部署过后端、数据库、模型服务
- [ ] 用 vLLM 本地部署开源模型（如 Qwen）并暴露 API
- [ ] 理解 Batch、KV Cache、GPU Memory 并写进项目 README
- [ ] 有压测或性能数据，不是只贴"能跑起来"

### 阶段 4（Day 271-365）：求职冲刺

目标：拿到 AI 应用工程实习 Offer。

完成标准：

- [ ] 3 个 GitHub 项目都有完整 README：架构图、技术选型、性能指标
- [ ] 能现场写出装饰器、多线程、异步的小例子
- [ ] 能讲 10 分钟 RAG 原理 + 自己踩过的坑
- [ ] 每周至少 2 次模拟面试（可让 AI 或同学当面试官）
- [ ] 每天投递 5-10 份，投递记录表完整

---

## 五、阶段 0 逐日任务（Day 1-14）

### 第 1 周：做出第一个项目并上传 GitHub

Day 1：装好 Python 和 VS Code；复习变量、函数；写 50 行小脚本（如猜数字）；初始化 git 仓库，第一次 commit。

Day 2：复习类、文件读写；继续写 50 行；把今天的改动 commit。

Day 3：文件管理工具第一版：输入文件夹 -> 扫描文件 -> 统计类型 -> 生成报告（先输出文本即可）。

Day 4：Git 完整流程：本地仓库、GitHub 建仓库、`git remote add`、第一次 push。完成"上传 GitHub"这个硬任务。

Day 5：Linux 基础命令（`ls / cd / grep / vim / ssh`）。Windows 用 WSL 或 Git Bash 练，不用装双系统。

Day 6：重构工具：拆分函数、加异常处理、让程序扫描失败时不崩溃。

Day 7：给工具加搜索功能（按文件名或关键词过滤）；写 README；push v1.0。

第 1 周完成标准：别人能按 README 在你的 GitHub 仓库运行你的工具。

### 第 2 周：工程化升级

Day 8：venv 创建虚拟环境，`pip install` 一个包试试，写 requirements.txt。

Day 9：学 logging，把工具里的 `print` 换成日志，区分 info / warning / error。

Day 10：把报告升级为 Markdown 文件；扫自己电脑的真实文件夹，修复真实问题。

Day 11：给工具加 2-3 个过滤参数（扩展名、大小、时间）。

Day 12：学 Docker 基础概念（镜像、容器、Dockerfile），把项目打包运行。

Day 13：补齐 README：功能列表、使用示例、截图或示例输出。

Day 14：项目复盘，整理笔记，push 最终版，写下周计划。

---

## 六、三个简历项目规格

### 项目 1：企业知识库 RAG（阶段 1）

- 功能：上传 PDF / Word / Markdown，用户提问，AI 基于文档回答
- 技术：Python、LangChain 或 LlamaIndex（只选一个）、FAISS 或 Milvus、BGE、BGE-Reranker、FastAPI
- 验收：10 份文档、20 个测试问题，记录检索命中率和回答正确率
- 简历一句话：基于 RAG 架构搭建企业知识助手，通过 Embedding + Vector Database + Rerank 优化检索流程

### 项目 2：AI Agent 工作流系统（阶段 2）

- 功能：用户说"分析销售数据"，Agent 自动读 Excel -> 分析 -> 生成报告
- 技术：LangGraph、Tool Calling、FastAPI、React（可选）
- 加分：LoRA 微调一个小模型接入系统；加入用户权限
- 简历一句话：用 Tool Calling + Workflow 搭建企业 AI 助手，串联 RAG、数据分析与微调模型

### 项目 3：LLM 部署平台（阶段 3）

- 功能：vLLM 本地部署 Qwen，提供 OpenAI 风格 API，Docker 一键启动
- 技术：vLLM、Docker / Docker Compose、GPU 优化
- 验收：README 里有启动步骤、性能数据（吞吐、显存、Batch 的影响）
- 简历一句话：基于 vLLM 实现开源模型本地部署，完成 Batch、KV Cache、GPU Memory 优化

---

## 七、阶段 4 执行表

Day 271-300：项目收尾。每个 README 补架构图（Mermaid 或 draw.io）、技术选型、性能指标；GitHub Profile 整理成"3 个项目 + 1 段简介"。

Day 301-330：面试准备。八股范围：Python 装饰器/多线程/异步；Transformer / RAG / Agent 原理；Docker / Linux / Redis / MySQL。每周 2 次模拟面试，记录没答上的题。

Day 331-365：投递。每天 5-10 份；岗位关键词：LLM Engineer Intern、大模型开发实习生、AI 应用开发实习、Agent 工程师。投递记录表：公司 / 岗位 / 日期 / 渠道 / 结果 / 下一步。

---

## 八、资源清单（只读必要的部分）

- Python：《Python编程：从入门到实践》前半部分，遇到再查
- 深度学习：《动手学深度学习》只看 Attention / Transformer 相关章节；李宏毅课程按需看
- LLM：《Hands-On Large Language Models》
- 系统：《CSAPP》只读内存、并发、网络三部分
- 论文最低 5 篇：Attention Is All You Need、BERT、GPT-3、LoRA、RAG
- 优先官方文档：OpenAI、Qwen、HuggingFace、LangGraph、vLLM

原则：书是字典，不是连续剧。项目需要什么查什么。

---

## 九、反拖延规则

1. 想换学习资料时，先写 10 行代码再决定。
2. 不收藏新教程。收藏 = 今天不学。
3. 视频不开 1.5 倍速就说明内容不值得看。
4. "我懂了"不算数，"能跑通 + 能讲出来"才算数。
5. 每周检查表没打满勾，下周不准开新项目。

---

## 十、每周复盘模板

本周数据：代码行数 ___ / commit 次数 ___ / 项目功能 ___

1. 本周完成了什么？
2. 卡在哪里？
3. 哪件事浪费了最多时间？
4. 下周只做哪三件事？
5. 下周最小目标是什么？
