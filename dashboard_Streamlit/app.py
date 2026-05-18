import streamlit as st
import pandas as pd
import plotly.express as px

df_final = pd.read_csv("df_final.csv")

cores_regiao = {"Norte":"#59A14F","Nordeste":"#F28E2B","Centro-Oeste":"#4C78A8","Sudeste":"#9C6ADE","Sul":"#2CB1BC"}

st.set_page_config(layout="wide")

st.title("Análise Educacional Brasileira")

st.markdown("Exploração interativa de indicadores socioeconômicos e desempenho educacional nos estados brasileiros.")

st.header("5.2.1 População, renda e desempenho educacional")

st.markdown("A variável população representa o tamanho das bolhas.")

df_final["pop_size"] = (df_final["populacao"]**0.8)/945

labels=df_final["sigla"].mask(df_final["sigla"].isin(["AP"]),"")

fig = px.scatter(df_final,x="renda",y="desempenho",size="pop_size",color="regiao",hover_name="estado",text=labels,size_max=28,opacity=0.60,color_discrete_map=cores_regiao,template="plotly_white",title="População, renda e desempenho educacional")

fig.update_layout(xaxis_title="Renda domiciliar per capita (R$)",yaxis_title="Desempenho",xaxis=dict(range=[920,3507]))

fig.update_traces(textposition="top center",textfont=dict(size=9.0),marker=dict(line=dict(width=1,color="white")))

st.plotly_chart(fig,use_container_width=True)

st.header("5.2.2 Pobreza, renda e desempenho")

st.markdown("O tamanho das bolhas representa o desempenho educacional.")

df_final["desempenho_size"] = ((df_final["desempenho"] - df_final["desempenho"].min()) ** 1.5) * 4.5 + 13

labels=df_final["sigla"].mask(df_final["sigla"].isin(["PE","AM","BA","MT","ES"]),"")

fig = px.scatter(df_final,x="renda",y="pobreza",size="desempenho_size",color="regiao",hover_name="estado",text=labels,size_max=28,opacity=0.66,color_discrete_map=cores_regiao,template="plotly_white",title="Pobreza, renda e desempenho educacional")

fig.update_yaxes(autorange="reversed")

fig.update_layout(xaxis_title="Renda domiciliar per capita (R$)",yaxis_title="Taxa de pobreza (%)",xaxis=dict(range=[920,3507]))

fig.update_traces(textposition="top center",textfont=dict(size=10.3),marker=dict(line=dict(width=1,color="white")))

st.plotly_chart(fig,use_container_width=True)

st.header("5.2.3 Desigualdade, renda e desempenho")

st.markdown("O tamanho das bolhas representa o desempenho educacional.")

labels=df_final["sigla"].mask(df_final["sigla"].isin(["PB","AM","PE","SE","ES"]),"")

fig = px.scatter(df_final,x="renda",y="gini",size="desempenho_size",color="regiao",hover_name="estado",text=labels,size_max=27,opacity=0.58,color_discrete_map=cores_regiao,template="plotly_white",title="Desigualdade, renda e desempenho educacional")

fig.update_yaxes(autorange="reversed")

fig.update_layout(xaxis_title="Renda domiciliar per capita (R$)",yaxis_title="Índice de Gini",xaxis=dict(range=[920,3507]),legend_title="")

fig.update_traces(textposition="top center",textfont=dict(size=10.5),marker=dict(line=dict(width=1,color="white")))

st.plotly_chart(fig,use_container_width=True)
