import requests

requests.utils.add_dict_to_cookiejar()

html = requests.get("http://www.itaren.com")
print(html.content)
print(html.history)
print(html.cookies)
print(html.content.title())
print(html.encoding)
print(html.headers)
print(html.elapsed)
print(html.links)
print(html.links)
print(html.close())