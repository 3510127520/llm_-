# 使用官方 python 镜像作为基础
FROM docker.m.daocloud.io/library/python:3.13-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器里
COPY 4tian.py /app/
COPY requirements.txt /app/

#安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 告诉 Docker 容器启动时运行这个命令
CMD ["python","4tian.py"]