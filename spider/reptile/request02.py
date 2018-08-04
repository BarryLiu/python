from json import JSONDecodeError

import requests
from  requests import help

html = requests.get("http://www.itaren.com")
try:
    json = html.json()
    print('成功转为json数据:'+json)
except JSONDecodeError as e:
    print("转换成json失败")





print(help.info())
print(help.main())

requests.__version__='2.2.2'
print(requests.__version__)
print(requests.__author__)

range(10)

