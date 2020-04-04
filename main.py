import numpy as np
import pandas as pd
import plotly.express as px 

#%% 
# Data import from Table 14-10-0023-01 "Labour force by industry, annual", with option province

emp_data = pd.read_csv('data/LFS_data_annual.csv')

#%% 
# Choosing columns to use.

emp_data = emp_data[['REF_DATE', 'GEO', 'North American Industry Classification System (NAICS)', 'Sex',
       'Age group', 'VALUE']]
# Checking it worked 
emp_data.columns == ['REF_DATE', 'GEO', 'North American Industry Classification System (NAICS)', 'Sex',
       'Age group', 'VALUE']
# renaming columns
emp_data.columns = ['year', 'province', 'naics_class', 'sex',
       'age_group', 'value']

# %%

# A dynamic plot where the static x = year and y = value,
# and the color of the entity is sorted by choice of category. 

import plotly.graph_objects as go 

def get_grouped_df(df, col):
    df = df.groupby(['year', col]).sum().reset_index()
    return df 
# getting dataframes grouped and ready. 

a_list_df = []
for col in emp_data.columns[1:-1]:
    a_df = get_grouped_df(emp_data, col)
    a_list_df.append(a_df)


fig = go.Figure()

bool_list = []

for df in a_list_df:
    if df.columns[1] == 'province':

        for each in df.iloc[:, 1].unique():
            bool_list.append(True)
            fig.add_trace(go.Bar(x= df['year'].unique(), y=df[df.iloc[:, 1] == each][
                'value'], visible = True, name=each))
    else: 
        for each in df.iloc[:, 1].unique():
            bool_list.append(False)
            fig.add_trace(go.Bar(x= df['year'].unique(), y=df[df.iloc[:, 1] == each][
                'value'], visible = False, name=each))


bool_naics = [ True if df.columns[1] == 'naics_class' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]

bool_sex = [ True if df.columns[1] == 'sex' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]
bool_age = [ True if df.columns[1] == 'age_group' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.5,
            buttons=list([
                dict(label="Province",
                     method="update",
                     args=[{"visible": bool_list},
                           {"title": "Employment 2014-2019 by Province measured in thousands",
                            "barmode": "relative",
                            "showlegend": True}]),
                dict(label="NAICS class",
                     method="update",
                     args=[{"visible": bool_naics},
                           {"title": "Employment 2014-2019 by Work class measured in thousands",
                           "barmode": "relative",
                           "showlegend": False}]),
                dict(label="Sex",
                     method="update",
                     args=[{"visible": bool_sex},
                           {"title": "Employment 2014-2019 by Sex measured in thousands",
                           "barmode": "group",
                           "showlegend": True}]),
                dict(label="Age group",
                     method="update",
                     args=[{"visible": bool_age},
                           {"title": "Employment 2014-2019 by Age group measured in thousands",
                           "barmode": "group",
                           "showlegend": True}]),
            ]),
        )
    ])

fig.update_layout(title="Employment 2014-2019 by Province measured in thousands", barmode= "relative")

#%% 

def get_grouped_df_change(df, col):
    df = df.groupby([col, 'year']).sum().reset_index()
    df['change_yearly'] = df.groupby(col).diff().fillna(0)['value']
    df['change_from_2014'] = df.groupby(col)['change_yearly'].cumsum().fillna(0).astype(int)
    return df 


b_list_df = []
for col in emp_data.columns[1:-1]:
    b_df = get_grouped_df_change(emp_data, col)
    b_list_df.append(b_df)


fig2 = go.Figure()

bool_list = []

for df in b_list_df:
    if df.columns[0] == 'province':

        for each in df.iloc[:, 0].unique():
            bool_list.append(True)
            fig2.add_trace(go.Bar(x= df['year'].unique(), y=df[df.iloc[:, 0] == each][
                'change_from_2014'], visible = True, name=each))
    else: 
        for each in df.iloc[:, 0].unique():
            bool_list.append(False)
            fig2.add_trace(go.Bar(x= df['year'].unique(), y=df[df.iloc[:, 0] == each][
                'change_from_2014'], visible = False, name=each))

bool_naics = [ True if df.columns[1] == 'naics_class' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]

bool_sex = [ True if df.columns[1] == 'sex' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]
bool_age = [ True if df.columns[1] == 'age_group' \
            else False\
                for df in a_list_df \
                    for i in df.iloc[:, 1].unique()]
fig2.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.5,
            buttons=list([
                dict(label="Province",
                     method="update",
                     args=[{"visible": bool_list},
                           {"title": "Employment Change from 2014 by Province measured in thousands",
                            "barmode": "relative",
                            "showlegend": True}]),
                dict(label="NAICS class",
                     method="update",
                     args=[{"visible": bool_naics},
                           {"title": "Employment Change from 2014 by Work class measured in thousands",
                           "barmode": "relative",
                           "showlegend": False}]),
                dict(label="Sex",
                     method="update",
                     args=[{"visible": bool_sex},
                           {"title": "Employment Change from 2014 by Sex measured in thousands",
                           "barmode": "group",
                           "showlegend": True}]),
                dict(label="Age group",
                     method="update",
                     args=[{"visible": bool_age},
                           {"title": "Employment Change from 2014 by Age group measured in thousands",
                           "barmode": "group",
                           "showlegend": True}]),
            ]),
        )
    ])

fig2.update_layout(title="Employment Change 2014-2019 by Province measured in thousands", barmode= "relative")

# %%
## Checking out the job skills data 

job_skills = pd.read_csv('data/job_skills.csv') 
#%% 

# lowercase all columns 
job_skills.columns = [i for i in map(str.lower, job_skills.columns)]


# %%
# What is the top mentioned (based on frequency) of each dimension for each company and how many times is that type mentioned? 

#Getting a new table with describe values that summarizes the table contents
describe_table = job_skills.groupby('company').describe().stack().reset_index()

# Renaming the
describe_table.columns = ['company', 'describe', 'title', 'category', 'location',
       'responsibilities', 'minimum qualifications',
       'preferred qualifications']

describe_table[(describe_table['describe'] == 'top') | (describe_table['describe'] == 'freq')]


# %%
 
# What are the most mentioned words (top 10) when it comes to preferred skills? 

import string
from itertools import chain
from nltk.corpus import stopwords
from nltk import word_tokenize

stoplist = set(stopwords.words('english'))
stoplist.update(list(string.punctuation))
stoplist.update(['2018', '2019', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'skills', 'ability', 'demonstrated'])


# %%
job_skills['preferred qualifications'] = job_skills['preferred qualifications'].astype(str)

b_list = []

for i, c in job_skills.iterrows():
    input_str = c['preferred qualifications'].lower()
    tokenized = word_tokenize(input_str)
    tokenized_nostop = [token for token in tokenized if token not in stoplist]
    b_list.append(tokenized_nostop)
    

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# Dechain nested list 
b_list = list(chain.from_iterable(b_list))

b_list = wordListToFreqDict(b_list) 

b_list = sortFreqDict(b_list)

#%% 

b_list = pd.DataFrame(b_list, columns = ['amount', 'word'])

print(b_list.head(10))

# %%

px.bar(b_list, x='word', y='amount')