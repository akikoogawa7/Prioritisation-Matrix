from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, NamedTuple, List, Dict
from datetime import datetime
# from utils import compute_inputs_json, check_threshold_against_groups_size
from errors import XYValueError

class UserData(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

class MatrixInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    time_created: datetime = Field(default_factory=datetime.utcnow)
    author: UserData
    problem_name: str 
    problem_description: Optional[str] = None

class XYInputs(NamedTuple):
    x_label: str
    y_label: str

class UserElementInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_element_name: str 
    time_created: datetime = Field(default_factory=datetime.utcnow)

class UserElementValues(BaseModel):
    element: UserElementInputs
    x_value: float
    y_value: float

    # Checks if x and y values are not more than 100
    @validator('x_value', 'y_value')
    @classmethod
    def must_be_less_than_100(cls, value):
        if value > 100.0:
            raise XYValueError(value=value, message='Value should not be more than 100.0')
        return value
    
class UserElementList(BaseModel):
    __root__: List[UserElementInputs] # change to Element list

class UserMetadata(BaseModel):
    user: UserData
    # matrix: MatrixInputs depends on whether user is creating matrix or only voting
    labels: XYInputs
    element_inputs: UserElementInputs
    element_values: UserElementValues
    tasks_list: UserElementList



user = UserData() # include user data

t1 = UserElementInputs(user_element_name='Do A')
t2 = UserElementInputs(user_element_name='Do B')

list_of_tasks = [t1, t2]

print(f'Task 1: {t1.task_name}\nTask 2: {t2.task_name}')

user_1 = UserMetadata(
    user=user,
    labels=XYInputs('Importance', 'Effort'), 
    element_inputs=UserElementInputs(user_element_name='Do x'),
    element_values=UserElementValues(x_value=50.0, y_value=40.0),
    tasks_list=list_of_tasks)

print(f'\nLABELS: {user_1.labels}\n\nMETADATA: {user_1.metadata}\n\nTASKS: {user_1.tasks_list}\n\n')