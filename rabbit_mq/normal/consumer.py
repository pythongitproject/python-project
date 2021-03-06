#/usr/bin/env python3
#coding=utf-8

#消费者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
# make message persistent
# channel.queue_declare(queue='hello',durable=True)

try:
    channel.queue_declare(queue='hello', durable=True)
except:
    channel = connection.channel()
    channel.queue_delete(queue='hello')
    channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print("Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

#表示谁来谁取，不再按照奇偶数排列
# channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False
                      )
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
