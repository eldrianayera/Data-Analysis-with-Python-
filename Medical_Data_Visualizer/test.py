import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] =  (df['weight'] / ((df['height']/100) ** 2) > 25).astype(int)




# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int) 
df['gluc'] = (df['gluc'] > 1).astype(int) 



# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars = ['cardio'],
        value_vars = ['cholesterol','gluc','smoke','active','alco','overweight']
    )

    print(f"ssss\n{df_cat}")
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    print(f"ffff\n{df_cat}")
    
    

    # 7
    fig = sns.catplot (
        data = df_cat ,
        x = 'variable',
        col = 'cardio',
        hue = 'value' ,
        kind = 'count'

    ).set(ylabel = 'total').fig


    # 9
    fig.savefig('catplot.png')
    return fig
    
    print(f"ssssss{type(fig)}")
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
  
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
 

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)
    



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(
        corr,
        mask=mask,
    )


    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()