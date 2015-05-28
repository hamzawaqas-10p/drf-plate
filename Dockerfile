FROM ubuntu
MAINTAINER Hamza Waqas
WORKDIR /code
RUN apt-get update
RUN apt-get install python3-setuptools -y
RUN easy_install3 pip
RUN alias python=python3
RUN alias pip=pip3
RUN alias easy_install=easy_install3
RUN apt-get install git -y
RUN git clone https://github.com/hamzawaqas-10p/drf-plate.git mbo
RUN pip install --upgrade virtualenv
WORKDIR /code/mbo
RUN virtualenv env
CMD ["source", "./env/bin/activate"]
RUN ["pip", "install", "-r", "requirements.txt"]
ADD ./data data
ADD conf/ conf
ADD bin/ bin
VOLUME ["/data/db"]
RUN apt-get install nano -y
EXPOSE 8001
EXPOSE 27017