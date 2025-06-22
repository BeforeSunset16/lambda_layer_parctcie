<<<<<<< HEAD
# lambda_layer_parctcie
The maximum size of a lambda layer is 70 MB.
=======
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
- `.github/workflows/build-and-upload-layer.yml` - GitHub Actions workflow for automated build and deployment

## Usage

### Automated Build with GitHub Actions (Recommended)

The project includes a GitHub Actions workflow that automatically builds and deploys the Lambda Layer to AWS when you push to the production branch.

#### Setup Required:
1. Add the following secrets to your GitHub repository:
   - `AWS_ACCESS_KEY_ID` - Your AWS access key
   - `AWS_SECRET_ACCESS_KEY` - Your AWS secret key
   - `AWS_REGION` - Your AWS region (e.g., us-east-1)

#### How it works:
- **On push to production branch**: Automatically builds the layer and deploys to AWS Lambda
- **Manual trigger**: Use "workflow_dispatch" to manually trigger the build and deployment

#### Deployment Process:
1. Push your changes to the `production` branch
2. GitHub Actions automatically triggers the workflow
3. Builds the Docker image and generates the Lambda Layer
4. Deploys the layer to AWS Lambda
5. You can download the layer file as an artifact from the Actions page

### Local Build (Windows)

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

### For Local Build:
- Docker Desktop (Windows)
- At least 2GB available memory
- Stable network connection (for downloading dependency packages)

### For GitHub Actions:
- No local setup required
- GitHub Actions runs on Ubuntu with Docker pre-installed
- AWS credentials configured as repository secrets
>>>>>>> c133789acc0140d86e2ede8832f2d42436dceb1f
