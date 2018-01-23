#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

r=requests.get("http://www.cnblogs.com/yoyoketang/")

blog=r.content
soup=BeautifulSoup(blog,"html.parser")
times=soup.find_all(class_="dayTitle")
title = soup.find_all(class_="postTitle")
for i in title:
    print i.a.string
descs = soup.find_all(class_="postCon")
for i, j, k in zip(times,title,descs):
    print i.a.string
    print j.a.string
    print k.div.contents[0]
    print ""