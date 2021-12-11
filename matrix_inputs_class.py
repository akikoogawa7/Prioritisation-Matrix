import pandas as pd
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing import Optional, NamedTuple, List, Dict
from datetime import datetime
from utils import compute_inputs_json, check_threshold_against_groups_size

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

class UserItemInputs(BaseModel):
    # list_of_tasks: List[TasksInputs] = None
    labels: XYInputs
    metadata: TasksInputs
    

user_1 = UserItemInputs(labels=XYInputs('Importance', 'Effort'), metadata=TasksInputs(task='Do x', x_value=10.0, y_value=10.0))
print(f'LABELS: {user_1.labels}, METADATA: {user_1.metadata}')


# class MatrixInputs():
#     def __init__(self, inputs_dataset, agents_group_size=1, threshold=50, matrix=True):
#         #TODO: Insert categories
#         x = ('Urgent', 'Less Urgent')
#         y = ('Important', 'Less Important')
#         self.categories = [x, y]
#         self.inputs_dataset = inputs_dataset
#         self.agents_group_size = agents_group_size

#     def _compute_inputs_dataset(self, inputs_dataset):
#         #TODO: Insert target and motivations to understand context of goals
#         compute_inputs_json(inputs_dataset)

#     def _calculate_threshold_against_groups_size(self, agents_groups_size, threshold):
#         #TODO: Calculate the defining factor for classifying tasks into our 4 categories

#         # Checks if values are within limits and throws error if not
#         check_threshold_against_groups_size(agents_groups_size, threshold)
        

#     #TODO: Insert graphic and ML to classify tasks based on the amount of people who rate a task with weight.
#     # Will the graph size depend on the number of voters?
#     # Will the division between classes be defined by the threshold? Maybe the threshold complicates things?