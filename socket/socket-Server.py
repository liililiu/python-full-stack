#!/usr/bin/python
# Author: liililiu
# Description: Threading
# Created Time: 2021-02-12

import socketserver

print('已建立监听：')
#继承socketserver的BaseRequestHandler类
class MyTcpHandler(socketserver.BaseRequestHandler):

    #重写handle方法,与客户端所有的交互都是在handle里完成的
    def handle(self):
        while True:
            
            self.data=self.request.recv(1024).strip() #实例化连接
            if not self.data:
                print('{}已断开连接'.format(self.client_address[0]))
                break
            print("{}已连接".format(self.client_address[0]),end=' ')
            print('输入数据为：',self.data)

            self.request.sendall(self.data.upper())

if __name__=='__main__':
    HOST,PORT='localhost',3344
    #实例化server
    server=socketserver.ForkingTCPServer((HOST,PORT),MyTcpHandler)
    #  server=socketserver.ThreadingTCPServer((HOST,PORT),MyTcpHandler)
    #server一直在监听
    server.serve_forever()
