#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-10

import socket,time

server=socket.socket()

server.bind(('localhost',4444))#绑定端口,注意元组形式

server.listen(8) #listen
print('已建立监听，等待连接')

while True:
    conn,addr=server.accept()# 若有连接进入，为其生成实例
    print('new connection:',addr)
    while True:
    
        data=conn.recv(1024) #recv默认阻塞
        if not data:#判断空数据，客户端断开发送为空，避免死循环
            break
        conn.send(data.decode().upper().encode('utf-8'))
        #  time.sleep(2)
        print('客户端请求数据已返回')

server.close()
