#-*-coding:utf-8-*- 
from selenium import webdriver
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        print ("beginging test")
    def tearDown(self):
        print ("close test")
    def testAdd(self):
        self.assertEqual((1+2),3)
        self.assertEqual((0+1),1)
    def testMultiply(self):
        self.assertEqual((0*10),0)
        self.assertEqual((6*8),48)

if __name__=="__main__":
    unittest.main()