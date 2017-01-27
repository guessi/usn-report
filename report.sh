#!/bin/bash

set -e

echo "==> $(date)"

echo "==> generate report"
./usn-report-retriever.py > report/temp.html

echo "==> beautify report"
python -m BeautifulSoup < report/temp.html > report/$(date +%Y%m%d).html

echo "==> sending report"
./usn-report-sendmail.py

echo "==> remove temporary files"
rm -f report/temp.html

echo "==> done"
