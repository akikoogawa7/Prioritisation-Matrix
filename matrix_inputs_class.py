import pandas as pd
import time
from utils import compute_inputs_json

class MatrixInputs():
    def __init__(self, inputs_dataset, agents_group_size=1, threshold=50, matrix=True):
        #TODO: Insert categories
        x = ('Urgent', 'Less Urgent')
        y = ('Important', 'Less Important')
        self.categories = [x, y]
        self.inputs_dataset = inputs_dataset
        self.agents_group_size = agents_group_size
        self.threshold = threshold

    def _compute_inputs_dataset(self, inputs_dataset):
        #TODO: Insert target and motivations to understand context of goals
        compute_inputs_json(inputs_dataset)

    def _calculate_threshold_against_groups_size(self, agent_groups_size, threshold):
        #TODO: Calculate the defining factor for classifying tasks into our 4 categories


    #TODO: Insert graphic and ML to classify tasks based on the amount of people who rate a task with weight