import pika
import json
import config as cfg

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare queue to send data
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

data = {
        "id": 1,
        "name": "My Name",
        "description": "This is description about me"
    }
message = json.dumps(data)

# Send data
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] Sent data to RabbitMQ")
connection.close()
