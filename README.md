# Lambda Layer Practice

This project is used to build an AWS Lambda Layer containing Snowflake connector and timezone processing libraries.

## Project Features

Builds an AWS Lambda Layer with the following dependencies:
- `snowflake-connector-python == 3.15.0` - Snowflake database connector
- `pytz == 2025.2` - Timezone processing library

## File Description

- `requirements.txt` - Python dependency packages list
- `dockerfile` - Docker build configuration
- `build.bat` - Windows build script

## Usage

### Windows Users

#### Method 1: Double-click to run (Recommended)
1. Ensure Docker Desktop is installed
2. Start Docker Desktop
3. Double-click the `build.bat` file directly
4. Wait for the build to complete, then press any key to close the window

#### Method 2: Command line execution
```cmd
build.bat
```

## Build Process

The script automatically executes the following steps:
1. Build Docker image `snowflake-pytz-layer-builder`
2. Run container to generate Lambda Layer zip file
3. Copy `snowflake-pytz-docker-layer.zip` from container to current directory
4. Clean up temporary container

## Output Files

After successful build, the following file will be generated in the current directory:
- `snowflake-pytz-docker-layer.zip` - Compressed package that can be directly uploaded to AWS Lambda Layer

## Use Cases

This Lambda Layer is suitable for:
- Connecting to Snowflake data warehouse in AWS Lambda functions
- Processing timezone-related data operations
- Avoiding repeated installation of dependency packages in Lambda functions

## System Requirements

- Docker Desktop (Windows)
- At least 2GB available memory
- Stable network connection (for downloading dependency packages)