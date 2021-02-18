#!/usr/bin/python
# Author: liililiu
# Description:  进程间通信
# Created Time: 2021-02-17


import multiprocessing 

def f(q):
    q.put([111,'aaa'])

if __name__=='__main__':
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=f,args=(q,))

    p.start()

    print(q.get())
    
