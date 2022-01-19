FROM python:3.10-slim
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD report-gen.py report-send.py /opt/
WORKDIR /opt/
