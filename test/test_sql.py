#-*-coding:utf-8-*- 
from selenium import webdriver

import pymysql


db=pymysql.connect(host='47.98.214.128',
                     port=3306,
                     user='test',
                     password='test123',
                     db='test'
                     )
cursor=db.cursor()
sql = """delete from EMPLOYEE where age=20"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

cursor.execute('SELECT * FROM EMPLOYEE')
print (cursor.fetchall())
cursor.close()
db.close()