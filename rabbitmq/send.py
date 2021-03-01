#!/usr/bin/python
# Author: liililiu
# Description: 
# Created Time: 2021-03-01

import pika

conn=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.99.107',port=5672,credentials=pika.PlainCredentials(username='guest',password='guest'))) ## 建立连接，建立一个socket
channel=conn.channel() ##获得channel


channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')

conn.close()



