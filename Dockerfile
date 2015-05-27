FROM ubuntu
MAINTAINER Hamza Waqas
WORKDIR /code
RUN apt-get update
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
RUN apt-get update
RUN apt-get install -y mongodb-org git
RUN start mongod
RUN apt-get install nginx -y
RUN apt-get install python-pip python-dev build-essential -y
RUN pip install --upgrade pip
RUN git clone https://github.com/hamzawaqas-10p/drf-plate.git mbo
RUN pip install --upgrade virtualenv
WORKDIR /code/mbo
RUN virtualenv env
CMD ["source", "./env/bin/activate"]
RUN pip install -r requirements.txt
ADD ./data data
ADD conf/ conf
ADD bin/ bin
VOLUME ["/data/db"]
RUN apt-get install nano -y
EXPOSE 8001
EXPOSE 27017