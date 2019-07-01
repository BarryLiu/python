# -*- coding: utf-8 -*-
"""
环境:python+ selenium
找就业班课程工具
    找慕课网实战就业班教程,看了下很多都是免费的，初级中级居多,质量应该还不错
"""
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
 
# 1跑到50: ['https://www.imooc.com/course/programdetail/pid/11', 'https://www.imooc.com/course/programdetail/pid/17', 'https://www.imooc.com/course/programdetail/pid/18', 'https://www.imooc.com/course/programdetail/pid/20', 'https://www.imooc.com/course/programdetail/pid/21', 'https://www.imooc.com/course/programdetail/pid/22', 'https://www.imooc.com/course/programdetail/pid/23', 'https://www.imooc.com/course/programdetail/pid/24', 'https://www.imooc.com/course/programdetail/pid/26', 'https://www.imooc.com/course/programdetail/pid/27', 'https://www.imooc.com/course/programdetail/pid/28', 'https://www.imooc.com/course/programdetail/pid/29', 'https://www.imooc.com/course/programdetail/pid/30', 'https://www.imooc.com/course/programdetail/pid/32', 'https://www.imooc.com/course/programdetail/pid/33', 'https://www.imooc.com/course/programdetail/pid/34', 'https://www.imooc.com/course/programdetail/pid/35', 'https://www.imooc.com/course/programdetail/pid/36', 'https://www.imooc.com/course/programdetail/pid/37', 'https://www.imooc.com/course/programdetail/pid/38', 'https://www.imooc.com/course/programdetail/pid/40', 'https://www.imooc.com/course/programdetail/pid/42', 'https://www.imooc.com/course/programdetail/pid/43', 'https://www.imooc.com/course/programdetail/pid/45', 'https://www.imooc.com/course/programdetail/pid/47', 'https://www.imooc.com/course/programdetail/pid/49']