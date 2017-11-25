FROM python:2.7-slim
ADD requirements.txt /opt/
RUN pip install -r /opt/requirements.txt
ADD *.py /opt/
WORKDIR /opt/
