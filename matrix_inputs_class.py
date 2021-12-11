from os import CLD_CONTINUED
import pandas as pd
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, NamedTuple, List, Dict
from datetime import datetime
from utils import compute_inputs_json, check_threshold_against_groups_size
from errors import XYValueError

class MatrixInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    author: str
    project_name: str 
    project_description: Optional[str] = None
    time_created: datetime = Field(default_factory=datetime.utcnow)

class XYInputs(NamedTuple):
    x_label: str
    y_label: str

class TasksInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    task: str
    time_created: datetime = Field(default_factory=datetime.utcnow)
    x_value: float
    y_value: float

    # Checks if x and y values are not more than 100
    @validator('x_value', 'y_value')
    @classmethod
    def must_be_less_than_100(cls, value):
        if value > 100.0:
            raise XYValueError(value=value, message='Value should not be more than 100.0')
        return value
    
class UserItemInputs(BaseModel):
    # list_of_tasks: List[TasksInputs] = None
    labels: XYInputs
    metadata: TasksInputs
    

user_1 = UserItemInputs(labels=XYInputs('Importance', 'Effort'), metadata=TasksInputs(task='Do x', x_value=101.0, y_value=10.0))

print(f'LABELS: {user_1.labels}, METADATA: {user_1.metadata}')
