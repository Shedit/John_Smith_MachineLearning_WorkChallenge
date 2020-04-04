import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 


data = pd.read_excel('data/LFS_data.xlsx', sheet_name = ['GEO_CANADA', 'GEO_PROVINCE'])
#%% 

geo_canada = data['GEO_CANADA']
geo_province = data['GEO_PROVINCE']

#%% 

del geo_canada['GEO']

geo_canada.columns = ['date', 'labour_force_type',
       'naics', 'sex',
       'age_group', 'value']

geo_province.columns = ['date', 'province', 'labour_force_type',
       'naics', 'sex',
       'age_group', 'value']

#%% 

for col in geo_canada.columns[0:-1]:
    geo_province[col] = geo_province[col].astype('category')

for col in geo_province.columns[0:-1]:
    geo_province[col] = geo_province[col].astype('category')

# %%
def plot_px(df, xx, yy, colorr):

    df2 = df.groupby([colorr, xx]).sum()
    df2 = df2.reset_index()
    return px.line(df2, x=xx, y=yy, color=colorr)

# %%
plot_px(geo_province, xx='REF_DATE', yy='VALUE', colorr='Age group')

# %%
