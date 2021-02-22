#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-22

import greenlet

def f1():
    print('12')
    b.switch()
    print('34')
    b.switch()
    #  pass

def f2():
    print('56')
    a.switch()
    print('78')
    #  pass

a=greenlet.greenlet(f1)
b=greenlet.greenlet(f2)
a.switch()
