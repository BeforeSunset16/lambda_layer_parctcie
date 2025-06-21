docker build -t lambda-layer-builder .
docker run --name build-layer lambda-layer-builder
docker cp build-layer:/opt/lambda_layer.zip .
docker rm build-layer
