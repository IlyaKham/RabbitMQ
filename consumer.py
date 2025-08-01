#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials("admin", "admin123")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.107', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
