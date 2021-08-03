FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/ports.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \ 
    apt-get update

RUN apt-get install -y python3.7 && \
    apt-get install -y python3-pip && \
    apt-get install -y git

RUN mkdir /src

RUN git clone https://oauth2:cae0e4e2613465f9734ccba00eacaad5@gitee.com/sun17ya/nlp-model.git /src && \
    git checkout -b feature/sun-20210721 origin/feature/sun-20210721

ADD requirements.txt /src/requirements.txt

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy && pip install -r /src/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
