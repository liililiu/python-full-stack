#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-03-01

import pika

conn=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.99.107',port=5672,credentials=pika.PlainCredentials(username='guest',password='guest')))
channel=conn.channel()

channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print(" [x] Received %r" % body)
    #  print('收到消息：',body)

channel.basic_consume(callback,queue='hello')

channel.start_consuming()
