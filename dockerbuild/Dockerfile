# KLS Project Dockerfile

# Base Image
FROM ubuntu:16.04

# Install requirements
RUN \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential && \
	apt-get install -y software-properties-common && \
	apt-get install -y curl git vim wget unzip python-pip python-dev && \
	pip install virtualenv

# Install mongo
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update && apt-get install -y mongodb-org
RUN mkdir -p /data/db

# Install Supervisor to run multiple services
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Install the code and set up flask
RUN cd /opt && wget https://github.com/terrabyteian/kls-project/archive/master.zip
RUN cd /opt && unzip master.zip

# expose frontend and start up supervisor
EXPOSE 5000
CMD ["/usr/bin/supervisord"]
