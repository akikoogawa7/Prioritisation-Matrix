from uuid import UUID, uuid4
from pydantic import BaseModel, Field, validator, EmailStr, validate_email
from typing import Optional, NamedTuple, List
from datetime import datetime
from pydantic.networks import EmailStr
from sqlalchemy.sql.schema import ForeignKey
from errors import XYValueError
import pprint
from utils import quadrant_classifier_label, quadrant_classifier_for_values

class UserData(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    fullname: Optional[str] = None
    # email: str
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

    class Config:
        allow_mutation = False

class UserDataOut(BaseModel):
    fullname: Optional[str] = None
    email: str
    username: str


# Question and Problem element (created by Admin)

class MatrixInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    time_created: datetime = Field(default_factory=datetime.utcnow)
    author: UserData

# XY Variables and Polarity (created by Admin)
class XYInputLabel(NamedTuple):
    x_label: str
    y_label: str

# Polarities for preference
class XYInputPolarity(BaseModel):
    x_polarity: bool
    y_polarity: bool
    
class UserElementInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    time_created: datetime = Field(default_factory=datetime.utcnow)

class UserElementValues(BaseModel):
    element: UserElementInputs
    x_value: float
    y_value: float
    # output: quadrant_classifier_for_values(x_value, y_value)

    # Checks if x and y values are not more than 100
    @validator('x_value', 'y_value')
    @classmethod
    def must_be_less_than_100(cls, value):
        if value > 100.0:
            raise XYValueError(value=value, message='Value should not be more than 100.0')
        return value
    
class UserElementList(BaseModel):
    __root__: List[UserElementInputs]

class MatrixOutputMetadata(BaseModel):
    user: UserData
    labels: XYInputLabel
    polarity: XYInputPolarity
    element_inputs: UserElementInputs
    element_values: UserElementValues
    element_list: UserElementList
    quadrant_class: str

    class Config:
        allow_mutation = False

if __name__ == '__main__':

    user = UserData(
        first_name='A',
        last_name='O',
        username='AO97',
        password='password',
        confirm_password='password'
    )

    # XY Labels 
    labels = XYInputLabel(x_label='Importance', y_label='Effort')

    # Elements created

    e1 = UserElementInputs(user_element_name='Do A')
    e2 = UserElementInputs(user_element_name='Do B')

    list_of_tasks = [e1, e2]

    x_polarity = True
    y_polarity = False

    x_value = 50.0
    y_value = 40.0

    element_values = UserElementValues(element=e1, x_value=x_value, y_value=y_value)

    polarity = XYInputPolarity(x_polarity=x_polarity, y_polarity=y_polarity)

    quadrant_class = quadrant_classifier_label(x_polarity=x_polarity, y_polarity=y_polarity)
    x, y, output_class = quadrant_classifier_for_values(x_value, y_value)

    matrix = MatrixOutputMetadata(
        user=user,
        labels=labels, 
        polarity=polarity,
        element_inputs=e1,
        element_list=list_of_tasks,
        element_values=element_values,
        quadrant_class=quadrant_class
        )

    # print(f'\nLABELS: {matrix.labels}\n\nELEMENT INPUT: {matrix.element_inputs}\n\nELEMENT VALUE: {matrix.element_values}\n\nELEMENTS: {matrix.element_list}\n\nPREFERRED CLASS: {matrix.quadrant_class}')

    # print(f'x: {x}\t y: {y}\nOUTPUT CLASS: {output_class}')