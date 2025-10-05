import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=20)
    
    # Create first line of best fit using all data
    slope_all, intercept_all, r_value, p_value, std_err = linregress(
        df['Year'], 
        df['CSIRO Adjusted Sea Level']
    )
    
    # Generate years from 1880 to 2050 for the first line
    years_extended = np.arange(1880, 2051)
    sea_level_pred_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_level_pred_all, 'r-', 
             label='Best fit line (1880-present)', linewidth=2)
    
    # Create second line of best fit using data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent['Year'], 
        df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Generate years from 2000 to 2050 for the second line
    years_recent = np.arange(2000, 2051)
    sea_level_pred_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_pred_recent, 'g-', 
             label='Best fit line (2000-present)', linewidth=2)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data (for testing)
    plt.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
    print("Plot created successfully! Check sea_level_plot.png")
