import pulsar
from pulsar.schema import JsonSchema
from schemas import ExampleSchema
from pulsar.schema import StringSchema
from time import sleep

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    'my-topic-str', 
    subscription_name='my-sub', 
    schema=StringSchema(),
    unacked_messages_timeout_ms=10000,
    negative_ack_redelivery_delay_ms=3000
)
i = 0
while True:
    msg = consumer.receive()
    data = msg.value()
    print(f"Received message: {data}, Redelivery Count: {msg.redelivery_count()}")
    if i == 0:
        sleep(11)
    if i % 2 == 0:
        consumer.negative_acknowledge(msg)
    else:
        consumer.negative_acknowledge(msg)
    i += 1

client.close()
