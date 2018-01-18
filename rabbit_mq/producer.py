#/usr/bin/env python3
#coding=utf-8

#生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
#durable   消息不丢失
# channel.queue_declare(queue='hello', durable=True)

try:
    channel.queue_declare(queue='hello', durable=True)
except:
    channel = connection.channel()
    channel.queue_delete(queue='hello')
    channel.queue_declare(queue='hello', durable=True)


channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='hello kugou',
    properties=pika.BasicProperties(
        delivery_mode=2   # make message persistent
    )
)
print('producer: sent hello world')
connection.close()