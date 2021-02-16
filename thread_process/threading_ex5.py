#!/usr/bin/python
# Author: liililiu
# Description:线程锁-------------------递归锁
# Created Time: 2021-02-14

import time
import threading

def run1():
    lock.acquire()
    global num
    num+=1
    lock.release()
    return num

def run2():
    lock.acquire()
    global num2
    num2+=1
    lock.release()
    return num2



def run3():
    lock.acquire()
    res=run1()
    print('-------between run1 and run2---------')
    res2=run2()
    lock.release()
    print(res,res2)


num,num2=0,0
lock=threading.RLock()
for i in range(5):
    t=threading.Thread(target=run3)
    t.start()
while threading.active_count() !=1:
    #  print('当前活跃线程数： ',threading.active_count())
    print(' ')

else:
    print('所有子线程都已结束，num和num2的值为：{},{} '.format(num,num2))
