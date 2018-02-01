#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings()

headers={
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Referer":"http://www.kuaidi.com/",
    "Cookie":"lang=zh-cn; theme=default; sid=a76h1u3jormln2ks88i0s9etk1; UM_distinctid=161504ea2675e6-0c91b8fa5da147-3b604c04-1fa400-161504ea268721; CNZZDATA1254194234=1681760608-1517468775-%7C1517468775"

}
url="http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
s=requests.session()
r = s.get(url,headers=headers)
result=r.json()
data=result['data']
print data
print data[0]["context"]