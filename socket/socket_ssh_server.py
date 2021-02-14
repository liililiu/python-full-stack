#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-10

import socket,os,time

server=socket.socket()
server.bind(('localhost',3332))
server.listen()

while True:
    conn,addr=server.accept() 
    print('新的连接已建立!')
    while True:
        data=conn.recv(8192)#byte类型
        if len(data)==0:
            print('连接断开!')
            break
        cmd=os.popen(data.decode()).read() #读取转化后的str类型返回str
        if len(cmd)==0:
            cmd='cmd has no output!'
        conn.send(str(len(cmd.encode('utf-8'))).encode('utf-8')) 
        time.sleep(1)
        conn.send(cmd.encode('utf-8'))


