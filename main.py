import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache
def load_data ():
    df=pd.read_csv('master_data.csv',index_col='lockdown')
    numeric_df=df.select_dtypes(['float','int'])
    text_df=df.select_dtypes(['object'])

    return df,numeric_df,text_df



df,numeric_df,text_df=load_data()
show_data=st.sidebar.checkbox(label="show dataset")
if show_data:
    st.write(df)
feature_selection=st.sidebar.multiselect(label='features',options=numeric_df.columns.unique())
lockdown_select=st.sidebar.selectbox(label='lockdown',options=np.append(df['region'].unique(),'Whole France'))
if lockdown_select!='Whole France':
    df=df[df['region']==lockdown_select]
df_features=df[feature_selection]
plot=px.scatter(data_frame=df_features,x=df_features.index ,y=feature_selection)
plot2=px.bar(data_frame=df_features,x=df_features.index,y=feature_selection)
plot3=px.line(data_frame=df_features,x=df_features.index,y=feature_selection)


st.plotly_chart(plot)
st.plotly_chart(plot2)
st.plotly_chart(plot3)

