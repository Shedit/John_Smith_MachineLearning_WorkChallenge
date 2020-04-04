import pandas as pd
import numpy as np
import matplotlib as plt

#%% 
from sklearn import preprocessing
#job_skills = pd.read_csv('data/job_skills.csv')

#%% 

# Manual definition for all Provinces. Easiest and minimal typing.

PROVINCES = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 'New brunswick', 'Qebuec', 'Ontario', 'Manitoba', 'Saskatchewan', 'Alberta', 'British Columbia']

# Read CSV and use the second line (header=1) as column names. 
by_prov_and_sex = pd.read_csv('data/t006a-eng.csv', header = [1])

#Removing whitespaces and renaminging columns
col_names = list(by_prov_and_sex.columns)

for i, c in enumerate(col_names): 
    if i == 0:
        col_names[i] = 'index'
    else: 
        col_names[i] = c.lstrip()

by_prov_and_sex.columns = col_names

# Get INDEXES in DF where PROVINCES are located. 
get_province_indexes = [(i,j)[0] for i, j in enumerate(by_prov_and_sex.isin(PROVINCES).iloc[:, 0]) if j == True ]

# Remove data containing NaN expect for the rows containing PROVINCE names.
by_prov_and_sex = by_prov_and_sex[(by_prov_and_sex.iloc[:, 1].notna()) & (by_prov_and_sex.iloc[:, 0].notna()) | (by_prov_and_sex.iloc[:, 0].isin(PROVINCES))]

# Get all WORK_TITLES in DataFrame. By Selecting all unique values in column 0 that is NOT in PROVINCES or the word totals which are Aggregations
WORK_TITLES = list(
    by_prov_and_sex[(~by_prov_and_sex.iloc[:, 0].isin(PROVINCES)) & \
    (~by_prov_and_sex.iloc[:, 0].str.contains('Total')) & \
    (~by_prov_and_sex.iloc[:, 0].str.contains('Services-producing')) & \
    (~by_prov_and_sex.iloc[:, 0].str.contains('Goods-producing'))].iloc[:,0].unique())

# %%
## Build tidy dataframe 

## Setting MultiIndex for re-engineering pivoted Data, where First index is Province and second is Work Class
multiindex = [(i, j) for i in PROVINCES for j in WORK_TITLES]
multiindex = pd.MultiIndex.from_tuples(multiindex, names=['Province', 'Workclass'])
# %%
# Setting new data frame with Index
newDF = pd.DataFrame(index = multiindex)

#Finding all data from fist columns by selecting all rows in index Column that does no contain PROVINCES
merge_data = by_prov_and_sex[ \
    (~by_prov_and_sex['index'].isin(PROVINCES)) & \
    (~by_prov_and_sex['index'].str.contains('Total')) & \
    (~by_prov_and_sex['index'].str.contains('Services-producing')) & \
    (~by_prov_and_sex['index'].str.contains('Goods-producing')) \
    ]
# Reseting index for clean index merge  
merge_data = merge_data.reset_index(drop = True)
newDF = newDF.reset_index()

# merging Data by index 
newDF = newDF.merge(merge_data, left_index=True, right_index=True)

# Set back the original indexes and deleting the row duplicate created by the merging
newDF = newDF.set_index(['Province','Workclass'])
del newDF['index']


# %%
import plotly.express as px 

newDF = newDF.reset_index()


fig = px.bar(newDF, x='Province', y='February 2019', color='Workclass', hover_name='Workclass')

fig.update_layout(showlegend=False)

fig.show()
# %%
