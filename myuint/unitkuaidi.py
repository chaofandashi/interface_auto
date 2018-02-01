import unittest
import requests

class Kuaidi_test(unittest.TestCase):
    def setUp(self):
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        }
        self.s=requests.session()
    def tearDown(self):
        pass
    def test_yunda(self,danhao="1202247993797",kd="yunda"):
        self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html"%(danhao,kd)
        print(self.url)
        r=self.s.get(self.url,headers=self.headers)
        result=r.json()
        data=result["data"]
        print data
        print data[0]["context"]
if __name__ == "__main__":
    unittest.main()