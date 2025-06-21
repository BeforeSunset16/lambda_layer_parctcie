FROM public.ecr.aws/lambda/python:3.11

RUN yum -y install gcc python3-devel

# 创建构建目录
WORKDIR /opt
COPY requirements.txt .

# 安装依赖到 python/ 文件夹
RUN pip3 install -r requirements.txt -t python/

# 打包成 zip
ENTRYPOINT  zip -r /opt/snowflake-pytz-docker-layer.zip python/