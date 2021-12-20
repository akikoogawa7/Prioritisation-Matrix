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

def avg_of_x_y(x_list, y_list):
    if len(x_list) == len(y_list):
        average_x = round(sum(x_list) / len(x_list), 2)
        average_y = round(sum(y_list) / len(y_list), 2)
    return average_x, average_y

# def multiply_x_positive_y_postive(x, y):
#     if x and y > 0:
#         z = x * y
#     return z
    
# def multiply_x_positive_y_negative(x, y):
#     if x > 0 and y < 0:
#         z = x * (100-y)
#     return z

# def multiply_x_negative_y_positive(x, y):
#     if x < 0 and y > 0:
#         z = (100-x) * y
#     return z

# def multiply_x_negative_y_negative(x, y):
#     if x < 0 and y < 0:
#         z = (100-x) * (100-y)
#     return z

def compute_z(avg_x, avg_y):
    if avg_x and avg_y > 0:
        z = avg_x * avg_y
    elif avg_x > 0 and avg_y < 0:
        z = avg_x * (100-avg_y)
    elif avg_x < 0 and avg_y > 0:
        z = (100-avg_x) * avg_y
    elif avg_x < 0 and avg_y < 0:
        z = (100-avg_x) * (100-avg_y)
    z = round(z, 2)
    return z

def ordinal_rank(z_list):
    z_ordinal_rank = np.sort(z_list)[::-1]
    return z_ordinal_rank

# x = [10.0, 20.0, 30.0]
# y = [20.4, 80.2, 100]

# avg_x, avg_y = avg_of_x_y(x, y)
# print(avg_x, avg_y)

# z = compute_z(avg_x, avg_y)
# print(z)

# rank = ordinal_rank(y)
# print(rank)

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