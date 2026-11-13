FROM python:3.11-slim
WORKDIR /app
#容器内部运行的文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
#no-cache-dir 下载后清理一下安装包
COPY . .
ENTRYPOINT ["python", "main.py"]
