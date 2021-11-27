import pandas as pd
import time

class MatrixInputs():
    def __init__(self, inputs_dataset, agents_group_size, matrix=True):
        #TODO: Insert categories
        x = ('Urgent', 'Less Urgent')
        y = ('Important', 'Less Important')
        self.categories = [x, y]
        self.inputs_dataset = inputs_dataset
        self.agents_group_size = agents_group_size

    def _compute_inputs_dataset(inputs_dataset):
        #TODO: Insert target and motivations to understand context of goals
        

    #TODO: Insert graphic and ML to classify tasks based on the amount of people who rate a task with weight