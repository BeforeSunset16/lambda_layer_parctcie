FROM amazonlinux:2

# 安装 Python 和依赖
RUN yum update -y && \
    yum install -y python3 python3-devel gcc zip && \
    python3 -m pip install --upgrade pip

# 创建构建目录
WORKDIR /opt
COPY requirements.txt .

# 安装依赖到 python/ 文件夹
RUN pip3 install --only-binary=:all: -r requirements.txt -t python/

# 打包成 zip
CMD zip -r /opt/snowflake-pytz-docker-layer.zip python/