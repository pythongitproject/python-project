#/usr/bin/env python3
#coding=utf-8

#消费者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',no_ack=True
                      )
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
