#/usr/bin/env python3
#coding=utf-8

#生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='hello kugou'
)
print('producer: sent hello world')
connection.close()