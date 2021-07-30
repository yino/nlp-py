FROM python:3.7

LABEL maintainer="SunXiaoHu <m15829090357@163.com>"

CMD [ "python3 -m pip install --upgrade pip","pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy","pip install -i https://mirrors.aliyun.com/pypi/simple/ uwsgi"," pip install -i https://mirrors.aliyun.com/pypi/simple/ pandas","pip install -i https://mirrors.aliyun.com/pypi/simple/ gensim"," pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/" ]
WORKDIR /code
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime