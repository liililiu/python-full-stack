#!/usr/bin/python
# Author: liililiu
# Description:进程共享数据-------manager
# Created Time: 2021-02-17

import os
from multiprocessing import Manager,Process

def f(l):
    l.append(os.getpid())

if __name__=='__main__':
    with Manager() as manager:
        l=manager.list()
        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(l,))
            p.start()
            p_list.append(p)
        for t in p_list:
            t.join()

        print(l)

