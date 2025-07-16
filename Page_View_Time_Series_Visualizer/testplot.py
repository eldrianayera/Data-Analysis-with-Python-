import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    'fcc-forum-pageviews.csv' ,
    parse_dates= True ,
    index_col= 'date'
)

# Clean data
df = df[df['value'].between(df['value'].quantile(0.025) , df['value'].quantile(0.975))]


df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['HAHA'] = df_box['date'].dt.year
df_box['month'] = [d.strftime('%b') for d in df_box.date]
df_box['HEHE'] = df_box['date'].dt.month_name()

df_box['monthnumber'] = df.index.month



print(df_box)


