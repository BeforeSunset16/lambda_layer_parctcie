@echo off
echo Building Docker image...
docker build -t snowflake-pytz-layer-builder .

echo Running container to generate layer...
docker run --name snowflake-pytz-builder snowflake-pytz-layer-builder

echo Copying generated layer file...
docker cp snowflake-pytz-builder:/opt/snowflake-pytz-docker-layer.zip ./snowflake-pytz-docker-layer.zip

echo Cleaning up container...
docker rm snowflake-pytz-builder

echo Build completed! Check snowflake-pytz-docker-layer.zip
pause 