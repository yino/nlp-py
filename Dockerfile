FROM python:3.7-alpine

LABEL maintainer="SunXiaoHu <m15829090357@163.com>"

WORKDIR /code
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime