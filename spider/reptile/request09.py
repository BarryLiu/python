# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re,time,random


# 自己添加随机请求头
agents = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
]



def get_proxys(page = 1):
    """
    函数说明:获取IP代理
    Parameters:
        page - 高匿代理页数,默认获取第一页
    Returns:
        proxys_list - 代理列表
    """
    #if True:
    #    return ['http://127.0.0.1:8888']
    #西祠代理高匿IP地址
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    #完善的headers
    target_headers = {'Upgrade-Insecure-Requests':'1',
                      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Referer':'http://www.xicidaili.com/nn/',
                      'Accept-Encoding':'gzip, deflate, sdch',
                      'Accept-Language':'zh-CN,zh;q=0.8',
                      }
    #get请求
    target_response = requests.session().get(url = target_url, headers = target_headers,verify=False)
    #utf-8编码
    target_response.encoding = 'utf-8'
    bf1_ip_list = BeautifulSoup(target_response.text, 'html.parser')
    bf2_ip_list = bf1_ip_list.select_one("#ip_list")
    tr_list = bf2_ip_list.find_all('tr')

    proxys_list = []
    #爬取每个代理信息
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) <=0:
            continue
        ip = td_list[1] #dom.xpath('//td[2]')
        port = td_list[2] #dom.xpath('//td[3]')
        protocol = td_list[5]  #dom.xpath('//td[6]')
        proxys_list.append(protocol.text.lower() + '://' + ip.text + ':' + port.text)
    #返回代理列表
    return proxys_list

def get_proxy_page():
    urls = get_urls()
    while True:
        req_urls(urls)
        print('页面刷完成',time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(60)
    pass
def  req_urls(urls):
    for url in urls:
        try:
            print('访问页面: %s'%url)
            user_agent = random.choice(agents)#随机取个代理头
            request_url(url=url,user_agent=user_agent)
            time.sleep(1)
        except BaseException as e:
            print('页面访问错误',url,e)
            pass
        pass
    pass

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
        'Referer': 'https://www.baidu.com/s?ie=ut'}

def get_urls():
    ''' 要请求的url列表 '''
    #urls = ['https://blog.csdn.net/weixin_41205148/article/details/97374886','https://blog.csdn.net/weixin_41205148/article/details/97374886']
    url='https://blog.csdn.net/weixin_41205148/article/list/%d?'
    urls = []
    for i in range(1,10):
        response = requests.get(url%i, headers=headers,verify=False)
        html = BeautifulSoup(response.text,"html.parser")
        alist = html.select("#mainBox > main > div.article-list > div > p > a")
        cur_urls = [a['href'] for a in alist]
        if len(cur_urls)== 0:
            break
        urls= urls + cur_urls
    return urls


def request_url(url='https://blog.csdn.net/weixin_41205148/article/details/97374886',proxy='http://127.0.0.1:8888',user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'):
    ''' 请求一个地址 '''
    headers = {'User-Agent': user_agent,'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=on%20duplicate%20key%20update%E7%AE%80%E5%8D%95%E4%BD%BF%E7%94%A8&rsv_pq=a72037cb006288fe&rsv_t=3aa0hJuPq3iCmRi9Ev7XJXrERym9yBU4dDVFk5WVSoAoxXcSvVTFqYCfLRk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_n=2&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=1093&rsv_sug4=1093'}
    proxies = {proxy.split("://")[0]: proxy}
    request  = requests.get(url,headers=headers,proxies=proxies,verify=False)
    if request.status_code != 200:
        print("请求返回失败!不是200")
        raise  Exception
    #soup = bs4.BeautifulSoup(request.content, 'html.parser')
    pass

if __name__ == "__main__":
    #print(get_proxys(1))
    #request_url()
    #print(get_urls())
    get_proxy_page()
    pass