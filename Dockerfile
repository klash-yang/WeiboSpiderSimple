#基于的基础镜像
FROM python:3.7

#维护者
MAINTAINER Dadiao

RUN chmod -R 777 ./inscrawler

#代码添加到code文件夹
ADD ./inscrawler /inscrawler

# 设置code文件夹是工作目录
WORKDIR /inscrawler

# 安装支持
RUN pip install -r requirements.txt

CMD ["python", "/inscrawler/run_once.py"]