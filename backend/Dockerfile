FROM python:3.11-slim
WORKDIR /app
COPY ../requirements.txt /app/requirements.txt
RUN pip install -U pip && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./app /app/app
EXPOSE 8000
CMD ["python", "run.py"]