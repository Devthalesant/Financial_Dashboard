from pymongo import MongoClient, UpdateOne
import pandas as pd
import re
import plotly.express as px



def grafico_barras_vendas(new_df,year_optinos):

  base = new_df.loc[new_df["ANO"] isin(year_optinos)]
  sell_groupby = base.groupby(["PERIODO"]).agg({"TOTAL LÍQUIDO ITEM" : "sum"}).reset_index()
  sell_grafic = px.bar(sell_groupby, x="PERIODO" , y="TOTAL LÍQUIDO ITEM",title = f"Gráfico de Vendas 2025")

  return sell_grafic
