#/usr/bin/env python3
#coding=utf-8

#生产者
import pika
#远程连接rabbitmq server
# credentials = pika.PlainCredentials("alex","123")
# connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.14.47',credentials=credentials))
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