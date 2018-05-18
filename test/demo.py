#-*-coding:utf-8-*-
from selenium import webdriver

import csv
csvfile = open('csvtest.csv', 'w')
writer = csv.writer(csvfile)

data = [
  ['1', 'http://www.xiaoheiseo.com/', '小黑'],
  ['2', 'http://www.baidu.com/', '百度'],
  ['3', 'http://www.jd.com/', '京东']
]
for i in data:
    print(i)
writer.writerows(data)
csvfile.close()