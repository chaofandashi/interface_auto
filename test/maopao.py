#-*-coding:utf-8-*- 
from selenium import webdriver


all=[65,63,52,48,20,5,4,1]

for i in range(len(all)-1):
    for j in range(len(all)-1):
        if all[j]>all[j+1]:
            all[j], all[j+1] = all[j+1], all[j]
    print (all)

print("分隔符------------------")
list1=[3,2,1,9,10,78,6]

for i in range(len(list1)):
    for j in range(i+1):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
    print(list1)