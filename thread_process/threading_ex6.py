#!/usr/bin/python
# Author: liililiu
# Description: 线程----------信号量
# Created Time: 2021-02-16
import threading
import time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('线程：',n)
    semaphore.release()


    
if __name__=='__main__':
    semaphore=threading.BoundedSemaphore(5)
    for i in range(23):
        t=threading.Thread(target=run,args=(i,))
        t.start()





