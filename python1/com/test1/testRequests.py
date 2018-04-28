import requests
from socket import *

f = requests.get("http://www.baidu.com");
#print(f.url)
#print(f.content)


myhost=''
myport = '8084'

sockobj=socket(AF_INET,SOCK_STREAM)

print(sockobj)

sockobj.bind(myhost,myport)

sockobj.listen(128)

while True:
	connection,address = sockobj.accept()
	print ("connect by ",address)
	data=connection.recv(1024)
	connection.send('echo:' +data)

	pass
