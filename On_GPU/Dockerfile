FROM ubuntu:latest 

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y libopencv-dev python-opencv python-pip && pip install paho-mqtt 

ADD capture.py /
CMD python capture.py

