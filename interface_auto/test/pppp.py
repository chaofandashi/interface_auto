#-*-coding:utf-8-*-
import requests
import urllib3
from bs4 import BeautifulSoup
import time
import re
#禁用安全警告
urllib3.disable_warnings()

print('time1:',time.strftime("%Y%m%d%H%M%S",time.localtime()))

url = 'https://movie.douban.com/ '
res = requests.get(url,verify=False)
soup = BeautifulSoup(res.content,'lxml')
titles = soup.find_all('li',class_='title')
rating = list(soup.find_all('span',class_='subject-rate'))
for title in titles:
    siblings = list(title.next_siblings)
    spans = siblings[1].contents
    for span in spans:
        try:
            if span['class'][0] == 'subject-rate':
                span_previous_sibling = span.previous_sibling
                star = int(span_previous_sibling['class'][1][-2:])/10.
                print('电影名称：%s，评分：%s，评星：%s' % (title.a.string, span.string,star))
            elif span['class'][0] == 'text-tip':
                print('电影名称：%s，评分：%s' % (title.a.string, span.string))
        except TypeError as msg:
            pass
print('time2:',time.strftime("%Y%m%d%H%M%S",time.localtime()))