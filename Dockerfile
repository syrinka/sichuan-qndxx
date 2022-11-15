FROM python:3.9-slim

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install cron

WORKDIR /app

COPY requirements.txt .
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT /app/docker-entrypoint.sh
