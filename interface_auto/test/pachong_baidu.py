#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import os
import urllib3
urllib3.disable_warnings()

r = requests.get("http://image.baidu.com/")
blog=r.content
soup=BeautifulSoup(blog,"html.parser")
p=soup.find_all(class_="imgrow")
print p

