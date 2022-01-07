# 前置步骤 pip install captcha  
#         pip install selenium  
#         下载安装chrome 浏览器以及浏览器对应的驱动文件

purpose = 'ADULT'               #购买成人票，不支持学生票
names = ['李时禹']              #填写购票人姓名
date = '2022-01-20'             #填写购票日期
start_station = '广州'          #购票出发站
end_station = '孝感东'          #购票目的站
password = '******'        #登录12306的秘密
username ='2385467836@qq.com'   #登录12306的账号
trains = ['G1172', 'G554','G552', 'G546', 'G696']  #你想买的班次


# ---------------代码部分-----------
import json
import time
from captcha import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC




options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  
browser = webdriver.Chrome(options=options)
browser.maximize_window()
login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
#ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
browser.get(login_url)
time.sleep(5)
# wait.WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,'login-hd-account'))).click()
input_name = browser.find_element_by_id('J-userName')
input_pd = browser.find_element_by_id('J-password')
input_name.send_keys(username)
input_pd.send_keys(password)
login = browser.find_element_by_id('J-login')
login.click()


browser.implicitly_wait(5)
print('=====开始处理滑动验证码=====')
track = [300, 400, 500]  
for i in track:
    try:
        btn = browser.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
        ActionChains(browser).drag_and_drop_by_offset(btn,i,0).perform()
    except:
        time.sleep(2)  
#拉动滑块验证
browser.implicitly_wait(1)
wait.WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary'))).click()


browser.find_element_by_xpath('//*[@id="J-chepiao"]/a').click()
browser.find_element_by_xpath('//*[@id="megamenu-3"]/div[1]/ul/li[1]/a').click()
browser.find_element_by_xpath('//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()
#选票
def input_info():
    print('=====选票=====')
    from_station = browser.find_element_by_xpath('//*[@id="fromStationText"]')
    from_station.send_keys(Keys.ENTER)
    from_station.send_keys(Keys.CONTROL, 'a')
    from_station.send_keys(start_station, Keys.ENTER)
    browser.implicitly_wait(5)
    to_station = browser.find_element_by_xpath('//*[@id="toStationText"]')
    to_station.send_keys(Keys.ENTER)
    to_station.send_keys(Keys.CONTROL, 'a')
    to_station.send_keys(end_station, Keys.ENTER)
    browser.implicitly_wait(5)
    start_date = browser.find_element_by_xpath('//*[@id="train_date"]')
    start_date.send_keys(Keys.ENTER)
    start_date.send_keys(Keys.CONTROL, 'a')
    start_date.send_keys(Keys.CONTROL, 'x')
    start_date.send_keys(date, Keys.ENTER)
    browser.implicitly_wait(5)
    wait.WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID,'query_ticket'))).click()
input_info()
input_info()
browser.implicitly_wait(2)
noorder = True
while(noorder) :
    input_info()
    browser.implicitly_wait(2)
    trList = browser.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
    for tr in trList:
        trainNum = tr.find_element_by_class_name("number").text
        # print('车次',trainNum)
        if trainNum in trains:
            leftTicket = tr.find_element_by_xpath(".//td[4]").text
            print('leftTicket', leftTicket,trainNum)
            if leftTicket == '有' or leftTicket.isdigit():
                orderBtn = tr.find_element_by_class_name("btn72")
                orderBtn.click()
                browser.implicitly_wait(5)
                passengerLabels = browser.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")
                for passengerLabel in passengerLabels: 
                    name = passengerLabel.text
                    if name in names: 
                        passengerLabel.click() 
                        print('=====开始买票=====')
                browser.implicitly_wait(2)
                # 获取提交按钮
                submitBtn = browser.find_element_by_id("submitOrder_id")
                submitBtn.click()
                browser.implicitly_wait(2)
                confirmBtn = browser.find_element_by_id("qr_submit_id")
                confirmBtn.click()
                time.sleep(2)
                browser.implicitly_wait(2)
                confirmBtn = browser.find_element_by_id("qr_submit_id")
                confirmBtn.click()
                noorder = False
                break



