#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

url="http://localhost:8080/j_acegi_security_check"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

d={
    "j_username":"qqssxx987",
    "j_password":"1234568",
    "from":"/",
    "Jenkins-Crumb":"c5cfa968c925619c0764de981a7786a2",
    "json":{"j_username": "qqssxx987",
            "j_password": "1234568",
            "remember_me": False,
            "from": "/",
            "Jenkins-Crumb": "c5cfa968c925619c0764de981a7786a2"
            },
    "Submit":u"登录"
}
s = requests.session()
r=s.post(url,headers=headers,data=d)
t=re.findall(r'<b>(.+?)</b>',r.content)
print t[0]
print t[1]
# print r.content
