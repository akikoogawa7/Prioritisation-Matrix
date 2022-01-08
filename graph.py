import matplotlib.pyplot as plt
from utils import avg_of_list
import seaborn as sns

def generate_matrix():
    threshold = 50

    matrix_name = 'Matrix'
    problem_name = 'Problem'
    x_label = 'x label'
    y_label = 'y label'
    x = [2, 23, 50, 80]
    y = [2, 23, 50, 80]

    #Scatterplot
    # sns.scatterplot(data=matrix_values,x='gni_pc', y='life_ex')

    # Title 
    plt.figure(figsize=(8, 8))
    plt.title(f'{problem_name}')
    plt.suptitle(f'{matrix_name}')

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

    plt.show()