FROM python:3.7

LABEL maintainer="Yino <m15829090357@163.com>"

WORKDIR /code

COPY requirements.txt /requirements.txt

RUN python3 -m pip install --upgrade pip && pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy && pip install -i https://mirrors.aliyun.com/pypi/simple/ gunicorn && pip install -i https://mirrors.aliyun.com/pypi/simple/ pandas && pip install -i https://mirrors.aliyun.com/pypi/simple/ gensim\
&& pip install -r /requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
