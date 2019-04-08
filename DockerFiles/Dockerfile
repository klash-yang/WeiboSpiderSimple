#基于的基础镜像
FROM python:3

#维护者
MAINTAINER Dadiao

#代码添加到code文件夹
ADD ./inscrawler /inscrawler

# 设置code文件夹是工作目录
WORKDIR /inscrawler

# 安装支持
RUN apt-get update
RUN apt-get install python3-pip
RUN pip3 install -r requirements.txt
RUN pip3 install pymongo

CMD ["python3", "/inscrawler/run_once.py"]