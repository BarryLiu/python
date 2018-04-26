import requests
from bs4 import BeautifulSoup

# def saveImg(self,url,dirpat,filename):
#     # urlFile = requests.get(url)
#     # f = open(filename,'wb')
#     # for c in urlFile.iter_content(10000):
#     #     f.write(c)
#     # f.close()
#     # print('--------下载完成---------')
#     # pass
#     print('hellooooo',url,dirpat,filename)

def saveImg(url,fileName):
    r = requests.get(url)
    with open(fileName, "wb") as code:
        code.write(r.content)

# html = requests.get('http://itaren.com')
html = requests.get('http://www.mmjpg.com/')

# print(html.content)

soup = BeautifulSoup(html.content,"html.parser")
print(soup.prettify())
print('---------分割线--------')
# print(soup.findAll('img'))
imgs = soup.findAll('img')
for img in imgs:
    img_url=img.get('src')

    print('下载',img_url,img_url.split('/')[-1])
    saveImg(img_url,'img/'+img_url.split('/')[-1])


print('--------测试下载--------')
# saveImg('http://img.mmjpg.com/2018/1329/1i8a.jpg','img/abc.png')