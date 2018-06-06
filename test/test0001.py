#-*-coding:utf-8-*- 
from selenium import webdriver
#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
ele=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(ele).perform()  #传driver参数，因为通过driver参数管理起来的