from time import sleep
from json import dumps
from kafka import KafkaProducer


bootstrap_servers = ['localhost:9092']
topic = 'colortrends'

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send(topic, value=data)
    sleep(0.5)


# producer.send(topic, b'Hello World!')
# producer.flush()