# Import package for environment setting
import pandas as pd
import numpy as np
import seaborn as sns


        
# null check
def null_check(df_input):
    '''
    df_input: the pandas dataframe that used to check missing percentage for all columns
    '''
    for col in df_input.columns:
        pct = (df_input[col].isnull().sum()/len(df_input))*100
        print('Column',col,'has',pct,'% of missing records')

        
# distribution plot        
def dist_plot(df_input, drop_list):
    '''
    df_input: the pandas dataframe that used to create distribution plot
    drop_list: columns that not used to generate distribution plot
    '''
    df_input = df_input.drop(drop_list, axis=1)
    columns = list(df_input.columns)
    dfm = df_input.melt(var_name='columns')
    g = sns.FacetGrid(dfm, col='columns')
    g = (g.map(sns.distplot, 'value'))
        
    