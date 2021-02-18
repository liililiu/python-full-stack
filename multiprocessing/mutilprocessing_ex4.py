#!/usr/bin/python
# Author: liililiu
# Description:  进程通信---管道
# Created Time: 2021-02-17

from multiprocessing import Pipe,Process


def f(conn):
    conn.send([111,'aaa'])

    print(conn.recv())

    conn.close()




if __name__=='__main__':
    conn_1,conn_2=Pipe()
    p=Process(target=f,args=(conn_1,))

    p.start()
    print(conn_2.recv())
    conn_2.send('来自管道2')

    p.join()
    
