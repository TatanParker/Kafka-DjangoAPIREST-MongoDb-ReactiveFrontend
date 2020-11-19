from kafka import KafkaConsumer
from json import loads
from time import sleep
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client['pykafkadb']
collection = db['apikafka_colortrends']

consumer = KafkaConsumer(
    'colortrends',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
for message in consumer:
	print(message.value)
	print(collection.insert_one(message.value))
	# print (message)








# from kafka import KafkaConsumer
# from json import loads
# from time import sleep

# consumer = KafkaConsumer(
#     'topic_test',
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='my-group-id',
#     value_deserializer=lambda x: loads(x.decode('utf-8'))
# )

# for event in consumer:
#     event_data = event.value
#     # Do whatever you want
#     print(event_data)
#     sleep(2)
# from kafka import KafkaConsumer

# consumer = KafkaConsumer('colortrends',
#                          group_id='my-group',
#                          bootstrap_servers=['localhost:9092'])
# for message in consumer:
#     # message value and key are raw bytes -- decode if necessary!
#     # e.g., for unicode: `message.value.decode('utf-8')`
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value))