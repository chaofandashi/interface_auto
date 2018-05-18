#-*-coding:utf-8-*- 
from selenium import webdriver
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
URL = 'http://finance.qq.com'


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find('div', {'id': 'listZone'}).findAll('a')
    return soup


def main():
    with open("hello.csv", "w") as fh:
        fh.write("url\ttitile\n")
        for item in get_data(URL + "/gdyw.htm"):
            fh.write("{}\t{}\n".format(URL + item.get("href"), item.get_text()))


if __name__ == "__main__":
    main()