# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os 
import time
import random
import re


class ManHua():

	def __init__(self,url):
		self.url=url
		pass
	def run(self):

		print('下载图片pic')
		pass


class ManHuaPage():

	def __init__(self,url,content):
		self.url=url
		self.content=content
		pass

	def parse_detail(self,detail_url='https://www.bnmanhua.com/comic/2974/928934.html?p=1'):
		

		pass
	def down_pic(self,url,targetDir): 
		print('下载图片pic',url,targetDir)


		pass



if __name__=='__main__2':
	print("开始下载啦")
	mh = ManHua(url="https://m.bnmanhua.com")
	mh.run()






from selenium import webdriver

if __name__=='__main__':
	driver = webdriver.Chrome() 
	index = 1
	inp = ''
	courses = []
	print('输入q 终止循环,输入a添加记录并循环,输入其它任意继续循环')
	while(inp!=None and inp != 'q'):
		course_url = 'https://www.imooc.com/course/programdetail/pid/%d'%index
		driver.get(course_url)
		index = index +1

		elements = driver.find_elements_by_class_name('errorwarp')
		if len(elements)>0:
			print('\t页面错误: url=%s'%course_url)
			continue
		inp = input("输入操作:")
		
		if inp !=None and inp=='a': 
			courses.append(course_url) 
		pass
	print(courses)