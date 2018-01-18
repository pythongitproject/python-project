#/usr/bin/env python3
#coding=utf-8

#发布
import pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type = 'fanout'
)
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
print(sys.argv[1:])

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print(" [x] Sent %r" % message)
connection.close()
