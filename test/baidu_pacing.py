#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os,time
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
# url="https://sf.taobao.com/court_item.htm?spm=a213w.7398554.pagination.2.i3PLXP&user_id=2825285724&auction_start_seg=-1&page=1"
url="http://www.ishuhui.com/"
r=requests.get(url,headers=headers)
print(r.encoding)
print r.content.decode("utf-8")







# res=r.content.decode("GBK")
# print(res)
# soup=BeautifulSoup(res,"html.parser")
# print (soup.title.string)
# print (soup.find_all("a")[0].attrs)
#
# res2=soup.find_all(class_="pai-item pai-status-doing")
# print(res2)
# images=soup.find_all(class_="alt")
# print images
# print os.getcwd()
# for i in images:
#     try:
#         jpg_url=i["data-original"]
#         title=i["title"]
#         print title
#         print jpg_url
#         print ""
#         with open(os.getcwd()+"\\jpg\\"+ title + '.jpg', "wb") as f:
#             f.write(requests.get(jpg_url).content)
#     except:
#         pass
