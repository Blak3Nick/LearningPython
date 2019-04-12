import pandas as pd
import numpy as np
happiness2015 = pd.read_csv("C:\\Users\\Cyr1lfiggus1\\Downloads\\World_Happiness_2015.csv")
grouped = happiness2015.groupby('Region')
aus_nz = grouped.get_group('Australia and New Zealand')

print(happiness2015['Region'].unique())
grouped = happiness2015.groupby('Region')
north_america = happiness2015.iloc[[4,14]]
na_group = grouped.get_group('North America')
equal = north_america == na_group

means = grouped.mean()
happy_grouped = grouped['Happiness Score']
happy_mean = happy_grouped.mean()
happy_mean_max = happy_grouped.agg([np.mean, np.max])
def dif(group):
    return (group.max() - group.mean())

mean_max_dif = happy_grouped.agg(dif)
