FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
        && pip install --upgrade pip \
        && pip install -r requirements.txt