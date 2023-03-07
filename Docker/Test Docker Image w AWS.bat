set /p image_name="Image Name: "
set /p tag_name="Tag Name: "
for /f %%i in ('aws --profile default configure get aws_access_key_id') do set AWS_ACCESS_KEY_ID=%%i
for /f %%i in ('aws --profile default configure get aws_secret_access_key') do set AWS_SECRET_ACCESS_KEY=%%i
docker build -t %image_name%:%tag_name% -f ./Dockerfile .
docker run -d -p 8501:8501 -e AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID%  -e AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% --name %image_name% %image_name%:%tag_name%
start "" http:127.0.0.1:8501
ECHO press enter to close development docker image
pause
docker stop %image_name%
docker rm %image_name%
docker image rm %image_name%:%tag_name%