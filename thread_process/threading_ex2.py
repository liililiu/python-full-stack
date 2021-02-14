#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-14

#关于继承式写法

import time,threading

class Mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print('这是线程{}。'.format(self.name))
        time.sleep(2) 

if __name__=='__main__':

    t1=Mythread(1)
    t2=Mythread(2)

    t1.start()
    t2.start()
