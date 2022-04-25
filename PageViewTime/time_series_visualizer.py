import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'fcc-forum-pageviews.csv', index_col='date', )
df.index = pd.to_datetime(df.index)
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    plt.plot(df,color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig = plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    # Draw bar plot
    df_bar.groupby(['month', 'year'])['value'].mean()
    plt.figure(figsize = (9,9))
    fig = sns.barplot(data=df_bar, ci = None,x='year', hue='month', hue_order=('January','February','March','April','May','June','July','August','September','October','November','December'),y ='value', palette='tab10')
    plt.legend(loc='upper left')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.figure.savefig('bar_plot.jpg')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes= plt.subplots(1,2, figsize=(20,9))
    sns.boxplot(data=df_box, x='year', y='value',ax=axes[0])
    sns.boxplot(data=df_box, x='month', y='value',ax=axes[1],hue_order=('January','February','March','April','May','June','July','August','September','October','November','December'))
    plt.show()

    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.jpg')
    return fig

