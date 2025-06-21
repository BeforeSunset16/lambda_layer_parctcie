FROM public.ecr.aws/lambda/python:3.11

RUN yum -y install gcc python3-devel

WORKDIR /opt
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install --only-binary=:all: -r requirements.txt -t python/

CMD zip -r /opt/snowflake-pytz-docker-layer.zip python/