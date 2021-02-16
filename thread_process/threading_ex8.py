#!/usr/bin/python
# Author: liililiu
# Description:  队列-生产者消费者模型
# Created Time: 2021-02-16


import queue,threading,time

q=queue.Queue(maxsize=10)

def producer():
    num=1
    while True:
        q.put(num)
        print('第{}个馒头做好了！'.format(num))
        num+=1
        time.sleep(0.25)


def consumer():
    while True:
        print('小明同学吃了第个{}包子'.format(q.get()))
        time.sleep(0.7)



p=threading.Thread(target=producer,args=())
c=threading.Thread(target=consumer,args=())
p.start()
c.start()
