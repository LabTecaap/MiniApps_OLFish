import pandas as pd
import csv

def carregar_dados(arquivo):
  return pd.read_csv(arquivo)

def inserir_dados(arquivo,dados):
  df = pd.DataFrame.from_dict(dados)
  df.to_csv(arquivo, mode='a', header=False, index=False)