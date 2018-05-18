# coding:utf-8
import requests
import json
import urllib3
import unittest
urllib3.disable_warnings()
class loginCase():
    def __init__(self,s):
        self.session = s
    def remen(self):  # 热门采购
            url = 'http://test.o2o.osm365.com:7777/Product/GetWholesaleProductTagList'
            header = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                # "Accept-Encoding": " gzip, deflate",
                "Host": "test.o2o.osm365.com:7777",
                "Origin": "http://test.o2o.osm365.com:9111",
                # "Referer:":"http://wholesale.osm365.com/html/new_product_list.html?htmlType=differenceHumberList_369&ps=eyJuYW1lIjoibmV3X3Byb2R1Y3RfbGlzdCIsInRpdGxlIjoi54Ot6YeH5ZWG5ZOBIiwiRGF0YSI6eyJ0YWdJRCI6IjEiLCJidXR0b25SaWdodE9uZSI6eyJDbGFzcyI6InYxLXRvcC1sYi0yIn19fQ==",
                # "User-Agent:":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
            }
            body = {
                {"RequestStamp": "stamp-1525681048778", "Callback": "110", "PostTime": 1525681048778,
                 "PostContent": {"pageNo": 1, "pageSize": 20, "BrandIDString": "", "ProductIDString": "",
                                 "CategoryIDString": "", "CategoryNoString": "", "ProductName": "", "SupplierName": "",
                                 "HighPrice": 0, "LowPrice": 0, "OrderRule": 0, "OrderType": 0, "SupplierID": -1,
                                 "BusinessType": 3, "KeyWord": "", "SupplierType": "", "MainPushGoodsType": "2",
                                 "MainPushGoodsID": "525", "TagID": "1", "IsHomeShow": 1}, "CustomApp": "BWEB",
                                "ApiCode": "Product/GetWholesaleProductTagList", "Platform": "PC",
                                "Token": "dbeab03d6a8d4e4fa9c2d29ff40c3fea", "PageNumber": 1, "PageSize": 20}
                 }
            r = self.session.post(url, json=body, headers=header, verify=False)
            return r
if __name__=='__main__':
    s = requests.session()
    login = loginCase(s)
    r = login.remen()
    print(r.content.decode("utf-8")) #输入接口返回结果，输入utf-8转码
    # print(data_dic['PostContent']['info']['Address'])  # 假设是str时，取返回值