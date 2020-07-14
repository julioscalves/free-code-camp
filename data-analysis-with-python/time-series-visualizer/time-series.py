import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('time-series.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[df['value']  >= df['value'].quantile(0.025)]
df = df.loc[df['value']  <= df['value'].quantile(0.975)]

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(16, 8))
    sns.lineplot(x=df.index, y=df.value, data=df, legend=False)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df.index.year), (df.index.month)]).mean().unstack()
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    ax = df_bar.plot(kind='bar', figsize=(16, 8))
    ax.legend(title='Months', labels=labels)
    ax.set(xlabel='Years', ylabel='Average daily page views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16,8))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax[0].set(title='Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', data=df_box.loc[~(df_box.year == 2016) | (df_box.year == 2019)], ax=ax[1])
    ax[0].set(title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
