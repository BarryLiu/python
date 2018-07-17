from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def login():
    '''
    登录程序首页
    :return:
    '''
    first_url= 'http://demo.open.renren.io/renren-security/login.html'
    first_url="http://192.168.1.67:8093/#/"
    print("now access %s" %(first_url))
    driver.get(first_url)
    driver.find_element_by_css_selector(".username > input").clear()
    driver.find_element_by_css_selector(".username > input").send_keys("msadmin")
    driver.find_element_by_css_selector(".passwd > input").clear()
    driver.find_element_by_css_selector(".passwd > input").send_keys("123456")

    valid_code = input("please input the valid code: ")
    driver.find_element_by_css_selector(".codes > input").send_keys(valid_code)
    # driver.find_element_by_css_selector(".codes > input").send_keys(Keys.ENTER) #code码
    driver.find_element_by_tag_name("button").click()

    time.sleep(1) # 睡一秒
    try:
        tip = driver.find_element_by_css_selector(".forms > .errorInfo > .Tip")
        if tip != None:
            is_login = driver.find_element_by_css_selector(".forms > .errorInfo > .Tip").is_displayed();
            print("is_login",is_login)
            if is_login==True: #没有登录成功
                print(driver.find_element_by_css_selector(".forms > .errorInfo > .Tip").text)
                print("----login fail relogin!!! --------");
                login();
    except NoSuchElementException:
        print("login success")
    # driver.quit()

def move_question_manage():
    """
     题库管理
    :return:
    """
    # 定位到要悬停的元素
    above =None
    enums = driver.find_elements_by_class_name(".el-submenu__title > .el-icon-zoom-in > .timehide")
    print(enums)

    # 对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(above).perform()

    pass
if __name__ =="__main__":
    login()#登录操作
    move_question_manage()


