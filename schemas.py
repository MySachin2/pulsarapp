
from dataclasses import dataclass
from pulsar.schema import Record
from pydantic import BaseModel


class ExampleSchema(BaseModel):
    action_type: str
    message_id: str