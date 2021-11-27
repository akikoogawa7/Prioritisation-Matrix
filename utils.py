
import json

def compute_user_inputs_dataset(inputs_dataset, agent_group_size):
    if json.loads(inputs_dataset):
        return 'true'

if __name__ == '__main__':
    compute_user_inputs_dataset(test.json)