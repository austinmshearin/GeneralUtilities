set /p name="Docker Image Name: "
set /p tag="Docker Image Tag: "
set /p region="ECR Region: "
set /p ecr_name="ECR Name: "
aws ecr get-login-password --region %region% | docker login --username AWS --password-stdin %ecr_name%
docker build -t %name%:%tag% -f ./Dockerfile .
docker tag %name%:%tag% %ecr_name%/%name%:%tag%
docker push %ecr_name%/%name%:%tag%
docker image rm %name%:%tag%
docker image rm %ecr_name%/%name%:%tag%
pause