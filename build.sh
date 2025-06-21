docker build -t snowflake-pytz-layer-builder .
docker run --name snowflake-pytz-builder snowflake-pytz-layer-builder
docker cp snowflake-pytz-builder:/opt/snowflake-pytz-docker-layer.zip ./snowflake-pytz-docker-layer.zip
docker rm snowflake-pytz-builder
