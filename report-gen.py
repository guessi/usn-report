#!/usr/bin/env python3

from bs4 import BeautifulSoup
from datetime import datetime as dt
from feedparser import parse as rss_parser
from lxml import etree, html

month_dict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def getDateString(rss, index):
    date_raw = rss.entries[index].published

    year = date_raw.split(' ')[3]
    month = date_raw.split(' ')[2]
    date = date_raw.split(' ')[1]

    return (year, month_dict.index(month) + 1, date)


def getContent(rss, year, month, date, prev_date):
    curr_date = "{0} {1}, {2}".format(month_dict[month - 1], date, year)

    if prev_date != curr_date:
        content = "<h4>{0}</h4>".format(curr_date)
    else:
        content = ""

    content += """
    <li><a style=\"text-decoration: none\" href=\"{0}\">{1}</a></li>
    """.format(rss.entries[index].link, rss.entries[index].title_detail.value)

    return curr_date, content


def getSectionHeader():
    return "<h3>Ubuntu Security Notices Report (AutoGen)</h3>"


rss = rss_parser('https://ubuntu.com/security/notices/rss.xml')
today = dt.now().date()
desire_days = 30
prev_date = ""

body = getSectionHeader()

for index in range(min(len(rss.entries), 50)):
    year, month, date = getDateString(rss, index)
    usn_date = dt.strptime(
        "{0}-{1}-{2}".format(year, month, date), '%Y-%m-%d').date()

    if (today - usn_date).days > desire_days:
        break

    prev_date, content = getContent(rss, year, month, date, prev_date)
    body += content

html_doc = etree.tostring(
               html.fromstring(body),
               encoding='unicode',
               pretty_print=True)

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
