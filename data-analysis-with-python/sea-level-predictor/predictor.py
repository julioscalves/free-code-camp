import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x=x, y=y)

    # Create first line of best fit
    first_slope, first_intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    first_reg_x = range(1880, 2050)  

    # Create second line of best fit
    second_df = df.loc[(df['Year'] >= 2000)]
    second_slope, second_intercept, r_value, p_value, std_err = linregress(x=second_df['Year'], y=second_df['CSIRO Adjusted Sea Level'])
    second_reg_x = range(2000, 2050)

    plt.plot(first_reg_x, first_intercept + first_slope*first_reg_x, 'y', label='fitted line')
    plt.plot(second_reg_x, second_intercept + second_slope*second_reg_x, 'r', label='fitted line')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
