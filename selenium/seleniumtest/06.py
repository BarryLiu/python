# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
import daili
import os,time
from selenium import webdriver
#import selenium.common.exceptions.NoSuchElementException
from selenium.common.exceptions import NoSuchElementException

chromeOptions = webdriver.ChromeOptions()
# proxy_url = daili.getIp()
# proxy_server = "--proxy-server="+proxy_url
# print('proxy_server = '+proxy_server)

# 设置代理
chromeOptions.add_argument("--proxy-server=http://192.168.86.24:8889")
# chromeOptions.add_argument(proxy_server)
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://192.168.86.24:8889
#driver = webdriver.Chrome(chrome_options = chromeOptions)
driver = webdriver.Chrome()

def loop_page(next_a):
    while next_a != None:
        next_a.click()
        print('当前页面:'+driver.current_url)
        #间断性的下拉滚动窗口  
        for i in range(0,1000,50):
            js = "var q=document.documentElement.scrollTop="+ str(i)
            driver.execute_script(js)
            time.sleep(1)
        
        driver.implicitly_wait(5)
        #time.sleep(5)
        try:
            next_a = driver.find_element_by_css_selector('div.nex > p > a')
        except NoSuchElementException  as e:
            next_a = None
            pass
       
    print('请求完成!!!!  ')


print('aaa')
if __name__=='__main__':
    print('bbb')
    # 查看本机ip，查看代理是否起作用
    driver.get("http://httpbin.org/ip") 
    # time.sleep(1)
    driver.get('http://itaren.com/2012/12/30/share-windows-and-linux/')
    # driver.get('http://itaren.com/2018/08/17/scrapy/')
    
    next_a = driver.find_element_by_css_selector('div.nex > p > a')
    print('当前页面:'+driver.current_url)
    # time.sleep(5)
    loop_page(next_a)

    # 退出，清除浏览器缓存
    driver.quit()