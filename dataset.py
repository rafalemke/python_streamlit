import json
import pandas as pd

file = open(r'C:\Users\Rafa_\Documents\python_streamlit\dados\vendas.json', 'r')

data = json.load(file)

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

# print(df.columns)

file.close()