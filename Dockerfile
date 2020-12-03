FROM ubuntu

ENV PYTHONBUFFER=1

RUN apt update && \
    apt upgrade && \
    apt install python3 python3-pip curl -y && \
    pip3 install numpy pandas
    pip3 install -i https://test.pypi.org/simple/ lambdata-Lopez-John==0.0.3