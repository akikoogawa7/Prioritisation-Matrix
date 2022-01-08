import matplotlib.pyplot as plt
import seaborn as sns
import asyncio
from utils import avg_of_list
import pandas as pd

def generate_matrix(num_of_users, name, problem, x_label, y_label, x_polarity, y_polarity, x_values, y_values):
    threshold = 50

    # this function should generate the average/mean of x and y values
    avg_x, avg_y = avg_of_list(num_of_users, x_values, y_values)
    # print(f'Your average X values are {avg_x}.\nYour average Y values are {avg_y}.')

    # Title 
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.title(f'{problem}')
    plt.suptitle(f'{name}')

    #Scatterplot
    data = pd.DataFrame({f'{x_label}':x_values, f'{y_label}':y_values})
    print(data)
    # sns.relplot(data=data, x=f'{x_label}', y=f'{y_label}', hue=f'{[x_label, y_label]}')
    # sns.scatterplot(data=data, y=f'{y_label}', hue=f'{y_label}')

    # to add 2 hues, concatenate x and y into one column

    # x and y axis labels
    plt.xlabel(f'{x_label}')
    plt.ylabel(f'{y_label}')

    # Quadrant Marker          
    plt.text(x=40000, y=68, s="Q4",alpha=0.7,fontsize=14, color='b')
    plt.text(x=15000, y=68, s="Q3",alpha=0.7,fontsize=14, color='b')
    plt.text(x=15000, y=78, s="Q2", alpha=0.7,fontsize=14, color='b')
    plt.text(x=40000, y=78, s="Q1", alpha=0.7,fontsize=14, color='b')   

    # Benchmark Mean values          
    plt.axhline(y=50, color='k', linestyle='--', linewidth=1)           
    plt.axvline(x=50, color='k',linestyle='--', linewidth=1) 

    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.show()

generate_matrix(3, 'matrix', 'problem', 'time', 'effort', 'positive', 'negative', [10.0, 60, 40.0], [10.0, 20.0, 40.0])