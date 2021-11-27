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
        print('THRESHOLD LOG: Error! Threshold must be less than and up to 100')
    elif threshold < 50:
        print('THRESHOLD LOG: Caution! Thresholds lower than 50 will make tasks less urgent and important')
    elif threshold == 0:
        print('THRESHOLD LOG: Error! Threshold must be included in order to determine urgency and importance')
    else:
        print(f'THRESHOLD: {threshold}')

    if agents_group_size > 50:
        print('GROUP SIZE LOG: Error! Group size of more than 50 will make tasks harder to optimize')
    elif agents_group_size == 0:
        print('GROUP SIZE LOG: Error! Group size cannot be 0')
    else:
        print(f'GROUP SIZE: {agents_group_size}')

calculate_threshold_against_groups_size(agents_group_size=10, threshold=60)