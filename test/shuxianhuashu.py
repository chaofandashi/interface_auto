#-*-coding:utf-8-*- 
from selenium import webdriver
a=range(10000)
all=[]
for i in a:
   c=i+1
   if 10<i<100:
       num1=i/10
       num2=i%10
       if num1**3+num2**3==i:
           all.append(i)
   elif 100<i<1000:
       num4=i/100
       num5=i%100/10
       num6=i%10
       if num4**3+num5**3+num6**3==i:
           all.append(i)
   elif 1000<i<10000:
       num7=i/1000
       num8=i%100%10
       num9=i%10%10
       num11=i%10
       if num7**3+num8**3+num9**3+num11**3==i:
           all.append(i)
print all