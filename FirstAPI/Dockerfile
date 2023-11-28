# Using Alpine Latest image
FROM alpine:latest

#Updating Python with no cache to make image lite
RUN apk add --no-cache python3-dev
RUN apk add py3-pip

#Updating all core packages
RUN apk update
RUN pip3 install --upgrade pip

#Copying local scripts into container image
ADD ./* ./

#Installed package requirements
RUN pip3 install -r ./requirements.txt
RUN apk update