#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import time
import json
from urllib.parse import quote

s = requests.Session()
r = s.get("http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx")

string1 = re.findall(r'id="__VIEWSTATE" value="(.*)"',r.text)
string2 = re.findall(r'id="__VIEWSTATEGENERATOR" value="(.*)"',r.text)
string3 = re.findall(r'id="__EVENTVALIDATION" value="(.*)"',r.text)
string4 = r.headers['Set-Cookie']
pagenum = 2

print("分割线".center(80,'-'))

header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
    # 'Cookie':'ASP.NET_SessionId=nqzt522vw1lqecjef3tq3dfh',
    # 'Cookie':string4,
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer':'http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx',
    'Content-Length':'7044',
    'Host':'www.ahyycg.cn'
    }

seq = "__VIEWSTATE="+quote(str(string1[0]), safe='')+"&"+"__VIEWSTATEGENERATOR="+quote(str(string2[0]), safe='')+ "&" + \
       "__EVENTTARGET=ctl00%24ContentPlaceHolder1%24pager1"+ "&" + \
       "__EVENTARGUMENT="+str(pagenum)+ "&" + \
       "__EVENTVALIDATION="+quote(str(string3[0]), safe='')+ "&" + \
       "input="+ "&" + \
       "input="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtGoodsID="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtPack="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtComSC="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtProductName="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtMedicineModel="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtOutlookc="

r1 = s.post(url="http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx",headers=header,data=seq)
print(r1.text)
