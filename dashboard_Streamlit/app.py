import streamlit as st
import pandas as pd
import plotly.express as px

df_final = pd.read_csv("df_final.csv")

st.title("Análise Educacional Brasileira")

fig = px.scatter(df_final,x="renda",y="desempenho",size="pop_size",color="regiao",hover_name="estado")

st.plotly_chart(fig,use_container_width=True)