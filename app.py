import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o conjunto de dados a partir do arquivo local
df = pd.read_csv("StudentsPerformance.csv")

# Exibir o título e a descrição do dashboard
st.title("Dashboard - Desempenho dos Alunos em Exames")
st.write("Este dashboard visualiza o desempenho dos alunos em exames com base em diferentes fatores como gênero, preparação para os exames, e tempo de estudo.")

# Exibir as primeiras linhas do DataFrame
st.write("Primeiras linhas dos dados:")
st.write(df.head())

# 1. Analisando a distribuição das notas
st.subheader("Distribuição das notas por gênero")
fig, ax = plt.subplots()
sns.boxplot(x="gender", y="math score", data=df, ax=ax)
plt.title("Notas de Matemática por Gênero")
st.pyplot(fig)

# 2. Comparar a média das notas de Matemática, Leitura e Escrita
st.subheader("Média das notas por disciplina")
media_notas = df[['math score', 'reading score', 'writing score']].mean()
st.write(media_notas)

# 3. Análise de correlação entre as notas
st.subheader("Correlação entre as notas")
fig, ax = plt.subplots()
sns.heatmap(df[['math score', 'reading score', 'writing score']].corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
plt.title("Correlação entre as notas")
st.pyplot(fig)

# 4. Analisando o impacto da preparação no desempenho
st.subheader("Desempenho com base na preparação para o exame")
fig, ax = plt.subplots()
sns.boxplot(x="test preparation course", y="math score", data=df, ax=ax)
plt.title("Notas de Matemática por Preparação para o Exame")
st.pyplot(fig)
