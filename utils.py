import json

def quadrant_classifier(x, y):

    """4 quadrants of preferrability classification defined based on X and Y polarity"""

    # A - Negative X Positive Y
    # B - Positive X Positive y
    # C - Negative X Negative Y
    # D - Positive X Negative Y 
    
    if x == False and y == True:
        A = 'Preferrable quadrant'
        return A
    elif x == True and y == True:
        B = 'Preferrable quadrant'
        return B
    elif x == False and y == False:
        C = 'Preferrable quadrant'
        return C
    else:
        D = 'Preferrable quadrant'
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

    # If the threshold is 50 then half of the agents' votes between urgency and importance will be split 50/50
    # This means that if 4/10 people vote urgent and 6/10 vote not urgent then it will be classed as a not urgent task
    # If it was 80 percent then if 3/10 people vote for an urgent task, 7/10 people vote as unurgent, it will still be classed as urgent?

    # Those remaining in important and less urgent, is there a way to delegate or automate that to other groups?
        
    # Default quadrants to be 50/50, could be flexible for other decision boundaries
    # Tasks could be ranked in terms of 'relative urgency'
    # Could each task be a feature that could be classed in the 4 quadrants?
    # Output is urgency? y-axis is importance/impact and x-axis is time and effort required
    # Proximity (how soon it should happen? not very soon 1-3 very soon), Impact, Difficulty
    # Look into MUST(what it must do) SHOULD (what it should do) COULD HAVE (what is nice to have) WONT (what is not possible, understanding of scope)

    # Task prioritisation planning could trigger a kanban board

    # Make it generalisable
    # Matrix is a visual aid that prompts for decision-making
    # Indicator of alignment - nearest dots, clustering algorithm.

