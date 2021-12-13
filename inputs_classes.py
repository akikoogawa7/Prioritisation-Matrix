from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ValidationError, validator, validate_arguments, constr
from typing import Optional, NamedTuple, List, Dict
from datetime import datetime
# from utils import compute_inputs_json, check_threshold_against_groups_size
from errors import XYValueError
import pprint
from utils import quadrant_classifier_label, quadrant_classifier_for_values

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
class XYInputLabel(NamedTuple):
    # Label
    x_label: str
    y_label: str

class XYInputPolarity(BaseModel):
    x_polarity: bool
    y_polarity: bool

# Polarities for preference
@validate_arguments
def quadrant_classifier_label(x_polarity, y_polarity):

    """4 quadrants of preferrability classification defined based on X and Y polarity"""

    # A - Negative X Positive Y
    # B - Positive X Positive y
    # C - Negative X Negative Y
    # D - Positive X Negative Y 

    # If True, x is positive, if False, x is negative
    # If True, y is positive, if False, y is negative

    if x_polarity == False and y_polarity == True:
        A = 'A'
        return A
    elif x_polarity == True and y_polarity == True:
        B = 'B'
        return B
    elif x_polarity == False and y_polarity == False:
        C = 'C'
        return C
    else:
        D = 'D'
        return D
    
class UserElementInputs(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_element_name: str 
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
    __root__: List[UserElementInputs] # change to Element list

class MatrixOutputMetadata(BaseModel):
    user: UserData
    labels: XYInputLabel
    polarity: XYInputPolarity
    # preferrable_class: str = quadrant_classifier_label(XYInputPolarity)
    element_inputs: UserElementInputs
    element_values: UserElementValues
    element_list: UserElementList
    # output: UserElementValues.output


# Test data
pp = pprint.PrettyPrinter(indent=4)

user = UserData(
    first_name='A',
    last_name='O',
    username='AO97',
    password='password',
    confirm_password='password'
)

labels = XYInputLabel(x_label='Importance', y_label='Effort')

t1 = UserElementInputs(user_element_name='Do A')
t2 = UserElementInputs(user_element_name='Do B')

question_element_name = UserElementInputs(user_element_name='Do x')

polarity = XYInputPolarity(x_polarity=True, y_polarity=False)

list_of_tasks = [t1, t2]

pp.pprint(f'Task 1: {t1.user_element_name}  Task 2: {t2.user_element_name}')


matrix = MatrixOutputMetadata(
    user=user,
    labels=labels, 
    polarity=polarity,
    # preferrable_class=polarity,
    element_inputs=question_element_name,
    element_values=UserElementValues(element=question_element_name, x_value=50.0, y_value=40.0),
    element_list=list_of_tasks)


print(f'\nLABELS: {matrix.labels}\n\nMETADATA: {matrix.element_inputs}\nVALUES: {matrix.element_values}\n\nELEMENTS: {matrix.element_list}\n\n')