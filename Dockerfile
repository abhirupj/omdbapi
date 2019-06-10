FROM python
MAINTAINER Abhirup Jannu
LABEL version="1.3"
RUN apt-get -y update
RUN mkdir /python-program
RUN pip install requests
RUN pip install termcolor
ADD ./omdbapi.py /python-program/omdbapi.py
WORKDIR /python-program
CMD ["python omdbapi.py"]
