# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("http://www.itaren.com")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"图片").click()
        driver.find_element_by_xpath("//img[contains(@src,'http://img3.imgtn.bdimg.com/it/u=3011882837,206644498&fm=27&gp=0.jpg')]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


#
# from selenium import webdriver
# import os
# #引入chromedriver.exe
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
#
# #设置浏览器需要打开的url
# url = "http://www.baidu.com"
# browser.get(url)
#
# #在百度搜索框中输入关键字"python"
# browser.find_element_by_id("kw").send_keys("python")
# #单击搜索按钮
# browser.find_element_by_id("su").click()
#
# #关闭浏览器
# #browser.quit()
