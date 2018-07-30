import os
from collections import namedtuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys,getopt

'''
登录脚本,
登录homework或者登录zeus,各个环境下面的登录按照脚本参数登录,默认 测试zeus
运行语句:
    02.py  -e test -m zeus
'''


User = namedtuple("User",['username',"password"])
users = []
users.append(User(username='msadmin',password='123456'))
users.append(User(username='msadmin',password='aaa111'))
users2 = [User('msadmin','123456'),User('msadmin','123456')]

# 公共路径配置
config = {
         'test':{
                    "homework":"http://192.168.1.68:8083/HomeworkManagement",
                    "zeus":"http://192.168.1.67:8093/#/"
                 },
          'pre':{
                    "homework":"http://59.110.163.188/HomeworkManagement/",
                    "zeus":"http://192.168.1.67:9999/#/"
          },
          'wtk':{
                    "bom":"http://192.168.1.19:8080/BomManagement/",
                    "meal":"http://192.168.1.19:8801/meal/login"
          }
    }


def init_config(argv):
    '''
    根据脚本键入的提示找到服务器和模块
    :param argv: 键盘传入参数
    :return: 那个服务器,哪个模块
    '''
    env = 'test'
    mod = 'zeus'
    try:
        opts, args = getopt.getopt(argv,"e:m:",["environment=","module="])
    except getopt.GetoptError:
        print('02.py -e <environment> -m <module> ')
        print('\tenvironment: 运行环境 test,pre,run default test')
        print('\tmodule： 模块 homework zeus exam default zeus')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('02.py -e <environment> -m <module> ')
            print('\tenvironment: 运行环境 test,pre,run default test')
            print('\tmodule： 模块 homework zeus exam default zeus')
            sys.exit()
        elif opt == '-v':
            print('version: 1.0')
            os.system("pause")
            sys.exit()
        elif opt in ("-e", "--environment"):
            env = arg
        elif opt in ("-m", "--module"):
            mod = arg
    print('运行环境 ：', env)
    print('模块 ：', mod)
    return env,mod



def login_zeus(url=None,super_code=None):
    '''
    登录zeus 程序首页
    :return:
    '''
    print("now access %s" %(url))
    driver.get(url)
    driver.find_element_by_css_selector(".username > input").clear()
    driver.find_element_by_css_selector(".username > input").send_keys("msadmin")
    driver.find_element_by_css_selector(".passwd > input").clear()
    driver.find_element_by_css_selector(".passwd > input").send_keys("123456")

    if super_code == None:
        valid_code = input("please input the valid code: ")
    else:
        valid_code=super_code
        super_code = None
    driver.find_element_by_css_selector(".codes > input").clear()
    driver.find_element_by_css_selector(".codes > input").send_keys(valid_code)
    # driver.find_element_by_css_selector(".codes > input").send_keys(Keys.ENTER) #code码
    driver.find_element_by_tag_name("button").click()

    time.sleep(1) # 睡一秒
    try:
        tip = driver.find_element_by_css_selector(".forms > .errorInfo > .Tip")
        if tip != None:
            is_not_login = driver.find_element_by_css_selector(".forms > .errorInfo > .Tip").is_displayed();
            print("is_not_login",is_not_login)
            if is_not_login==True: #没有登录成功
                print(driver.find_element_by_css_selector(".forms > .errorInfo > .Tip").text)
                print("----login fail relogin!!! --------");
                login_zeus(url=url);
    except NoSuchElementException:
        print("login success")
    # driver.quit()

def login_homework(url=None,user = None):
    """
     请求登录
    :param url: 登录url
    :return:
    """
    print("now access %s, user: %s " %(url,user))
    driver.get(url)
    driver.find_element_by_id("btn").click()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(user.password)

    driver.find_element_by_id("submit").click()
    try:
        driver.find_element_by_id("username")
        #重新登录
        print('login fail!')
        return False
    except:
        print('login success')
        return True

def login_bom(url=None,user = None):
    """
     请求登录
    :param url: 登录url
    :return:
    """
    print("now access %s, user: %s " %(url,user))
    driver.get(url)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(user.password)
    driver.find_element_by_id("login_btn").click()
    return True

def login_meal(url=None,user = None):
    """
    请求登录
   :param url: 登录url
   :return:
   """
    print("now access %s, user: %s " %(url,user))
    driver.get(url)
    driver.find_element_by_id("userName").clear()
    driver.find_element_by_id("userName").send_keys(user.username)
    driver.find_element_by_id("passWord").clear()
    driver.find_element_by_id("passWord").send_keys(user.password)
    driver.find_element_by_id("passWord").send_keys(Keys.ENTER)
    #driver.find_element_by_css_selector("login_btn").click()
    return True


def move_question_manage():
    """
     题库管理
    :return:
    """
    # 定位到要悬停的元素
    above = driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/nav/ul/div/div/div[13]/li/div/span')

    # 对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(above).perform()
    #tag_mng = driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/nav/ul/div/div/div[13]/li/ul/li[1]/div')
    tag_mng = driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/nav/ul/div/div/div[5]/li')
    ActionChains(driver).click(tag_mng)
    print("点击了。。。")
    pass

if __name__ == '__main__':
    env,mod = init_config(sys.argv[1:])
    print(env,mod)
    if env not in ("test","pre","run",'wtk') and mod not in ('homework','zeus') :
        print("参数错误")
        sys.exit()


    #mod='homework'
    url = config[env][mod]
    print("url=",url)
    driver = webdriver.Chrome()
    if(mod=='zeus'):
        login_zeus(url=url,super_code='supervalid54321')#登录操作
    elif(mod=='homework'):
        flag = login_homework(url=url,user = User(username='msadmin',password='123456'))#登录操作
        if flag == False:
            time.sleep(1)
            login_homework(url=url,user = User(username='msadmin',password='aaa111'))
    elif(mod=='bom'):
        flag = login_bom(url=url,user = User(username='bomsys',password='dSqWul6B'))#登录操作
        if flag == False:
            time.sleep(1)
            login_bom(url=url,user = User(username='msadmin',password='aaa111'))
    elif(mod=='meal'):
        flag = login_meal(url=url,user = User(username='yingjing.liu',password='BarryLiu!'))#登录操作
        if flag == False:
            time.sleep(1)
            login_meal(url=url,user = User(username='yingjing.liu',password='BarryLiu!'))

