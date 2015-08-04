import pika
import json
import config as cfg

#RABBIT_HOST = '192.168.100.191'
#QUEUE = 'topic_name'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

channel.queue_declare(queue=cfg.QUEUE_TOPIC)

data = {
        "id": 1,
        "name": "My Name",
        "description": "This is description about me"
    }
message = json.dumps(data)
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] Sent data to RabbitMQ")
connection.close()
