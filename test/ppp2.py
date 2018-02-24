#-*-coding:utf-8-*-
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
import unittest
import time
import re
#禁用安全警告
# urllib3.disable_warnings()

url="https://www.baidu.com"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Cookie":"_ga=GA1.2.1621354742.1519443840; _gid=GA1.2.1031460666.1519443840; __utma=59123430.1621354742.1519443840.1519452779.1519452779.1; __utmc=59123430; __utmz=59123430.1519452779.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=59123430.4.10.1519452779"
}
r=requests.get(url)

print (r.status_code)
print (r.headers)
print (r.text)

