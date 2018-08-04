from bs4 import  BeautifulSoup
import requests
# from urllib import request

# response = request.urlopen('http://itaren.com').read().decode('utf-8');
# print(html.content)
# response.encoding = "utf-8"

response = requests.get('http://itaren.com')
soup = BeautifulSoup(response,'html.parser')


print(soup.prettify('utf-8'))
