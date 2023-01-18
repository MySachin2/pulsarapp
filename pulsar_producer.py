import uuid
import pulsar
from pulsar.schema import StringSchema

from schemas import ExampleSchema

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic-str', schema=StringSchema())

for i in range(10):
    sch = ExampleSchema(
        action_type='headbang',
        message_id=str(uuid.uuid4())
    )
    producer.send(sch.json())

client.close()