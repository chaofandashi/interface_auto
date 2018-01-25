#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

r=requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing=r.content
soup=BeautifulSoup(fengjing,"html.parser")

images=soup.find_all(class_="lazy")
print images
print os.getcwd()
for i in images:
    try:
        jpg_url=i["data-original"]
        title=i["title"]
        print title
        print jpg_url
        print ""
        with open(os.getcwd()+"\\jpg\\"+ title + '.jpg', "wb") as f:
            f.write(requests.get(jpg_url).content)
    except:
        pass
