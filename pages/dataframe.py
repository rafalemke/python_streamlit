import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
                'Selecione as colunas', 
                df.columns,
                df.columns
                )

st.sidebar.title('Filtro de Colunas')

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
    
query = '''
    `Categoria do Produto` in @filtro_categoria and \
    @preco[0] <= `Preço` <= @preco[1] and \
    @data[0] <= `Data da Compra` <= @data[1]
'''

filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas.')

st.dataframe(filtro_dados)

st.markdown('Escreva o nome do arquivo')

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('', label_visibility='collapsed')
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )
