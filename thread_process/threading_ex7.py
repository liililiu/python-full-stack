#!/usr/bin/python
# Author: liililiu
# Description:  event--红绿灯
# Created Time: 2021-02-16

import threading,time

event=threading.Event()

def lighter():
    num=0
    while True:
        if num<3:
            event.clear()
            print('红灯中---------------------')
        elif num<6:
            event.set()
            print('绿灯中---------------------')
        else:
            num=-1
        time.sleep(2)
        num+=1

def car(name):
    while True:
        if event.is_set():
            print('{}正在行驶中。。'.format(name))
            time.sleep(3)
        else:
            print('{}正在等绿灯中。。'.format(name))
            event.wait()

light=threading.Thread(target=lighter,)
car1=threading.Thread(target=car,args=(('新能源小汽车',)))
light.start()
car1.start()



