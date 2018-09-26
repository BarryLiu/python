# -*- coding:utf-8 -*-
import argparse

import requests,urllib3
import fake_useragent
import re
from bs4 import BeautifulSoup
import logging
import sys,os
from contextlib import closing

"""
下载网站视频,requests下载,下载进度显示,网站没有做防爬机制
"""

logging.basicConfig(level=10,
                        format='%(asctime)s [%(module)s] %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

fa = fake_useragent.UserAgent()
headers = {'User-Agent': fa.random,
           'Referer': 'http://www.39cmm.com'}


def download_detail(detail_url):
	html = requests.get(detail_url,headers=headers)
	html.encoding='gb2312'

	b_html=BeautifulSoup(html.text,'html.parser')

	# video_url=b_html.select_one('#ckplayer_a1') # 因为对正则解析还不熟,先用字符串方式取
	pattern = re.compile("video=", re.MULTILINE | re.DOTALL)
	script =  b_html.find("script", text=pattern)
	group=pattern.search(script.text)
	b = group.string.split('\r\n')

	video_url = b[12][12:-3]
	target_dir = detail_url.split('/')[-2]
	video_name = b_html.select_one("title").text.split('在线观看')[0]

	logging.info('正在【%s】页面下载文件保存到【%s】,文件名称是【%s】，地址是【%s】'%(detail_url,target_dir,video_name,video_url))
	if os.path.exists(target_dir) == False:
		os.makedirs(target_dir)

	#requests.urlretrieve(url=video_url,filename='111.mp4',reporthook=Schedule)
	with closing(requests.get(video_url,headers = headers, stream=True,verify=False)) as response:
		chunk_size=1024
		content_size=int(response.headers['content-length'])
		data_count=0

		real_file = target_dir+'/'+video_name+'.'+video_url.split('.')[-1]
		# 存在并且和服务器上一样大就不用下载啦
		if os.path.exists(real_file) and os.path.getsize(real_file) == content_size:
			return

		with open(real_file,'wb') as file:
			for data in response.iter_content(chunk_size=chunk_size):
				file.write(data)
				data_count = data_count + len(data)
				now_jd = (data_count / content_size) * 100
				print("\r 文件下载进度: %d%%(%.2f/%.2f)M -%s" %(now_jd,data_count/1000/1000,content_size/1000/1000,video_url),end=" ")

		print('下载完成')
	# 下一个视频链接, 
	# start_url=b_html.select_one('#video_tags a')['href']
	# print(video_url,start_url)


if __name__ == '__main__':

	# download_detail('http://www.39cmm.com/video/2015-9/3187.html')
	# print('下载完成')

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', help=('页面格式.eg:http://www.39cmm.com/diao/se58_%d.html'),default='http://www.39cmm.com/diao/se58_%d.html')
	parser.add_argument('-p', '--lastpage', help=('下载开始页码(网站是倒叙显示所以倒叙下载),eg:9'),default='9')
	args = parser.parse_args()
	page_url = args.url
	lastpage= args.lastpage

	#一种分类下面的url
	page_url = 'http://www.39cmm.com/diao/se58_%d.html'
	print(page_url.split('.com'))
	num = 0
	for i in range(int(lastpage),0,-1):
		url = page_url%i
		print(url)
		html = requests.get(url,headers=headers)
		b_html=BeautifulSoup(html.content,'html.parser')
		links=b_html.select('.box a')
		links.reverse()# 倒序下载
		num+=len(links)
		j=0
		for a in links:
			j+=1
			print('\n\n\n\n 正在下载【%s】页面的第【%d】个视频,路径是【%s】'%(url,j,a['href']))
			try:
				download_detail('http://www.39cmm.com/'+a['href'])
			except Exception as e:
				logging.error('下载页面出错',e)
			
			
	print('下载完成,共【%d】个视频'%num)