#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import re
s=requests.session()

def login(s,url,payload):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "UM_distinctid=15f24f4804f20c-0a1c110c2e3bfd-57e1b3c-1fa400-15f24f4805029b; Hm_lvt_88e110cc097c67c394f60bd3cf28fe1d=1511370921; ASP.NET_SessionId=wzwappklsg2mqqmyaexbso24; _ga=GA1.2.2112019853.1508149352; _gid=GA1.2.1234247461.1516418466; SERVERID=34e1ee01aa40e94e2474dffd938824db|1516421434|1516417358",
        "Connection": "keep-alive"
    }

if __name__ == "__main__":
    pass