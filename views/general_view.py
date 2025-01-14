from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
from auxiliar.groupby import *
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visão Geral - teste")

# Opções de anos a serem selecionadas
year_options = [2024, 2025]
selected_years = st.multiselect("Ano de Análise:", year_options, default=year_options)

# Carregar o DataFrame
database = "/content/Financial_Dashboard/bases/billcharges10jan.csv"
billcharges_df = pd.read_csv(database)

# Criar a coluna ANO se não existir
if 'DATA' in billcharges_df.columns:
    billcharges_df['ANO'] = pd.to_datetime(billcharges_df['DATA']).dt.year

# Usar o DataFrame já tratado
new_df = billcharges_df

# Exibir o DataFrame
st.dataframe(new_df)

# Gerar o gráfico
if selected_years:
    grafico = grafico_barras_vendas(new_df, selected_years)
    st.plotly_chart(grafico)
else:
    st.write("Por favor, selecione um ou mais anos para visualizar o gráfico.")
