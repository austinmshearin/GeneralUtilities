set /p image_name="Image Name: "
set /p tag_name="Tag Name: "
docker build -t %image_name%:%tag_name% -f ./Dockerfile .
docker run -d -p 8501:8501 --name %image_name% %image_name%:%tag_name%
start "" http:127.0.0.1:8501
ECHO press enter to close development docker image
pause
docker stop %image_name%
docker rm %image_name%
docker image rm %image_name%:%tag_name%