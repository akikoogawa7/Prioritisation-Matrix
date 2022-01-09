import matplotlib.pyplot as plt
import seaborn as sns
# from utils import avg_of_list
import pandas as pd
import cv2 as cv
import numpy as np

default_x_y_values = [0]

# Matrix A
def generate_matrix_A(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values=default_x_y_values, y_values=default_x_y_values):
    threshold = 50

    if default_x_y_values > x_values[0]:
        x_values[0] = default_x_y_values
    if len(default_x_y_values) > 0:
        x_values.append(default_x_y_values)

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
    plt.text(x=75, y=25, s="Q4",alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=25, s="Q3",alpha=0.7,fontsize=14, color='b')
    plt.text(x=75, y=75, s="Q2", alpha=0.7,fontsize=14, color='b')
    plt.text(x=25, y=60, s="Q1", alpha=0.7,fontsize=14, color='b')

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

# Matrix B
def generate_matrix_B(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values=default_x_y_values, y_values=default_x_y_values):
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

# Matrix C
def generate_matrix_C(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values=default_x_y_values, y_values=default_x_y_values):
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

# Matrix D
def generate_matrix_D(num_of_users, name, problem, class_name, x_label, y_label, x_polarity, y_polarity, x_values=default_x_y_values, y_values=default_x_y_values):
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

# Make synthetic data:
xData = np.random.randint(100, size=dataSize)
yData = np.linspace(0, dataSize, num=dataSize, dtype=int)

# generate_matrix_A(num_of_users=3, name='matrixA', problem='Task A', class_name='A' , x_label='Time', y_label='Effort', x_polarity='negative', y_polarity='positive')
# generate_matrix_B(num_of_users=3, name='matrixB', problem='Task B', class_name='B' , x_label='Time', y_label='Effort', x_polarity='positive', y_polarity='positive')
# generate_matrix_C(num_of_users=3, name='matrixC', problem='Task C', class_name='C', x_label='Time', y_label='Effort', x_polarity='negative', y_polarity='positive', x_values=xData, y_values=yData)
# generate_matrix_D(num_of_users=3, name='matrix', problem='Task A', class_name='D' , x_label='Time', y_label='Effort', x_polarity='positive', y_polarity='negative', x_values=xData, y_values=yData)


def check_matrix(preferred_quadrant):
    if preferred_quadrant == 'A':
        return generate_matrix_A
    elif preferred_quadrant == 'B':
        return generate_matrix_B
    elif preferred_quadrant == 'C':
        return generate_matrix_C
    else:
        return generate_matrix_D