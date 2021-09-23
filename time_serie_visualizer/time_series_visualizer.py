import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv')
#df.columns
df['value'].describe().round(2)
# Clean data
df=df[
    (df['value'] >= (df['value'].quantile(0.025))) & #this takes into account the row which aren't in the bottom part
    (df['value'] <= (df['value'].quantile(0.975))) # and this other statement the ones thar aren't in the top part

]
df.describe().round(2) #to check if the numbers of rows changed
df


def draw_line_plot():
    # Draw line plot
    ig=plt.figure(figsize=(12,4))
    plt.plot(df['date'], df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index)

    df['year']=df.index.year
    df['month']=df.index.month
    barChart=df.groupby(['year', 'month'],)['value'].mean()
    barChart=barChart.unstack()

    fig=barChart.plot.bar(legend=True, figsize=(12,5),ylabel='Average Page Views',xlabel='Years')


    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title = 'Months')
    #fig.savefig('bar_plot.png') 

    # Draw bar plot





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
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    fig,axis = plt.subplots(1,2)
    fig.set_size_inches(18,7)
    sns.boxplot(x = df_box['year'], y = df_box['value'], ax = axis[0]).set(xlabel='Year', ylabel='Page Views')
    sns.boxplot(x = df_box['month'], y = df_box['value'], 
        order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec'], 
        ax = axis[1]).set(xlabel='Month', ylabel='Page Views')
    axis[0].set_title('Year-wise Box Plot (Trend)')
    axis[1].set_title('Month-wise Box Plot (Seasonality)')

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
