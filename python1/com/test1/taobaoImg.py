
#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re
from lxml import etree
import os

#定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    #print(html.decode('GBK'))
    return html

def getSecondUrl(html):
    tree = etree.HTML(html)
    nodeList = tree.xpath("//div[@class='lm10']/a/@href")
    return nodeList

def getThirdUrl(html):
    reg = r'class="biank1"><a href='
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    tree = etree.HTML(html)
    nodeList = tree.xpath("//div[@class='biank1']/a/@href")
    return nodeList

##下载
def check_save_path(save_path):
    try:
        os.mkdir(save_path)
    except Exception as e:
        print(e)

def get_image_name(image_link):
    file_name = os.path.basename(image_link)
    return file_name

def get_page_title_from_index_page(base_page_link):
    try:
        html_content = urllib.request.urlopen(url=base_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        page_title_list = html_tree.xpath('//td/div[@class="title"]')
        page_title_tmp = page_title_list[0].text
        return page_title_tmp
    except Exception as ex:
        print(ex)
        return ""  

def save_image(image_link, save_path):
    file_name = get_image_name(image_link)
    file_path = save_path + "\\" + file_name
    print("正在下载%s" % image_link)
    try:
        file_handler = open(file_path, "wb")
        image_handler = urllib.request.urlopen(url=image_link, timeout=5).read()
        file_handler.write(image_handler)
        # file_handler.closed()
    except Exception as ex:
        print(ex)

def get_image_from_web(base_page_link, save_path):
    check_save_path(save_path)
    page_link_list = get_page_link_list_from_index_page(base_page_link)
    x = 0 
    for page_link in page_link_list:
        #print('下载地址：'+page_link)
        image_link_list = get_image_link_from_web_page(page_link)
        for image_link in image_link_list:
            x = x + 1
            #print(image_link)
            save_image(image_link, save_path)

def get_image_link_from_web_page(web_page_link):
    image_link_list = []
    try:
        html_content = urllib.request.urlopen(url=web_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        link_list = html_tree.xpath('//p/img/@src')
        for link in link_list:
            if str(link).find("uploadfile"):
                image_link_list.append("http://www.xgyw.cc/" + link)
    except Exception as ex:
        print(ex)
        pass
    return image_link_list

def get_page_link_list_from_index_page(base_page_link):
    try:
        html_content = urllib.request.urlopen(url=base_page_link, timeout=5).read()
        #print(html_content)
        html_tree = etree.HTML(html_content)
        link_tmp_list = html_tree.xpath('//div[@class="page"]/a/@href')
        page_link_list = []
        for link_tmp in link_tmp_list:
            page_link_list.append("http://www.xgyw.cc/" + link_tmp)
        return page_link_list
    except Exception as ex:
        print(ex)
        return []



#开始调用
url = 'http://www.mmjpg.com/mm/1329';
html = getHtml(url) 

# third = getThirdUrl(html)
# print(len(third))
# for t in third:https://github.com/BarryLiu/python.git
#     print(t)
# print(urllib.request.urlopen(url))


nodeList = getSecondUrl(html)
nodeList.remove("/")
nodeList.remove("/html/")
#nodeList.remove("/Tgod/")
for secondUrl in nodeList:
    newUrl = 'http://www.xgyw.cc' + secondUrl
    se = secondUrl.split('/')[1]
    #print(newUrl)
    content = getHtml(newUrl) 
    third = getThirdUrl(content)
    #print(len(third))
    for t in third:
        th = t.split('/')[1]
        if(se == th):
            location = newUrl+'/'+t.split('/')[2]
            #print(location)
            page_title = get_page_title_from_index_page(location)
            #print(page_title)
            if(page_title != ""):
                save_path = "F:/python/images3/" + page_title
            else:
                save_path = "F:/python/images3_other/" + page_title
            #print(location+'...'+save_path)
            get_image_from_web(location, save_path)


