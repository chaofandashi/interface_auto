#-*-coding:utf-8-*-
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
import unittest
import time
import re
import json
import urllib.parse
#禁用安全警告
urllib3.disable_warnings()

url="https://passport.baidu.com/v2/api/?login"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Cookie":"SAVEUSERID=e0402cfe5a87f0c66329e480f38f5579574500dd; UBI=fi_PncwhpxZ%7ETaKAbCz9C49D2DNUSWgTOnYW%7ECiGJiIX-KrVsbrzZ74DO4IzHqe1U5-RcA3QbbYSDhX5ATk; USERNAMETYPE=2; HOSUPPORT=1; HISTORY=e33ac23a106d4251aa0a82c20ca811a957ae1a7eab55df65; FP_UID=e5b1aa48826e7d24b0c639b14d9f715c; BAIDUID=E1D73F42C31B6A34693C83A242B81AD3:FG=1; BIDUPSID=E1D73F42C31B6A34693C83A242B81AD3; PSTM=1519377877; cflag=15%3A3; BDRCVFR[k2U9xfnuVt6]=mk3SLVN4HKm; H_PS_PSSID=25843_1422_21126_22160"
}
s=requests.session()
r=s.get(url,headers=header,verify=False)

c = requests.cookies.RequestsCookieJar()
c.set("BAIDUID",'E1D73F42C31B6A34693C83A242B81AD3:FG=1')
c.set('BIDUPSID','E1D73F42C31B6A34693C83A242B81AD3')

s.cookies.update(c)


import re

s=r'abc'
c='aasddasdaasdabcbxcabc'
c=re.findall(s,c)
print (c)