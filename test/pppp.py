#-*-coding:utf-8-*-
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
import unittest
import time
import re
#禁用安全警告
urllib3.disable_warnings()

r=requests.get("https://www.qiushibaike.com/")
blog=r.content
soup=BeautifulSoup(blog,"html.parser")
times=soup.find_all(class_="content")
print (times)
for i in times:
    print (i.span.contents[0])

