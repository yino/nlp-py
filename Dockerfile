FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

ENV ENV prod
ENV CONFIG_PATH /nlp-model

RUN sed -i 's/ports.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \ 
    apt-get update

RUN apt-get install -y python3.7 && \
    apt-get install -y python3-pip && \
    apt-get install -y git && \ 
    pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy && \
    pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple && \
    git clone https://oauth2:cae0e4e2613465f9734ccba00eacaad5@gitee.com/sun17ya/nlp-model.git && \
    cd $CONFIG_PATH && \
    git checkout -b feature/sun-20210721 origin/feature/sun-20210721 && \
    pip install -r $CONFIG_PATH/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && \
    touch $CONFIG_PATH/log/gunicorn_error.log && \
    touch $CONFIG_PATH/log/gunicorn_access.log && \
    chmod -R 777 $CONFIG_PATH/log && \
    cp template.ini prod.ini

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime