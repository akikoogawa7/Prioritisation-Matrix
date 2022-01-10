import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import cv2 as cv
import numpy as np
from utils_functions import avg_of_list

# Template A
def matrix_template_A(name, problem, class_name, x_label, y_label, x_polarity, y_polarity):
    threshold = 50

    # Style
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(25, 75, f'{class_name}', size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def matrix_template_B(name, problem, class_name, x_label, y_label, x_polarity, y_polarity):
    threshold = 50

    # Style
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(75, 75, f'{class_name}', size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def matrix_template_C(name, problem, class_name, x_label, y_label, x_polarity, y_polarity):
    threshold = 50

    # Style
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(25, 25, f'{class_name}', size=60.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def matrix_template_D(name, problem, class_name, x_label, y_label, x_polarity, y_polarity):
    threshold = 50

    # Style
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(75, 25, f"{class_name}", size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()


# Matrix with values
def generate_matrix_A(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values, y_values):
    threshold = 50

    # this function should generate the average/mean of x and y values
    # avg_x, avg_y = avg_of_list(num_of_users, x_values, y_values)

    # Style
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']

    #Scatterplot
    x_data = pd.DataFrame({f'{x_label}':x_values})
    y_data = pd.DataFrame({f'{y_label}':y_values})
    xy_data = pd.concat([x_data, y_data], axis=1, join='inner')
    # img = cv.imread("Images/Eisenhower-Matrix.jpeg")

    sns.relplot(data=xy_data, x=f'{x_label}', y=f'{y_label}', hue=xy_data[[f'{x_label}', f'{y_label}']].apply(tuple, axis=1), height=6, aspect=8/8)
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(25, 75, f'{class_name}', size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def generate_matrix_B(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values, y_values):
    threshold = 50

    # this function should generate the average/mean of x and y values
    # avg_x, avg_y = avg_of_list(num_of_users, x_values, y_values)

    # Style 
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']

    #Scatterplot
    x_data = pd.DataFrame({f'{x_label}':x_values})
    y_data = pd.DataFrame({f'{y_label}':y_values})
    xy_data = pd.concat([x_data, y_data], axis=1, join='inner')
    img = cv.imread("Images/Eisenhower-Matrix.jpeg")

    sns.relplot(data=xy_data, x=f'{x_label}', y=f'{y_label}', hue=xy_data[[f'{x_label}', f'{y_label}']].apply(tuple, axis=1), height=6, aspect=8/8)
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(75, 75, f'{class_name}', size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def generate_matrix_C(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values, y_values):
    threshold = 50

    # this function should generate the average/mean of x and y values
    # avg_x, avg_y = avg_of_list(num_of_users, x_values, y_values)

    # Style 
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']

    #Scatterplot
    x_data = pd.DataFrame({f'{x_label}':x_values})
    y_data = pd.DataFrame({f'{y_label}':x_values})
    xy_data = pd.concat([x_data, y_data], axis=1, join='inner')
    img = cv.imread("Images/Eisenhower-Matrix.jpeg")

    sns.relplot(data=xy_data, x=f'{x_label}', y=f'{y_label}', hue=xy_data[[f'{x_label}', f'{y_label}']].apply(tuple, axis=1), height=6, aspect=8/8)
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(25, 25, f'{class_name}', size=60.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

def generate_matrix_D(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values, y_values):
    threshold = 50

    # this function should generate the average/mean of x and y values
    # avg_x, avg_y = avg_of_list(num_of_users, x_values, y_values)
    
    # Style 
    sns.set_style("darkgrid")

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica Neue']

    #Scatterplot
    x_data = pd.DataFrame({f'{x_label}':x_values})
    y_data = pd.DataFrame({f'{y_label}':y_values})
    xy_data = pd.concat([x_data, y_data], axis=1, join='inner')
    img = cv.imread("Images/Eisenhower-Matrix.jpeg")

    sns.relplot(data=xy_data, x=f'{x_label}', y=f'{y_label}', hue=xy_data[[f'{x_label}', f'{y_label}']].apply(tuple, axis=1), height=6, aspect=8/8)
    
    # Title 
    plt.title(f'{problem}', fontsize=12)
    plt.suptitle(f'{name}', fontsize=14)

    # x and y axis labels
    plt.xlabel(f'{x_label}', fontsize=11)
    plt.ylabel(f'{y_label}', fontsize=11)

    # Quadrant Marker        
    plt.text(x=75, y=25, s="D",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="C",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="B", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=75, s="A", alpha=0.7,fontsize=14, color='b')

    plt.text(75, 25, f"{class_name}", size=50.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.5, 0.5, 0.5),
                   fc=(0.2, 0.8, 0.8),
                   ), fontsize=20
         )
    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=0.5)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=0.5) 

    # Sets axis limit
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    # plt.imshow(img, extent=[0, 100, 0, 100], aspect='auto')

    # Adjusts size
    plt.subplots_adjust(left=0.124, bottom=0.133, right=0.76, top=0.887)
    plt.show()

dataSize = 50

test_user_values = {
    'user1': 5,
    'user2': 2,
    'user3': 3,
    'user4': 2,
    'user5': 1}

# Make synthetic data:
xData = np.random.randint(100, size=dataSize)
yData = np.linspace(0, dataSize, num=dataSize, dtype=int)

# generate_matrix_A(num_of_users=3, name='matrixA', problem='Task A', class_name='A' , x_label='Time', y_label='Effort', x_polarity='negative', y_polarity='positive', x_values=test_user_values, y_values=test_user_values)
# generate_matrix_B(num_of_users=3, name='matrixB', problem='Task A', class_name='B' , x_label='Time', y_label='Effort', x_polarity='positive', y_polarity='positive', x_values=test_user_values, y_values=test_user_values)
# generate_matrix_C(num_of_users=3, name='matrixC', problem='Task A', class_name='C' , x_label='Time', y_label='Effort', x_polarity='negative', y_polarity='negative', x_values=test_user_values, y_values=test_user_values)
# generate_matrix_D(num_of_users=3, name='matrixD', problem='Task A', class_name='D' , x_label='Time', y_label='Effort', x_polarity='positive', y_polarity='negative', x_values=test_user_values, y_values=test_user_values)

# Generate matrix based on quadrant
def check_matrix(preferred_quadrant):
    if preferred_quadrant == 'A':
        return generate_matrix_A
    elif preferred_quadrant == 'B':
        return generate_matrix_B
    elif preferred_quadrant == 'C':
        return generate_matrix_C
    else:
        return generate_matrix_D

def check_matrix_template(preferred_quadrant):
    if preferred_quadrant == 'A':
        return matrix_template_A
    elif preferred_quadrant == 'B':
        return matrix_template_B
    elif preferred_quadrant == 'C':
        return matrix_template_C
    else:
        return matrix_template_D
