from selenium import webdriver
import requests

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

driver.get_screenshot_as_png()

