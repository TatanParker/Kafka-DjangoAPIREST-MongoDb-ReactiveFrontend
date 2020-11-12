from kafka import KafkaProducer, KafkaConsumer
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


def kafka_consumer(topic):

	consumer = KafkaConsumer(
		topic,
		bootstrap_servers = ['localhost:9092'],
		auto_offset_reset='earliest',
		enable_auto_commit=True,
		group_id = 'colors'
		)

	for message in consumer:
		print(message.value)



consumer = KafkaConsumer(
		'color',
		bootstrap_servers = ['localhost:9092'],
		auto_offset_reset='earliest',
		enable_auto_commit=True,
		group_id = 'colors'
		)
