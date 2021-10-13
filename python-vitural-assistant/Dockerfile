# FROM python:3.8

# COPY . /app
# WORKDIR /app

# RUN apt-get update && apt-get upgrade -y
# RUN apt-get install espeak -y
# RUN apt-get install ffmpeg -y
# RUN apt-get install libespeak1 -y
# # RUN sudo apt-get install alsa-utils
# RUN python -m pip install -U -r requirements.txt


FROM ubuntu:latest

RUN apt-get update && \
      apt-get -y install sudo

COPY . /app

RUN sudo apt-get install -y python3-pip

RUN pip install --upgrade wheel

# RUN sudo apt-get install alsa-utils
RUN apt-get update && apt-get upgrade -y
RUN apt-get install espeak -y
RUN apt-get install ffmpeg -y
RUN apt-get install libespeak1 -y
RUN pip install pyttsx3


WORKDIR /app