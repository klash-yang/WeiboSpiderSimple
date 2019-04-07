#基于的基础镜像
FROM ubuntu:16.04

#维护者
MAINTAINER Dadiao

# 安装Python
RUN apt-get update && \
      apt-get install -y python3 \
      rm -rf /var/lib/apt/lists/*

#代码添加到code文件夹
ADD ./inscrawler /inscrawler

# 设置code文件夹是工作目录
WORKDIR /inscrawler

# 安装支持
RUN pip3 install -r requirements.txt

CMD ["python3", "/inscrawler/run_once.py"]