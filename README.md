# Ubuntu Security Notices Report Generator

[![Docker Stars](https://img.shields.io/docker/stars/guessi/usn-report.svg)](https://hub.docker.com/r/guessi/usn-report/)
[![Docker Pulls](https://img.shields.io/docker/pulls/guessi/usn-report.svg)](https://hub.docker.com/r/guessi/usn-report/)
[![Docker Automated](https://img.shields.io/docker/automated/guessi/usn-report.svg)](https://hub.docker.com/r/guessi/usn-report/)

Get latest security report from upstream [Ubuntu Security Notices](https://www.ubuntu.com/usn/)


### Usage

Generate Report

    $ ./report-gen.py > report.html

Send Report

    $ export SMTP_SERVER='msa.hinet.net'
    $ export RECIPIENT='kuole_mei@trend.com.tw'
    $ ./report-send.py


### Dockerized as Tool

    $ docker run -it guessi/usn-report         \
        /opt/report-gen.py > report.html

    $ docker run                               \
        -v $(pwd)/report.html:/opt/report.html \
        -it guessi/usn-report                  \
        /opt/report-send.py

OR

    $ docker run                               \
        -e SMTP_SERVER=msa.hinet.net           \
        -e RECIPIENT=guessi@gmail.com          \
        -v $(pwd)/report.html:/opt/report.html \
        -it guessi/usn-report                  \
        /opt/report-send.py
