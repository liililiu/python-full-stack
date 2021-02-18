#!/usr/bin/python
# Author: liililiu
# Description: 进程池
# Created Time: 2021-02-17


import os,multiprocessing,time

def Foo(i):
    time.sleep(1)
    print('当前在{}号进程中'.format(os.getpid()))
    return 100+i
    #  print(100+i)

def Bar(args):                       #####回调
    print('执行完毕。 ',args,os.getpid())

if __name__=='__main__':
    pool=multiprocessing.Pool(3) ##允许进程池同时放入3个进程
    print('--------------------------------------')
    print('主进程的进程ID： ',os.getpid())

    for i in range(10):
        #  pool.apply(func=Foo,args=(i,))          #串行
        #  pool.apply_async(func=Foo,args=(i,))      #并行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)    # 回调函数

    print('--------------------------------------')

    pool.close()
    pool.join()



    
