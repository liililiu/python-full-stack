#!/usr/bin/python
# Author: liililiu
# Description:线程锁 
# Created Time: 2021-02-14

import time
import threading

def run(n):
    lock.acquire()
    global num
    for i in range(1000000):
        num+=1
    print('子线程{}越算结束后，num值为{}.'.format(threading.current_thread().getName(),num))
    lock.release()


lock=threading.Lock()
num=0
t_res=[]
for i in range(3):
    t=threading.Thread(target=run,args=(str(i),))
    t.start()
    t_res.append(t)

    #  t.join()

for t in t_res:
    t.join()



print('主线程结束后num为：',num)
