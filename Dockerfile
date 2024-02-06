FROM python:3.10-slim

WORKDIR /app

ADD requirements.txt /app
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY src /app
CMD ["/bin/bash","-c","uvicorn app:app  --host 0.0.0.0 --port 8080 --workers 2"]