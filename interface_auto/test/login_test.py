#-*-coding:utf-8-*- 
from selenium import webdriver
import requests
import re
s=requests.session()

def login(s,url,payload):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "UM_distinctid=15f24f4804f20c-0a1c110c2e3bfd-57e1b3c-1fa400-15f24f4805029b; Hm_lvt_88e110cc097c67c394f60bd3cf28fe1d=1511370921; ASP.NET_SessionId=wzwappklsg2mqqmyaexbso24; _ga=GA1.2.2112019853.1508149352; _gid=GA1.2.1234247461.1516418466; SERVERID=34e1ee01aa40e94e2474dffd938824db|1516421434|1516417358",
        "Connection": "keep-alive"
    }
    r=s.post(url,json=payload,headers=headers,verity=False)
    result=r.json()
    print result
    return result['success']
def save_box(s,url2,tutle,body_data):
    body = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "FE27D343",
            "Editor$Edit$txbTitle": title,
            "Editor$Edit$EditorBody": "<p>" + body_data + "</p>",
            "Editor$Edit$Advanced$ckbPublished": "on",
            "Editor$Edit$Advanced$chkDisplayHomePage": "on",
            "Editor$Edit$Advanced$chkComments": "on",
            "Editor$Edit$Advanced$chkMainSyndication": "on",
            "Editor$Edit$lkbDraft": u"存为草稿",
            }
    r2=s.post(url2,data=body,verift=False)
    print r2.url
    return r2.url
def get_postid(u):
    postid = re.findall(r"postid=(.+?)&", u)
    print postid  # 这里是 list
    if len(postid) < 1:
        return ''
    else:
        return postid[0]

def delete_box(s, url3, postid):
    json3 = {"postId": postid}
    r3 = s.post(url3, json=json3, verify=False)
    print r3.json()
if __name__ == "__main__":
    url = "https://passport.cnblogs.com/user/signin"
    payload = {
    "input1": "x9iFiUQ4dfHyV72zwM4AQsden2TX722s3tm3slmPc/IL8uCi7g/OZH2qziBqICnxqRrEq8lxOLSlme/qmtGwHYAz7CERcEpMkikavNkXe+yleRhoHPyuZ2kFtvNGub7ULWq8ZJNkit+lMP74F0PH8MJbGbTCyvMVDv0/OlvHDQw=",
    "input2": "NuaG0eb2LzaZ0jQBa3CEPfzkznr9y0E6P2sOJnFWVGYP1z4SpSgBhbgp9liztDzz3nbSG2Utuh1wvK8tMTxf5pFpZPKp5d2e78hz9EDpDw7jHmcmC8l1LCqc7eMvlVcH6aDWl1xagaVset6ZyNI00skoR+fOzRV/8FrrOIKpVqs=",
    "remember": True
    }
    s = requests.session()
    login(s, url, payload)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    u = save_box(s, url2, u"标题", u"正文内容")
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    delete_box(s, url3, postid)