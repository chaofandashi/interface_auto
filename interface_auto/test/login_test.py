#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import re


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
url = "https://passport.baidu.com/v2/api/?login"
s=requests.session()
r = s.get(url, headers=headers,verify=False)
print s.cookies
print r.content
c = requests.cookies.RequestsCookieJar()
c.set("BAIDUID=","1A420958A3B31C2C9AC5800F8FC4E402:FG=1")
c.set("PSTM","1515988853")
c.set("BIDUPSID","DA2F4CA95DA2C80B8044D349321BB91E")
c.set("HOSUPPORT","1")
c.set("UBI","fi_PncwhpxZ%7ETaKAd%7EjeCEwFNNvq9kfmmW1cfqn%7EIDHVJUFfocCtV-lwLB4svgyNdGySf0abqsCNXxIo3w9")
c.set("HISTORY","e33ac23a106d4251aa0a82c20ca811a957ae1a7eab55df65")
c.set("SAVEUSERID","e0402cfe5a87f0c66329e480f38f5579574500dd")
c.set("USERNAMETYPE","2")
c.set("BDORZ","B490B5EBF6F3CD402E515D22BCDA1598")
c.set("locale","zh")
c.set("pgv_pvi","1956250624")
c.set("FP_UID","b2475d7df40fb01ea5757fdfff49dcfc")
c.set("H_PS_PSSID","1469_21107_22072")
s.cookies.update(c)
print s.cookies
print r.text