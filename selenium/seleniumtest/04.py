#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from PIL import Image,ImageEnhance
import pytesseract

"""
验证码识别
"""
def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login/login.png')  #截取登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgLocation = imgElement.location #获取验证码元素坐标
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    login = Image.open("login/login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('login/authcode.png')
    authcodeImg = Image.open('login/authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    return authCodeText

def pandarola_login(driver,account,passwd,authCode):
    '''登录pandarola系统'''
    driver.find_element_by_id('loginname').send_keys(account)
    driver.find_element_by_id('password').send_keys(passwd)
    driver.find_element_by_id('code').send_keys(authCode)
    driver.find_element_by_id('to-recover').click()
    time.sleep(2)
    title = driver.find_element_by_id('menuName-h').text  #获取登录的标题
    '''验证是否登录成功'''
    try:
        assert title == u'桌面'
        return '登录成功'
    except AssertionError as e:
        return '登录失败'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.67:8093/#/')
    imgElement = driver.find_element_by_id('updetpic')
    authCodeText = get_auth_code(driver,imgElement)
    pandarola_login(driver,'msadmin','123456',authCodeText)
    driver.quit()



def get_valid_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login/login.png')  #截取登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgLocation = imgElement.location #获取验证码元素坐标
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    login = Image.open("login/login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('login/authcode.png')
    authcodeImg = Image.open('login/authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    return authCodeText

if __name__ == '__main__2':
    imgUrl='http://192.168.1.68/console/captcha.jpg'
    code = get_valid_code(codeEelement=imgUrl)
    print(code)