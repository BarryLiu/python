# 
# 
# class Foo:
# 
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   
#   def detail(self):
#     print(self.name)
#     print(self.age)
#   
# obj1 = Foo('chengd', 18)
# obj1.detail()  # Python默认会将obj1传给self参数，即：obj1.detail(obj1)，所以，此时方法内部的 self ＝ obj1，即：self.name 是 chengd ；self.age 是 18
#   
# obj2 = Foo('python', 99)
# obj2.detail()  # Python默认会将obj2传给self参数，即：obj1.detail(obj2)，所以，此时方法内部的 self ＝ obj2，即：self.name 是 python ； self.age 是 99x

# from urllib import request
# 
# req = request.urlopen("http://www.baidu.com")
# print(req.read().decode("utf-8"))

from bs4 import BeautifulSoup
from urllib import request #
import re  # 正则表达式模块

html = request.urlopen("http://itaren.com/WebDemos").read().decode("utf-8");
# print(html)
bs = BeautifulSoup(html,"html.parser") # 查找解析器
print("-------- bs.title ----")
print(bs.title)  # 直接点标签名可以取到第一个
print("-------- bs.prettify() ----")
# print(bs.prettify())


print("-------- \n----")
print(bs.find(id='footer_wrap'))#通过id查找
print(bs.find(id='footer_wrap').string)
print(bs.findAll("a"))  # 通过标签查找,返回集合

print("------------")   # 循环标签打印
for link in bs.findAll("a"):
    print(link)
    
print("-----输出div下面所有 class为highlight的文本内容------")
print(bs.find("div",{"class":"highlight"}).get_text())

print("-----正则表达式搜索")
for tag in bs.find_all(re.compile("^d")):
    print("-----")
    print(tag)
