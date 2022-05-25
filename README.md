# This repo is to illustrate continuous model deployment using AWS
Inspired from: https://github.com/srivatsan88/ContinousModelDeploy which does it in GCP

AWS services used:
- AWS ECR
- AWS ECS (Fargate & EC2)
- AWS CodeBuild

The monolithic application has also be decoupled into two microservices
- Front end Streamlit app &
- Back end API using Fast API

The respective Docker File and requirements.txt is in the respective folders
