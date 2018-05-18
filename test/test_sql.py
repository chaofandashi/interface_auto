#-*-coding:utf-8-*- 
from selenium import webdriver

import pymysql


conn=pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     db='test'
                     )
cursor=conn.cursor()
cursor.execute('insert into user (id, name,age) values (%s, %s,%s)', ['', 'sbc','25'])
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
cursor.rowcount
conn.commit()
cursor.execute('select * from user')
print (cursor.fetchall())
cursor.execute('delete from user where name="sbc"')
conn.commit()
cursor.execute('select * from user')
print (cursor.fetchall())
cursor.close()
conn.close()