#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os,time

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

# url="http://699pic.com/sousuo-218808-13-1-0-0-0.html"
# r=requests.get(url)
# m=r.content.decode("utf-8")
#
# soup=BeautifulSoup(m,"html.parser")
#
# all=soup.find_all(class_="list")
# for i in all:
#     url=i.a.img["data-original"]
#     title=i.a.img["title"]
#     r=requests.get(url)
#     with open(title+".jpg","wb") as f:
#         f.write(r.content)


r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing = r.content
soup = BeautifulSoup(fengjing, "html.parser")
# 找出所有的标签
images = soup.find_all(class_="lazy")
# print images # 返回 list 对象
for i in images:
    try:
        jpg_url=i["data-original"]
        title=i["title"]
        print (title)
        print (jpg_url)
        with open(os.getcwd()+"\\jpg\\"+ title + '.jpg', "wb") as f:
            f.write(requests.get(jpg_url).content)
    except:
        pass
