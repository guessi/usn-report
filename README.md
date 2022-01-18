# Ubuntu Security Notices Report Generator

Get latest security report from upstream [Ubuntu Security Notices](https://www.ubuntu.com/usn/)


### Usage

Generate Report

    $ ./report-gen.py > report.html

Send Report

    $ export SMTP_SERVER='msa.hinet.net'
    $ export RECIPIENT='kuole_mei@trend.com.tw'
    $ ./report-send.py


### Dockerized as Tool

Generate report File

    $ docker run -it guessi/usn-report         \
        /opt/report-gen.py > report.html

Send out report

    $ docker run                               \
        -e SMTP_SERVER=msa.hinet.net           \
        -e RECIPIENT=guessi@gmail.com          \
        -v $(pwd)/report.html:/opt/report.html \
        -it guessi/usn-report                  \
        /opt/report-send.py
