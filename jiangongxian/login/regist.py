#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import urllib3
urllib3.disable_warnings()
import json
url="https://idev.bhsgd.net/jgx/client/holduser/regist"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
}
d={
    "username": "qq9965",
    "password": "123456",
    "introduceCode": "168496714invitation1520403190"
}
s=requests.session()
r=s.post(url,data=d,headers=header)
data=r.json()
print data
print data["code"]
print data["cnmsg"]

