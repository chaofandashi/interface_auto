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
    "remember_me":"on",
    "Jenkins-Crumb":"31219746d2d26ad37c1eaae482e82835",
    "json":{
        "j_username": "qqssxx987",
        "j_password": "1234568",
        "remember_me": True,
        "from": "/",
        "Jenkins-Crumb": "31219746d2d26ad37c1eaae482e82835"
    },
    "Submit":u"登录"
}

r=requests.post(url,headers=headers,data=d)
print (r.content)


