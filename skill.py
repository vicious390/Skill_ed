from email.policy import default
from enum import unique
import numbers
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
st.set_page_config(page_title='Skill-Ed',
                    layout="wide")
excel_file = 'job.xlsx'
sheet_name ='out'
df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:C',
                    header=0)
st.dataframe(df)
col1,col2 = st.columns(2)  
job = df['job role'].unique().tolist()
col1.header("SELECT JOB")
skills=col1.multiselect('select the skill',job )
mask = df['job role'].isin(skills)

col2.header("TOP SKILLS")
results = df[mask].head()
st.dataframe(results)
bar_chart = px.bar(results,
                    x='skill',
                    y='number',
                    text='number',
                    color_discrete_sequence = ['#F63366']*len(results),
                    template='plotly_white')
col2.plotly_chart(bar_chart)                    