#-*-coding:utf-8-*- 
from selenium import webdriver
import unittest
import requests

class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers={
	            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            }
        self.s=requests.session()

    def test_yunda(self):
        danhao='1202247993797'
        kd="yunda"
        self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao, kd)
        print (self.url)
        r=self.s.get(self.url,headers=self.headers,verify=False)
        result = r.json()

        print (result['company'])
        data=result["data"]
        print (data[0])
        get_result=data[0]['context']
        print (11111)
        print (get_result)

        self.assertEqual(u"韵达快递", result['company'])
        self.assertIn(u"已签收", get_result)

    def test_tiantian(self):
        danhao="200504452283"
        kd="yuantong"
        self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao,kd)
        print (self.url)

        r=self.s.get(self.url,headers=self.headers,verify=False)
        result=r.json()

        print (result['company'])
        data = result["data"]
        print (data[0])
        get_result = data[0]['context']
        print (get_result)
        self.assertEqual(u"圆通快递",result['company'])
        self.assertIn(u"已签收", get_result)
if __name__ == "__main__":
    unittest.main()