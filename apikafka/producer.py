from kafka import KafkaProducer
from json import dumps


producer = KafkaProducer(
	bootstrap_servers = ['localhost:9092'],
	value_serializer = lambda x:dumps(x).encode('utf-8')
	)

def kafka_send(topic, name, color):
    data = {
        'name' : name,
        'color' : color
    }
    producer.send(topic, data)

