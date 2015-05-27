FROM ubuntu
MAINTAINER Hamza Waqas
WORKDIR /code
RUN apt-get update
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
RUN apt-get update
RUN apt-get install -y mongodb-org
RUN service mongod start
RUN apt-get install nginx -y
RUN apt-get install python-pip python-dev build-essential -y
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN virtualenv env
CMD ["source", "./env/bin/activate"]
ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
RUN django-admin.py startproject mbo_api
RUN service nginx start
EXPOSE 80