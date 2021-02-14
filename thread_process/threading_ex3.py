#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-02-14

import time
import threading

def run(n):
    print('这是线程{}。'.format(n))
    time.sleep(2)
    print('线程{}结束了。'.format(n))

start_time=time.time()


#  t_res=[]
for i in range(5):
    t=threading.Thread(target=run,args=(str(i)))

    t.setDaemon(True)

    t.start()
    #  t_res.append(t)

#  print('当前总的活跃线程数为：',threading.active_count())
#  for t in t_res:
#      t.join()


print(threading.current_thread())

print('程序消耗时间为：',time.time()-start_time)
