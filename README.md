# Dados e Educação: Priorização de Intervenções Educacionais no Brasil

Análise socioeducacional orientada por dados para identificação de vulnerabilidades, priorização de intervenções educacionais e apoio à tomada de decisão em contextos educacionais brasileiros.

---

![Gapminder Educacional](images/gapminder_educacao.png)

*Visualização inspirada na abordagem do Gapminder para análise de relações entre desenvolvimento social, vulnerabilidade socioeconômica e desempenho educacional.*

---

## Visão Geral

**Dataset:** indicadores educacionais e socioeconômicos dos estados brasileiros  
**Fontes:** IBGE, SAEB / INEP e indicadores educacionais públicos brasileiros  
**Técnicas:** análise exploratória, regressão linear, clusterização, priorização educacional e simulação de acompanhamento  
**Principal insight:** estados com contextos socioeconômicos semelhantes apresentaram desempenhos educacionais muito diferentes.  
Enquanto o Ceará apresentou o maior desempenho da rede pública, estados como Maranhão, Roraima e Paraíba apresentaram os maiores níveis relativos de prioridade de intervenção educacional.

---

## Contexto do Projeto

Desigualdades educacionais no Brasil estão fortemente associadas a fatores socioeconômicos e regionais. No entanto, estados com contextos semelhantes podem apresentar desempenhos educacionais significativamente diferentes.

O projeto integra indicadores educacionais e socioeconômicos públicos para explorar relações entre desempenho educacional, vulnerabilidade social e priorização de intervenções educacionais nos estados brasileiros.

A proposta busca demonstrar como análises orientadas por dados podem apoiar processos de priorização, monitoramento e tomada de decisão em políticas públicas educacionais.

---

## Objetivos

- identificar relações entre indicadores socioeconômicos e desempenho educacional
- comparar diferenças educacionais entre estados e regiões
- analisar desigualdades entre redes pública e privada
- construir um indicador de vulnerabilidade socioeconômica
- desenvolver um modelo simplificado de priorização educacional
- identificar contextos com maior potencial relativo para intervenção
- simular acompanhamento de um piloto educacional orientado por dados

---

## Dataset

O projeto utiliza indicadores educacionais e socioeconômicos públicos dos estados brasileiros, integrando dados relacionados a desempenho educacional, renda, pobreza, desigualdade social e urbanização.

### Principais variáveis analisadas

- desempenho educacional médio da rede pública
- desempenho médio da rede privada
- renda
- pobreza
- índice de Gini
- escolaridade
- urbanização
- população

### Fontes de dados

- IBGE
- SAEB / INEP
- indicadores educacionais públicos brasileiros

---

## Metodologia

A análise foi estruturada nas seguintes etapas:

1. Integração e preparação dos dados
2. Análise exploratória (EDA)
3. Visualizações inspiradas no Gapminder
4. Regressões lineares
5. Comparações regionais
6. Clusterização de estados
7. Construção do score de vulnerabilidade socioeconômica
8. Modelo de priorização de intervenção educacional
9. Proposta de piloto educacional orientado por dados
10. Simulação de acompanhamento educacional

---

## Principais Resultados

- Estados das regiões **Norte** e **Nordeste** concentraram os maiores níveis relativos de vulnerabilidade socioeconômica e prioridade de intervenção educacional.

- Indicadores socioeconômicos apresentaram relação relevante com o desempenho educacional da rede pública, mas não explicaram isoladamente todas as diferenças observadas entre os estados.

- Estados como **Ceará**, **Piauí** e **Pernambuco** apresentaram desempenho educacional relativamente superior ao observado em outros contextos socioeconômicos semelhantes.

- O **Ceará** apresentou o maior desempenho médio da rede pública da análise (**264.6 pontos**), destacando-se mesmo em uma região com elevados níveis relativos de vulnerabilidade social.

- Estados com indicadores socioeconômicos mais favoráveis, como o **Distrito Federal**, não apresentaram desempenho educacional proporcionalmente superior quando comparados a outros estados analisados.

- Todos os estados apresentaram desempenho superior na rede privada em relação à rede pública.

- As maiores diferenças entre redes ocorreram em **Rio Grande do Norte (+26.5%)** e **Sergipe (+23.9%)**, enquanto **Paraná (+4.3%)** e **Ceará (+7.5%)** apresentaram as menores diferenças relativas.

- A análise mostrou que indicadores socioeconômicos tendem a seguir padrões regionais relativamente semelhantes, enquanto o desempenho educacional variou significativamente entre estados de uma mesma região.

- **Santa Catarina** apresentou um dos resultados mais equilibrados da análise, combinando elevado desempenho educacional (**261.8 pontos**), baixa pobreza (**12.6%**) e menor desigualdade social relativa (**Gini = 0.418**).

---

## Comparação entre Redes Pública e Privada

Além da análise da rede pública, o projeto também investigou diferenças de desempenho entre redes pública e privada nos estados brasileiros.

![Comparação entre Redes](images/publico_privado.png)

A comparação mostrou que:

- todos os estados apresentaram desempenho superior na rede privada
- as diferenças entre redes variaram significativamente entre os estados
- não foi observado um padrão regional único para as maiores diferenças

Estados como **Rio Grande do Norte**, **Sergipe** e **Minas Gerais** apresentaram os maiores gaps relativos entre as redes, enquanto **Paraná** e **Ceará** apresentaram diferenças proporcionalmente menores.

---

## Clusterização e Perfis Regionais

A clusterização permitiu identificar diferentes perfis socioeconômicos e educacionais entre os estados brasileiros.

![Clusterização](images/clusterizacao.png)

Os resultados reforçaram que:

- estados de uma mesma região podem apresentar desempenhos educacionais bastante diferentes
- indicadores socioeconômicos não explicam isoladamente os resultados educacionais
- análises multidimensionais são importantes para apoiar decisões de intervenção educacional

---

## Priorização de Intervenção Educacional

A partir do cruzamento entre vulnerabilidade socioeconômica e desempenho educacional, foi desenvolvido um indicador simplificado de priorização educacional.

O modelo permitiu identificar estados com maior potencial relativo para intervenções direcionadas.

![Mapa de Priorização](images/mapa_priorizacao.png)

### Estados classificados como maior prioridade relativa

- Maranhão
- Roraima
- Paraíba
- Bahia
- Rio Grande do Norte
- Sergipe
- Pará

---

## Proposta de Piloto Educacional

Com base nos resultados observados ao longo da análise, foi construída uma proposta simplificada de piloto educacional orientado por dados.

A proposta possui foco principalmente em:

- estados classificados como maior prioridade relativa
- acompanhamento contínuo de indicadores educacionais
- monitoramento de desempenho
- apoio pedagógico e tecnologia educacional

O projeto também utilizou o **Ceará** como importante referência comparativa devido ao desempenho educacional acima da tendência observada para contextos socioeconômicos semelhantes.

---

## Simulação de Acompanhamento

Foi desenvolvida uma simulação simplificada de acompanhamento educacional ao longo de quatro anos.

A proposta buscou ilustrar como indicadores educacionais poderiam apoiar:

- monitoramento contínuo
- avaliação de impacto
- acompanhamento de desempenho
- priorização educacional orientada por dados

Estados utilizados na simulação:

- Maranhão
- Pará
- Ceará (referência comparativa)

![Simulação do Piloto](images/simulacao_piloto.png)

---

## Aplicações Práticas

A proposta desenvolvida ao longo do projeto pode contribuir para:

- priorização de políticas públicas educacionais
- monitoramento de indicadores educacionais
- avaliação simplificada de impacto
- identificação de contextos vulneráveis
- acompanhamento de metas educacionais
- apoio à tomada de decisão orientada por dados

---

## Limitações

Algumas limitações devem ser consideradas:

- utilização de dados agregados por estado
- ausência de séries temporais mais longas
- limitação de indicadores disponíveis em algumas bases públicas
- utilização de simulações simplificadas no piloto educacional

---

## Próximos Passos

Possíveis expansões futuras incluem:

- análises em nível municipal
- integração com dados de evasão escolar
- utilização de séries históricas
- modelos preditivos para risco de evasão
- integração com indicadores reais de acompanhamento escolar
- modelos de séries temporais educacionais
- análise de políticas públicas específicas
- dashboards interativos de monitoramento

---

## Estrutura do Projeto

```bash
.
├── data
├── notebooks
├── images
├── requirements.txt
└── README.md
```

---

## Pipeline Analítico

```text
Coleta de dados
→ análise exploratória
→ regressão linear
→ clusterização
→ score de vulnerabilidade
→ priorização educacional
→ simulação de acompanhamento
→ aplicações práticas
```

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Plotly
- Scikit-learn
- GeoPandas
- Matplotlib

---

## Conclusão

Este projeto buscou demonstrar como análises de dados podem apoiar processos de priorização, monitoramento e avaliação em contextos educacionais complexos.

Os resultados mostraram que fatores socioeconômicos possuem relação importante com o desempenho educacional, mas não explicam isoladamente as diferenças observadas entre os estados brasileiros.

Casos como o **Ceará** reforçam a importância de análises multidimensionais e da avaliação individual dos contextos educacionais, enquanto estados como **Maranhão**, **Roraima** e **Paraíba** destacaram-se entre os maiores níveis relativos de prioridade para intervenção educacional.

Mais do que produzir previsões, o projeto busca demonstrar como dados públicos podem apoiar decisões educacionais mais direcionadas, transparentes e orientadas por evidências.
