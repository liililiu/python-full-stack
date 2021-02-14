#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-10

import socket,time

client=socket.socket() #声明类型，同时生成socket连接对象

#  print(client)
client.connect(('localhost',3344))
print('已建立连接')
#  time.sleep(2)

while True:
    data=input('>>:').strip()
    if len(data)==0: continue

    client.send(data.encode('utf-8'))
    #  print('请求已发送等待响应')
    
    #  time.sleep(5)
    data=client.recv(1024)
    print('已获取到响应内容: ',data.decode())

client.close()

