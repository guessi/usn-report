#!/usr/bin/env python3

import os.path

from datetime import datetime
from email.mime.text import MIMEText
from smtplib import SMTP


def get_report(subject, sender, recipient):
    # detect report file's existence
    if not os.path.isfile('report.html'):
        print('can not find report file: report.html')
        exit(1)

    # read report from file
    fp = open('report.html', 'rb')
    msg = MIMEText(fp.read(), 'html', 'utf-8')
    fp.close()

    # setup mail content
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    return msg


def send_report(smtp_server, sender, recipient, msg):
    try:
        smtp = SMTP(smtp_server)
        smtp.sendmail(sender, recipient, msg.as_string())
        smtp.quit()
    except Exception as e:
        print("Error, failed to send report. " + str(e))


if __name__ == '__main__':
    date = datetime.now().strftime("%Y%m%d")
    subject = 'Ubuntu Security Notices Report ({0})'.format(date)
    sender = 'no-reply@example.com'
    smtp_server = os.getenv('SMTP_SERVER', default='msa.hinet.net')
    recipient = os.getenv('RECIPIENT', default='guessi@gmail.com')

    msg = get_report(subject, sender, recipient)
    send_report(smtp_server, sender, recipient, msg)
