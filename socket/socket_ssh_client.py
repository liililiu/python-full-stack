#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-11

import socket,os,time

client=socket.socket()
client.connect(('localhost',3332))

while True:
    data=input('>>:').strip()
    if len(data)==0: continue
    client.send(data.encode('utf-8'))
    
    cmd_size=client.recv(1024)   #执行命令结果的长度
    #  print('cmd执行后大小：',cmd_size.decode())
    data_recv=b''
    total_size=0
    while total_size<int(cmd_size.decode()):
        data_dan=client.recv(1024)
        #  data.recv+=client.recv(1024)
        total_size+=len(data_dan)
        data_recv+=data_dan
    print(data_recv.decode())
    


    

