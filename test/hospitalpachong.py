#-*-coding:utf-8-*- 
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import requests,time
import csv,json,re
from urllib.parse import quote
url="http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx"
s = requests.Session()
r = s.get(url)
string1 = re.findall(r'id="__VIEWSTATE" value="(.*)"',r.text)
string2 = re.findall(r'id="__VIEWSTATEGENERATOR" value="(.*)"',r.text)
string3 = re.findall(r'id="__EVENTVALIDATION" value="(.*)"',r.text)
pagenum = 2
print(string1)
print(string2)
print(string3)
h={
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Referer':'http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx',
}
body="__VIEWSTATE="+quote(str(string1[0]), safe='')+"&"+\
    "__VIEWSTATEGENERATOR="+quote(str(string2[0]), safe='')+ "&" + \
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

r=s.post(url,headers=h,data=body)
m=r.content.decode("utf-8")

soup=BeautifulSoup(m,"html.parser")
# 多属性爬
table=soup.find("table",{"class":"mainlist","id":"ctl00_ContentPlaceHolder1_gvwAppraiseInfo"})
# 继续爬
print(table)
data=table.find_all("th")
data2=table.find_all("tr")
print(table.find_all("td"))
# list=[]
# for i in data2[0]:
#     if i.string=='\n':
#         continue
#     else:
#         list.append(i.string)
# for i in range(0,len(data2)):
#     data3=data2[i]
#     list1 = []
#     for a in data3:
#         if a.string == '\n':
#             continue
#         else:
#             list1.append(a.string)
#     with open("hospital.csv", 'a+', newline='') as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow(list1)
# print(list)






#
# data2=table.find_all("tr")
# for i in data2:
#     if len(i.find_all("td"))==0:
#         continue
#     else:
#         print(i.find_all("td"))
#
# data3=data2[1]
#
# for i in range(1,len(data2)):
#     data=data2[i]
#     for i in data:
#         print(i.string)

