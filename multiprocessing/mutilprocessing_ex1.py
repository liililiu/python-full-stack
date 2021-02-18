#!/usr/bin/python
# Author: liililiu
# Description: 多进程
# Created Time: 2021-02-17

import multiprocessing,time
import threading,os

def run(name):
    print('hello,{},这是子进程。'.format(name))
    print('当前进程的进程ID：',os.getpid())
    print('当前进程的父进程ID：',os.getppid())



def run1(name):
    print('hello, ',name)
    print('当前进程的进程ID：',os.getpid())
    print('当前进程的父进程ID：',os.getppid())
    print('-------------------------------------------')

    p=multiprocessing.Process(target=run,args=('liu',))
    p.start()

if __name__=='__main__':
    print('当前进程的进程ID：',os.getpid())
    print('当前进程的父进程ID：',os.getppid())
    print('-------------------------------------------')
    run1('zhangsan')


