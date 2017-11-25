#!/usr/bin/env python

from datetime import datetime as dt
from lxml import etree, html

from bs4 import BeautifulSoup

import feedparser
import re

month_dict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def getDateString(rss, index):
    entry = rss.entries[index].summary_detail.value
    date_raw = re.search("<em>(.+?)</em>", entry).group(1)

    year = date_raw.split(',')[1].strip()
    month = date_raw.split(',')[0].split(' ')[1][:3]
    date = date_raw.split(',')[0].split(' ')[0][:-2]

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


rss = feedparser.parse('https://www.ubuntu.com/usn/rss.xml')
today = dt.now().date()
desire_days = 30
prev_date = ""

body = getSectionHeader()

for index in xrange(100):
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
