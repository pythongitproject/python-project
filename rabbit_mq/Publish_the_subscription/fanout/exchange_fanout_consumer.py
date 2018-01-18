#/usr/bin/env python3
#coding=utf-8

#订阅
import pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)
#一个新的空的queue，将exclusive置为True，这样在consumer从RabbitMQ断开后会删除该queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
