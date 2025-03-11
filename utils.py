import pandas as pd
import streamlit as st
import time

def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

def get_rec_estado(df):
    df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
    df_rec_estado = df.drop_duplicates(
        subset='Local da compra')[
            ['Local da compra', 'lat', 'lon']
        ].merge(
            df_rec_estado, 
            left_on='Local da compra', 
            right_index=True
        ).sort_values('Preço', ascending=False)
    return df_rec_estado

def get_rec_month(df):
    df_rec_month = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))[['Preço']].sum().reset_index()
    df_rec_month['Ano'] = df_rec_month['Data da Compra'].dt.year
    df_rec_month['Mês'] = df_rec_month['Data da Compra'].dt.month_name()
    return df_rec_month

def get_rec_categoria(df):
    df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False).reset_index()
    return df_rec_categoria

def get_vendedores(df):
    df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
    return df_vendedores


# Função para converter em csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')


def mensagem_sucesso():
    success = st.success(
        'Dados exportados com sucesso!',
        icon="✅"
        )
    time.sleep(2)
    success.empty()