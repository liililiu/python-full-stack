#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-23

import gevent

from gevent import socket,monkey ###gevent下的socket方法

monkey.patch_all()

def server(port):
    s=socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(100)

    while True:
        cli,addr=s.accept()
        print('{}已连接'.format(cli))
        gevent.spawn(handle,cli)
    #  pass


def handle(conn):
    try:
        while True:
            data=conn.recv(1024)
            if not data:
                print('{}已退出'.format(conn))
                break
            print('recv:',data)
            conn.send(data)
        #  pass
    except Exception as e:
        print(e)
         #  ccpass
    finally:
        conn.close()
    #  pass

if __name__=='__main__':

    server(6789)





