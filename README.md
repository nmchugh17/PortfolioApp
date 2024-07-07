# What is this project
This is a web app to showcase Python projects
# Instructions for Elastic Container Service and Code Pipeline

## 1. Install Docker on Your Local Machine
For Windows:
Download Docker Desktop from Docker's website.
Run the installer and follow the installation instructions.
After installation, Docker Desktop should start automatically. You can verify Docker is running by opening a command prompt and typing docker --version.
## 2. Create a Dockerfile
Create a Dockerfile in the same directory as your Home.py file. This Dockerfile will define the environment for your Streamlit app.

Dockerfile
Copy code
###Use the official Python image from the Docker Hub
FROM python:3.11-slim

### Set the working directory in the container
WORKDIR /app

### Copy the requirements file
COPY requirements.txt requirements.txt

### Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

### Copy the current directory contents into the container at /app
COPY . .

### Expose port 8501 for streamlit
EXPOSE 8501

### Command to run the streamlit app
CMD ["streamlit", "run", "Home.py"]
## 3. Create a requirements.txt File
Create a requirements.txt file in the same directory and add your dependencies:

Copy code
streamlit
pandas
## 4. Build and Test Your Docker Image Locally
sh
Copy code
### Navigate to your project directory
cd C:\Users\Niall McHugh\PythonApps\PortfolioApp

### Build the Docker image
docker build -t portfolio-app .

### Run the Docker container
docker run -p 8501:8501 portfolio-app
## 5. Push Your Docker Image to Amazon ECR
Create an ECR Repository:

Go to the Amazon ECR console.
Create a new repository for your Docker image.
Authenticate Docker to Your ECR Repository:
Follow the steps provided in the AWS ECR console to authenticate Docker.

Tag and Push Your Docker Image:

sh
Copy code
### Tag your Docker image
docker tag portfolio-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/portfolio-app:latest

### Push the image to ECR
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/portfolio-app:latest
## 6. Create a Task Definition in ECS
Go to the Amazon ECS console.
Create a new task definition.
Add a container to the task definition with the image URL from ECR and set the necessary environment variables and port mappings.
## 7. Create an ECS Cluster and Service
Create a Cluster:

In the ECS console, create a new cluster (e.g., EC2 or Fargate).
Create a Service:

Create a new service in the cluster, using the task definition you created.
## 8. Set Up CodePipeline for CI/CD
Create a Pipeline:

Go to the AWS CodePipeline console.
Create a new pipeline.
Add Source Stage:

Select GitHub as the source provider.
Connect your GitHub repository.
Add Build Stage:

Use AWS CodeBuild to build your Docker image and push it to ECR.
Create a buildspec.yml file in your repository:
yaml
Copy code
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
  build:
    commands:
      - echo Building the Docker image...
      - docker build -t portfolio-app .
      - docker tag portfolio-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/portfolio-app:latest
  post_build:
    commands:
      - echo Pushing the Docker image...
      - docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/portfolio-app:latest
      - echo Writing image definitions file...
      - printf '[{"name":"<container_name>","imageUri":"%s"}]' <aws_account_id>.dkr.ecr.<region>.amazonaws.com/portfolio-app:latest > imagedefinitions.json
artifacts:
  files: imagedefinitions.json
Add Deploy Stage:

Use Amazon ECS as the deploy provider.
Select your cluster and service.
## 9. Finalize and Test the Pipeline
Save and execute your pipeline.
Make a change to your Streamlit app, commit, and push it to GitHub.
Verify that CodePipeline picks up the change, builds a new Docker image, pushes it to ECR, and updates your ECS service.
This setup will ensure your Streamlit app is deployed on AWS ECS and automatically updated whenever you push changes to your GitHub repository.