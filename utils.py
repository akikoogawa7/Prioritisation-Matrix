import json
from os import times_result
import numpy as np

def quadrant_classifier_for_values(x, y, threshold=50):

    """4 quadrants of preferrability classification defined based on X and Y threshold"""

    # A - Negative X Positive Y  - x less than 50, y more than 50
    # B - Positive X Positive y  - x more than 50, y more than 50
    # C - Negative X Negative Y  - x less than 50, y less than 50
    # D - Positive X Negative Y  - x more than 50, y less than 50

    if x < threshold and y > threshold:
        return x, y, 'A'
    elif x > threshold and y > threshold:
        return x, y, 'B'
    elif x < threshold and y < threshold:
        return x, y, 'C'
    else:
        return x, y, 'D'

def quadrant_classifier_label(x_polarity:bool, y_polarity:bool):

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

def compute_inputs_json(inputs_dataset):
    try:
        with open(inputs_dataset, 'r') as fp:
            inputs_dataset = json.load(fp)
            print(inputs_dataset)
            print('Data loaded')
    except IOError:
        print('File not found, will create a new one.')
        inputs_dataset = {}

def avg_of_list(list):
    if len(list) == len(list):
        average = round(sum(list) / len(list), 2)
    return average

def compute_z(x_polarity, y_polarity, avg_x, avg_y): # parameters should know the polarities of X and Y
    if x_polarity == False:
        corrected_x = 100 - avg_x
    if y_polarity == False:
        corrected_y = 100 - avg_y
    if x_polarity == True:
        corrected_x = avg_x
    if y_polarity == True:
        corrected_y = avg_y
    z = corrected_x * corrected_y
    z = round(z, 2)
    return z

z = compute_z(x_polarity=False, y_polarity=True, avg_x=0, avg_y=0)
print(z)

# So what we have to do here, is create another condition where if x is negative and y is positive, and if both x and y are at their most preferrable it can be, then we should do 10,000 minus 0 which makes the ordinal rank for this 10,000 which should be accurate.

def ordinal_rank(z_list):
    z_ordinal_rank = np.sort(z_list)[::-1]
    return z_ordinal_rank


def check_threshold_against_groups_size(agents_group_size, threshold):
    """
    Enter size of the voting party (no more than 50 participants) and the level of urgency (1-10) to achieve critical mass.
    """
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

def calculate_threshold_against_groups_size(agents_group_size, threshold):
    check_threshold_against_groups_size(agents_group_size, threshold)
    # if threshold == 50: