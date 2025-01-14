from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
from auxiliar.groupby import *
import streamlit as st
import pandas as pd
import re
import plotly.express as px

st.title("Visão Geral - teeste")

year_optinos = [2024, 2025]
st.pills("Ano de Análise :",year_optinos, selection_mode = "multi" )

# # Getting a dataframe of billchaeges
# billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")

database = "database/billcharges10jan.csv"

pd.read_csv(database)

billcharges_df = pd.read_csv(database)

new_df = treating_values(billcharges_df)

# para gráfico no ploty
grafico = grafico_barras_vendas(new_df)
st.plotly_chart(grafico)

## tratar dados, salvar em csv, importar e trabalhar em cima disso para seguir com o deenvolvimento
# os dados ja estão na pasta base de dados do git. como eu puxo eles para esse bloco de código? não lebro
