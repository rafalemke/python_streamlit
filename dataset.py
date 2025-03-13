import json
import pandas as pd
import os

# Construir o caminho dinamicamente
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data', 'vendas.json')

# Abrir o arquivo usando o caminho dinâmico
with open(file_path, 'r') as file:
    data = json.load(file)

df = pd.DataFrame.from_dict(data)
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

# print(df.columns)