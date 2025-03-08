import streamlit as st
from dataset import df

st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
                'Selecione as colunas', 
                df.columns,
                df.columns
                )

st.sidebar.title('Filtro de Vendedor')

with st.sidebar.expander('Categoria do Produto'):
    filtro_categoria = st.multiselect(
                'Escolha a categoria',
                df['Categoria do Produto'].unique(),
                df['Categoria do Produto'].unique()
                )
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
                'Escolha o preço do produto',
                float(df['Preço'].min()),
                float(df['Preço'].max()),
                (float(df['Preço'].min()), float(df['Preço'].max()))
                )
    
with st.sidebar.expander('Data da Compra'):
    data = st.date_input(
        'Escolha a data da compra', 
        (df['Data da Compra'].min(), 
        df['Data da Compra'].max())
        )
st.dataframe(df)
