#-*-coding:utf-8-*- 
from selenium import webdriver


all=[5,2,45,2,56,2,14,65,36]

for i in range(len(all)-1):
    for j in range(len(all)-1):
        if all[j]>all[j+1]:
            all[j], all[j+1] = all[j+1], all[j]
print all

