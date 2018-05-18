#-*-coding:utf-8-*- 
from selenium import webdriver
a=range(100,1000)
all=[]
print(a)
for i in a:
   num4=int(i/100)
   num5=int(i/10%10)
   num6=int(i%10)
   if num4**3+num5**3+num6**3==i:
       print(num4+num5+num6)
       all.append(i)
print (all)




