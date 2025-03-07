from dataset import df
import pandas as pd



def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'



# RECEITA POR ESTADO
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(
    subset='Local da compra')[[
        'Local da compra', 
        'lat', 
        'lon']].merge(df_rec_estado, 
                    left_on='Local da compra', 
                    right_index=True
                    ).sort_values('Preço', ascending=False)


# RECEITA POR MES
df_rec_month = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))[['Preço']].sum().reset_index()
df_rec_month['Ano'] = df_rec_month['Data da Compra'].dt.year
df_rec_month['Mês'] = df_rec_month['Data da Compra'].dt.month_name()


# RECEITA POR CATEGORIA
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False).reset_index()

