import json

def compute_inputs_json(inputs_dataset):
    try:
        with open(inputs_dataset, 'r') as fp:
            inputs_dataset = json.load(fp)
            print(inputs_dataset)
            print('Data loaded')
    except IOError:
        print('File not found, will create a new one.')
        inputs_dataset = {}

def calculate_threshold_against_groups_size(agents_group_size, threshold):
    if threshold > 100:
        print('Error! Threshold must be less than and up to 100')
    elif threshold < 50:
        print('Error! Thresholds lower than 50 will make tasks less urgent and important')