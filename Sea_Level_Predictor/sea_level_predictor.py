import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x=df['Year'],y =df['CSIRO Adjusted Sea Level'],)
    
    # Create first line of best fit
    slope,intercept = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[:2]
    x = np.linspace(1880,2050,100)
    y= slope*x+intercept
    plt.plot(x,y, 'r')
    
    # Create second line of best fit
    df1 = df
    df1 = df1[df1['Year'] >= 2000]
    slope,intercept = linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])[:2]
    x = np.linspace(2000,2050,100)
    y= slope*x+intercept
    plt.plot(x,y, 'b')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.jpg')
    return plt.gca()