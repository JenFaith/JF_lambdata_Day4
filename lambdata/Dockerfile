#Getting base image ubuntu
FROM ubuntu

MAINTAINER jennifer faith <jennifer.faith16@gmail.com>

WORKDIR /Users/jenniferquigley/DS22/JF\ -/lambdata/lambdata

COPY . .

RUN apt-get update && \
	apt-get upgrade -y  && \
	apt install python3 python3-pip curl -y && \
	pip3 install pandas numpy

CMD ['helper_function.py']
