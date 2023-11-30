# Using Alpine Latest image
FROM alpine:latest
RUN apk upgrade
RUN apk add --upgrade apk-tools
RUN apk upgrade --available

#Updating Python with no cache to make image lite
RUN apk add --no-cache python3-dev
RUN apk add py3-pip

#Updating all core packages
RUN apk update
RUN pip3 install --upgrade pip

#Copying local scripts into container image Working Directory
WORKDIR /app
COPY requirements.txt /app
COPY app.py /app

#Installed package requirements
RUN pip3 --no-cache-dir install -r /app/requirements.txt
RUN apk update

#Exposing flask app port -- 5000
EXPOSE 5000

#Running Flask App during container execution
#ENTRYPOINT ["python3"]
CMD ["flask", "run","--host","0.0.0.0","--port","5000"]