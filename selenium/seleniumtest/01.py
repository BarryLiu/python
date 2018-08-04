from selenium import webdriver
import requests

# http://www.testclass.net/selenium_python
# 如果运行报错，没有驱动，需要下载 chromedriver配到环境变量里面去 http://npm.taobao.org/mirrors/chromedriver/  https://www.cnblogs.com/technologylife/p/5829944.html
driver = webdriver.Chrome()

# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
driver.get("http://baidu.com")
driver.close()


#基本操作
# driver.back() # 后退
# driver.forward()#前进
# driver.quit() # 退出驱动并关闭所有关联的窗口
# driver.close() #关闭当前窗口。
# driver.refresh() #刷新当前页面

#定位方式
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()