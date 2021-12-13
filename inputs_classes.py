from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, NamedTuple, List, Dict
from datetime import datetime
# from utils import compute_inputs_json, check_threshold_against_groups_size
from errors import XYValueError
import pprint

class UserData(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str

    @validator('confirm_password')
    @classmethod
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    @classmethod
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

# Question and Problem element (created by Admin)
class UserElementName(BaseModel):
    user_element_name: str

class MatrixInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    time_created: datetime = Field(default_factory=datetime.utcnow)
    author: UserData
    project_name: str 
    project_description: Optional[str] = None
    problem_title: UserElementName

# XY Variables and Polarity (created by Admin)
class XYInputs(NamedTuple):
    x_label: str
    x_polarity: bool # If True, x is positive, if False, x is negative
    y_label: str
    y_polarity: bool # If True, y is positive, if False, y is negative

    # XY 4 quadrants of preferrability classification
    # A - Negative X Positive Y
    # B - Positive X Positive y
    # C - Negative X Negative Y
    # D - Positive X Negative Y 
    
    @validator('x_polarity', 'y_polarity')
    @classmethod
    def negative_x_positive_y(cls, x, y):
        if x == False and y == True:
            A = 'Preferrable quadrant'
            return A
        elif x == True and y == True:
            B = 'Preferrable quadrant'
            return B
        elif x == False and y == False:
            C = 'Preferrable quadrant'
            return C
        else:
            D = 'Preferrable quadrant'
            return D


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


# Test data
pp = pprint.PrettyPrinter(indent=4)

user = UserData(
    first_name='A',
    last_name='O',
    username='AO97',
    password='password',
    confirm_password='password'
)

t1 = UserElementInputs(user_element_name='Do A')
t2 = UserElementInputs(user_element_name='Do B')

element_inputs = UserElementInputs(user_element_name='Do x')

list_of_tasks = [t1, t2]

pp.pprint(f'Task 1: {t1.user_element_name}  Task 2: {t2.user_element_name}')

user_1 = UserMetadata(
    user=user,
    labels=XYInputs('Importance', 'Effort'), 
    element_inputs=element_inputs,
    element_values=UserElementValues(element=element_inputs, x_value=50.0, y_value=40.0),
    tasks_list=list_of_tasks)

print(f'\nLABELS: {user_1.labels}\n\nMETADATA: {user_1.element_inputs}\nVALUES: {user_1.element_values}\n\nTASKS: {user_1.tasks_list}\n\n')