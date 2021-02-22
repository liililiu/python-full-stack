#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-22

import gevent
def f1():
    print('in the f1')
    gevent.sleep(2)  ##模拟io操作
    #  pass
    print('in the f1,again')



def f2():
    print('in the f2')
    gevent.sleep(1)
    print('in the f2,again')
    #  pass


gevent.joinall([gevent.spawn(f1),gevent.spawn(f2)])
