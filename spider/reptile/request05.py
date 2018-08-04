#coding=utf-8
import os
import requests,bs4
import logging
import time
from  urllib import parse

'''
简单使用session发送请求
'''
session = requests.session();


def login():
    loginUrl = 'http://192.168.1.67:8093/console/sys/login'
    data = {'username':'msadmin','password':'123456','captcha':'supervalid54321'}
    referer = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer':'http://192.168.1.67:8093',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    cookies={
        'SESSION':'82b872af-afb0-40c5-b228-5aebcfed82b7',
    }
    cookies_str = 'SESSION=82b872af-afb0-40c5-b228-5aebcfed82b7; sidebar_collapsed=false; remember_user_token=W1syMV0sIiQyYSQxMCQ2eDJBbFY3LklJVHpTLnMxdHA0UFR1IiwiMTUzMjk5OTE2OS45NjQ3ODIiXQ%3D%3D--945639d1bdf4382757b9f66783dade340ecbdd43; _gitlab_session=8060e1225018c74f3450d994d3267a3f'
    cookie_items = cookies_str.split("; ")
    for item in  cookie_items:
        a = item.split("=")
        cookies[a[0]]=a[1]
    session.get('http://192.168.1.67:8093/console/captcha.jpg',data=data,headers=referer,cookies=cookies)
    html = session.post(loginUrl,data=data,headers=referer,cookies=cookies)
    login_json = html.json()
    assert login_json['code']=='0000'

    logging.info("login success!!!")


def get_user_list():
    url = 'http://192.168.1.67:8093/console/user/userList/userDetails?schoolId=10040&userId=21227&keyWord=&pageSize=10&userType=1&pageNum=1'
    user_data = session.post(url=url).json()
    print('user_data',user_data)
    pass


if __name__=="__main__":

    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.INFO)

    login()

    get_user_list()
    logging.warning("程序开始下载")