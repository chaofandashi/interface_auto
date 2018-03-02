#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os,time

r=requests.get("https://sf.taobao.com/court_item.htm?spm=a213w.7398554.pagination.2.i3PLXP&user_id=2825285724&auction_start_seg=-1&page=1")
fengjing=r.content
soup=BeautifulSoup(fengjing,"html.parser")

print soup.find_all("a")[0].attrs
print soup.find_all("a")[0]["href"]
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
