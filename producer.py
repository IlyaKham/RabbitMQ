#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials("admin", "admin123")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.107', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
