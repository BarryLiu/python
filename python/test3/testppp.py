#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas
import time
newarry = []
user_agent = '*******'
headers = {'User_Agent': user_agent}
for i in range(15):
    gradeUrl = 'https://movie.douban.com/celebrity/1274297/partners?start='+str(i*10)
    res = requests.get(gradeUrl, headers)
    soup = BeautifulSoup(res.content, 'html.parser').find(class_='article')
    for item in soup.find_all(class_='partners item'):
        partner = item.select('a')[1].text
        times = item.select('li')[1].text
        collect_num = item.select('li')[2].text
        url_list = item.select('li')[1]
        for url in url_list.find_all('a'):
            each_page = requests.get(url.get('href'), headers)
            sub_res = BeautifulSoup(each_page.content, 'html.parser')
            info = sub_res.find(id='wrapper')
            movie_name = info.select('span[property="v:itemreviewed"]')[0].text
            print(movie_name)
            director = info.find(class_='attrs').select('a')[0].text
            types = ' '.join([style.text for style in info.select('span[property="v:genre"]')])
            if info.find(class_='ll rating_num') is None:
                 rate = 0
            else:
                rate = info.find(class_='ll rating_num').text
            newarry.append({
                'partner': partner.split(" ")[0],
                'time': times[5],
                'collect_num': collect_num,
                'movie_name': movie_name,
                'director': director,
                'types': types,
                'rating': rate
            })
        time.sleep(2)
    print(newarry)

new_df = pandas.DataFrame(newarry, columns=['partner', 'time', 'collect_num', 'movie_name', 'director', 'types', 'rating'])
new_df.to_excel('D:partner.xlsx')
print(new_df)