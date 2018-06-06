#-*-coding:utf-8-*- 
from selenium import webdriver


all=[65,63,52,48,20,5,4,1]

for i in range(len(all)-1):
    for j in range(len(all)-1):
        if all[j]>all[j+1]:
            all[j], all[j+1] = all[j+1], all[j]
    print (all)

