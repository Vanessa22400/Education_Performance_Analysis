import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(
    page_title="Análise Educacional Brasileira",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

df_final = pd.read_csv(BASE_DIR / "df_final.csv")

cores_regiao = {
    "Norte":"#59A14F",
    "Nordeste":"#F28E2B",
    "Centro-Oeste":"#4C78A8",
    "Sudeste":"#9C6ADE",
    "Sul":"#2CB1BC"
}

cores_prioridade = {
    "Alta prioridade": "#D95F02",
    "Prioridade moderada": "#F2CF5B",
    "Menor prioridade": "#4C78A8"
}

st.sidebar.title("Navegação")

st.sidebar.markdown("""
- Introdução
- 5. Análise Exploratória
- 6. Regressão Linear
- 7. Clustering
- 8. Priorização
- 9. Piloto Educacional
- 10. Simulação
- 11. Conclusão
""")

st.title("Dados e Educação: Priorização de Intervenções Educacionais no Brasil")

st.markdown("""
### Análise socioeducacional baseada em indicadores públicos e priorização orientada por dados

Este projeto explora relações entre indicadores socioeconômicos e desempenho educacional nos estados brasileiros, utilizando análises exploratórias, regressão linear, clustering e priorização de intervenção.

Os dados utilizados foram obtidos principalmente a partir do SAEB (INEP), IBGE/SIDRA, PNAD Contínua e Censo Demográfico.
""")

st.caption("Projeto de portfólio em Data Science aplicado ao contexto educacional brasileiro.")

st.divider()

# =========================================================
# 5
# =========================================================

st.header("5. Análise exploratória de indicadores socioeducacionais")

st.markdown("""
A análise exploratória busca identificar padrões, desigualdades regionais e relações entre indicadores educacionais e socioeconômicos nos estados brasileiros.
""")

# =========================================================
# 5.1
# =========================================================

st.subheader("5.1 Distribuição do desempenho educacional")

st.markdown("""
Inicialmente, foi analisada a distribuição do desempenho educacional entre os estados e regiões brasileiras.
""")

# =========================================================
# 5.1.1
# =========================================================

st.markdown("### 5.1.1 Comparação do desempenho educacional por estado")

st.markdown("""
O gráfico abaixo apresenta a distribuição do desempenho educacional entre os estados brasileiros em ordem crescente, com destaque visual para as diferentes regiões do país.
""")

df_plot = df_final.sort_values(by="desempenho")

fig = px.bar(
    df_plot,
    x="sigla",
    y="desempenho",
    color="regiao",
    color_discrete_map=cores_regiao,
    hover_data={
        "estado": True,
        "regiao": True,
        "desempenho":":.2f",
        "sigla":False
    },
    template="plotly_white",
    title="Desempenho educacional por estado"
)

fig.update_layout(
    xaxis_title="Estado",
    yaxis_title="Desempenho médio",
    legend_title="",
    xaxis={
        'categoryorder':'total ascending',
        'tickfont':dict(size=10)
    }
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**Destaques observados:**

- Ceará apresentou o maior desempenho médio da análise.
- Regiões Norte e Nordeste concentraram menores desempenhos médios.
- Sul apresentou maior homogeneidade entre os estados.
""")

# =========================================================
# 5.1.2
# =========================================================

st.markdown("### 5.1.2 Comparação regional do desempenho educacional")

st.markdown("""
O boxplot abaixo permite comparar a distribuição do desempenho educacional entre as regiões brasileiras.
""")

fig = px.box(
    df_final,
    x="regiao",
    y="desempenho",
    color="regiao",
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="Distribuição regional do desempenho educacional"
)

fig.update_layout(
    xaxis_title="",
    yaxis_title="Desempenho médio",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 5.1.3
# =========================================================

st.markdown("### 5.1.3 Diferenças entre redes pública e privada")

st.markdown("""
Foi realizada uma comparação entre os desempenhos médios das redes pública e privada nos estados brasileiros.
""")

df_redes = df_final[
    ["estado","sigla","desempenho","desempenho_privado"]
].copy()

df_redes = df_redes.sort_values(by="desempenho")

df_redes = df_redes.melt(
    id_vars=["estado","sigla"],
    value_vars=["desempenho","desempenho_privado"],
    var_name="rede",
    value_name="desempenho_medio"
)

df_redes["rede"] = df_redes["rede"].replace({
    "desempenho":"Rede pública",
    "desempenho_privado":"Rede privada"
})

fig = px.bar(
    df_redes,
    x="sigla",
    y="desempenho_medio",
    color="rede",
    barmode="group",
    template="plotly_white",
    title="Desempenho médio das redes pública e privada por estado",
    color_discrete_map={
        "Rede pública":"#7FCDBB",
        "Rede privada":"#225EA8"
    }
)

fig.update_layout(
    xaxis_title="Estado",
    yaxis_title="Desempenho médio",
    legend_title="",
    bargap=0.18
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
A rede privada apresentou desempenho superior em todos os estados analisados, embora os gaps variem significativamente entre as regiões.
""")

# =========================================================
# 5.2
# =========================================================

st.subheader("5.2 Contexto socioeconômico e desempenho educacional")

st.markdown("""
As visualizações abaixo foram inspiradas no modelo Gapminder, integrando múltiplos indicadores em uma única análise.
""")

# =========================================================
# 5.2.1
# =========================================================

st.markdown("### 5.2.1 População, renda e desempenho educacional")

st.markdown("""
Foi analisada a relação entre renda domiciliar per capita e desempenho educacional.
""")

st.caption("O tamanho das bolhas representa a população dos estados.")

df_final["pop_size"] = (df_final["populacao"]**0.8)/945

labels = df_final["sigla"].mask(
    df_final["sigla"].isin(["AP"]),
    ""
)

fig = px.scatter(
    df_final,
    x="renda",
    y="desempenho",
    size="pop_size",
    color="regiao",
    hover_name="estado",
    text=labels,
    size_max=28,
    opacity=0.60,
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="População, renda e desempenho educacional"
)

fig.update_layout(
    xaxis_title="Renda domiciliar per capita (R$)",
    yaxis_title="Desempenho",
    xaxis=dict(range=[920,3507]),
    legend_title=""
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=9),
    marker=dict(
        line=dict(width=1,color="white")
    )
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 5.2.2
# =========================================================

st.markdown("### 5.2.2 Pobreza, renda e desempenho")

st.markdown("""
Foi analisada a relação entre renda domiciliar per capita, taxa de pobreza e desempenho educacional.
""")

st.caption("O tamanho das bolhas representa o desempenho educacional.")

df_final["desempenho_size"] = (
    ((df_final["desempenho"] - df_final["desempenho"].min()) ** 1.5)
    * 4.5 + 13
)

labels = df_final["sigla"].mask(
    df_final["sigla"].isin(["PE","AM","BA","MT","ES"]),
    ""
)

fig = px.scatter(
    df_final,
    x="renda",
    y="pobreza",
    size="desempenho_size",
    color="regiao",
    hover_name="estado",
    text=labels,
    size_max=28,
    opacity=0.66,
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="Pobreza, renda e desempenho educacional"
)

fig.update_yaxes(autorange="reversed")

fig.update_layout(
    xaxis_title="Renda domiciliar per capita (R$)",
    yaxis_title="Taxa de pobreza (%)",
    xaxis=dict(range=[920,3507]),
    legend_title=""
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10.3),
    marker=dict(
        line=dict(width=1,color="white")
    )
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 5.2.3
# =========================================================

st.markdown("### 5.2.3 Desigualdade, renda e desempenho")

st.markdown("""
Foi analisada a relação entre desigualdade de renda, desempenho educacional e renda domiciliar per capita.
""")

labels = df_final["sigla"].mask(
    df_final["sigla"].isin(["PB","AM","PE","SE","ES"]),
    ""
)

fig = px.scatter(
    df_final,
    x="renda",
    y="gini",
    size="desempenho_size",
    color="regiao",
    hover_name="estado",
    text=labels,
    size_max=27,
    opacity=0.58,
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="Desigualdade, renda e desempenho educacional"
)

fig.update_yaxes(autorange="reversed")

fig.update_layout(
    xaxis_title="Renda domiciliar per capita (R$)",
    yaxis_title="Índice de Gini",
    xaxis=dict(range=[920,3507]),
    legend_title=""
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10.5),
    marker=dict(
        line=dict(width=1,color="white")
    )
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 5.3
# =========================================================

st.subheader("5.3 Urbanização e desempenho educacional")

st.markdown("""
Foi analisada a relação entre urbanização e desempenho educacional nos estados brasileiros.
""")

fig = px.scatter(
    df_final,
    x="desempenho",
    y="urbanizacao",
    color="regiao",
    hover_name="estado",
    text="sigla",
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="Urbanização e desempenho educacional"
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=11),
    marker=dict(
        size=10,
        line=dict(width=1,color="white")
    )
)

fig.update_layout(
    xaxis_title="Desempenho médio",
    yaxis_title="Taxa de urbanização (%)",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 5.4
# =========================================================

st.subheader("5.4 Escolaridade da população adulta e desempenho educacional")

st.markdown("""
Foi analisada a relação entre escolaridade da população adulta e desempenho educacional.
""")

fig = px.scatter(
    df_final,
    x="desempenho",
    y="escolaridade",
    color="regiao",
    hover_name="estado",
    text="sigla",
    color_discrete_map=cores_regiao,
    template="plotly_white",
    title="Escolaridade da população adulta e desempenho educacional"
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10),
    marker=dict(
        size=12,
        line=dict(width=1,color="white")
    )
)

fig.update_layout(
    xaxis_title="Desempenho médio",
    yaxis_title="Escolaridade da população adulta (%)",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 6
# =========================================================

st.divider()

st.header("6. Relação entre variáveis e regiões")

st.markdown("""
Foi utilizada regressão linear para investigar tendências entre indicadores socioeconômicos e desempenho educacional.
""")

# =========================================================
# 6.1
# =========================================================

st.subheader("6.1 Renda e desempenho educacional")

coef_regiao = {}

for r in df_final["regiao"].unique():

    df_r = df_final[df_final["regiao"] == r]

    X = df_r[["renda"]]

    y = df_r["desempenho"]

    coef_regiao[r] = LinearRegression().fit(X,y).coef_[0]

df_final["legenda"] = df_final["regiao"].map(
    lambda x: f"{x}: {coef_regiao[x]:.4f}"
)

fig = px.scatter(
    df_final,
    x="renda",
    y="desempenho",
    color="legenda",
    text="sigla",
    trendline="ols",
    hover_name="estado",
    template="plotly_white",
    color_discrete_map={
        f"{k}: {coef_regiao[k]:.4f}":v
        for k,v in cores_regiao.items()
    },
    title="Renda domiciliar per capita e desempenho educacional"
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10.5)
)

fig.update_layout(
    xaxis_title="Renda domiciliar per capita (R$)",
    yaxis_title="Desempenho médio",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 6.2
# =========================================================

st.subheader("6.2 Pobreza e desempenho educacional")

coef_regiao = {}

for r in df_final["regiao"].unique():

    df_r = df_final[df_final["regiao"] == r]

    X = df_r[["pobreza"]]

    y = df_r["desempenho"]

    coef_regiao[r] = LinearRegression().fit(X,y).coef_[0]

df_final["legenda"] = df_final["regiao"].map(
    lambda x: f"{x}: {coef_regiao[x]:.4f}"
)

fig = px.scatter(
    df_final,
    x="pobreza",
    y="desempenho",
    color="legenda",
    text="sigla",
    trendline="ols",
    hover_name="estado",
    template="plotly_white",
    color_discrete_map={
        f"{k}: {coef_regiao[k]:.4f}":v
        for k,v in cores_regiao.items()
    },
    title="Taxa de pobreza e desempenho educacional"
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10.5)
)

fig.update_layout(
    xaxis_title="Taxa de pobreza (%)",
    yaxis_title="Desempenho médio",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 7
# =========================================================

st.divider()

st.header("7. Segmentação de contextos educacionais (Clustering)")

st.markdown("""
Foi aplicada uma técnica de clustering para identificar grupos de estados com perfis socioeconômicos e educacionais semelhantes.
""")

X = df_final[
    ["desempenho","renda","pobreza","gini","urbanizacao"]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

df_final["cluster"] = kmeans.fit_predict(X_scaled)

df_final["perfil_cluster"] = df_final["cluster"].map({
    0:"Menor vulnerabilidade",
    1:"Maior vulnerabilidade",
    2:"Contextos intermediários"
})

df_final["indice_socioeconomico"] = (
    -df_final["gini"]
    -df_final["pobreza"]
    +df_final["urbanizacao"]
)

fig = px.scatter(
    df_final,
    x="indice_socioeconomico",
    y="desempenho",
    color="perfil_cluster",
    symbol="perfil_cluster",
    text=df_final["sigla"].mask(
        df_final["sigla"].isin(["RO"]),
        ""
    ),
    hover_name="estado",
    template="plotly_white",
    title="Agrupamento socioeconômico e desempenho educacional",
    color_discrete_map={
        "Menor vulnerabilidade":"#4f81bd",
        "Maior vulnerabilidade":"#c051a2",
        "Contextos intermediários":"#f4b942"
    }
)

fig.update_traces(
    textposition="top center",
    textfont=dict(size=10),
    marker=dict(
        size=10,
        line=dict(width=1,color="white")
    )
)

fig.update_layout(
    xaxis_title="Índice socioeconômico agregado",
    yaxis_title="Desempenho educacional",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 8
# =========================================================

st.divider()

st.header("8. Priorização de intervenção educacional")

st.markdown("""
Foi construído um indicador simplificado de prioridade de intervenção educacional.
""")

features = ["renda","pobreza","gini"]

scaler = StandardScaler()

df_scaled = pd.DataFrame(
    scaler.fit_transform(df_final[features]),
    columns=features
)

df_final["score_vulnerabilidade"] = (
    -(df_scaled["renda"] * 1.1)
    + (df_scaled["pobreza"] * 1.3)
    + (df_scaled["gini"] * 1.0)
)

desempenho_padronizado = StandardScaler().fit_transform(
    df_final[["desempenho"]]
)

df_final["prioridade_intervencao"] = (
    df_final["score_vulnerabilidade"]
    - desempenho_padronizado.flatten() * 2.5
)

def classificar_prioridade(valor):

    if valor >= 4.0:
        return "Alta prioridade"

    elif valor >= 0:
        return "Prioridade moderada"

    else:
        return "Menor prioridade"

df_final["faixa_prioridade"] = df_final[
    "prioridade_intervencao"
].apply(classificar_prioridade)

df_plot = df_final.sort_values(
    by="prioridade_intervencao",
    ascending=False
)

fig = px.bar(
    df_plot,
    x="estado",
    y="prioridade_intervencao",
    color="faixa_prioridade",
    color_discrete_map=cores_prioridade,
    template="plotly_white",
    title="Priorização de contextos para intervenção educacional",
    text="prioridade_intervencao"
)

fig.update_traces(
    texttemplate="%{text:.1f}",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Estado",
    yaxis_title="Prioridade de intervenção",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 9
# =========================================================

st.divider()

st.header("9. Proposta de piloto educacional orientado por dados")

st.markdown("""
Os resultados anteriores mostraram maior concentração de estados prioritários nas regiões Norte e Nordeste.
""")

top_prioridade = (
    df_final[
        ["estado","prioridade_intervencao"]
    ]
    .sort_values(
        by="prioridade_intervencao",
        ascending=False
    )
    .head(7)
)

st.dataframe(
    top_prioridade,
    use_container_width=True
)

# =========================================================
# 10
# =========================================================

st.divider()

st.header("10. Simulação de acompanhamento do piloto")

st.markdown("""
Foi construída uma simulação simplificada de evolução do desempenho educacional ao longo do tempo.
""")

df_piloto = pd.DataFrame({
    "estado":["Maranhão","Pará","Ceará"],
    "Ano 1":[234.4,238.8,264.6],
    "Ano 2":[238.5,241.5,265.0],
    "Ano 3":[242.0,244.2,266.0],
    "Ano 4":[245.5,247.0,267.0]
})

df_plot = df_piloto.melt(
    id_vars="estado",
    var_name="Ano",
    value_name="desempenho"
)

fig = px.line(
    df_plot,
    x="Ano",
    y="desempenho",
    color="estado",
    markers=True,
    template="plotly_white",
    title="Simulação de acompanhamento do piloto educacional",
    color_discrete_map={
        "Maranhão":"#3B82F6",
        "Pará":"#14B8A6",
        "Ceará":"#7C3AED"
    }
)

fig.update_layout(
    xaxis_title="Período de acompanhamento",
    yaxis_title="Desempenho educacional médio",
    legend_title="",
    yaxis_range=[220,280]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 11
# =========================================================

st.divider()

st.header("11. Conclusão")

st.markdown("""
Os resultados mostraram forte relação entre vulnerabilidade socioeconômica e desempenho educacional, com concentração de contextos prioritários principalmente nas regiões Norte e Nordeste.

Ao mesmo tempo, estados como Ceará demonstraram desempenho acima do esperado para contextos socioeconômicos semelhantes, sugerindo possível influência de fatores institucionais e políticas educacionais.

O projeto também demonstrou como dados públicos podem apoiar processos de priorização, monitoramento e tomada de decisão no contexto educacional brasileiro.
""")

st.caption("Fonte: SAEB/INEP, IBGE/SIDRA, PNAD Contínua e Censo Demográfico.")
