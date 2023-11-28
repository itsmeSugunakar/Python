# Using Alpine Latest image
FROM alpine:latest

#Updating Python with no cache to make image lite
RUN apk add --no-cache python3-dev
RUN apk add py3-pip

#Updating all core packages
RUN apk update
RUN pip3 install --upgrade pip

#Copying local scripts into container image Working Directory
WORKDIR /app
COPY ./* /app/

#Installed package requirements
RUN pip3 --no-cache-dir install -r /app/requirements.txt
RUN apk update

#Exposing flask app port -- 5000
EXPOSE 5000

#Running Flask App during container execution
ENTRYPOINT [ "python3" ]
CMD [ "/app/app.py" ]