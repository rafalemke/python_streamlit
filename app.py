import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number, get_rec_estado, get_rec_month, get_rec_categoria, get_vendedores
from charts import create_rec_estado_bar_chart, create_rec_month_line_chart, create_rec_categoria_bar_chart, create_vendedores_bar_chart, create_vendas_vendedores_bar_chart, create_rec_estado_map_chart

st.set_page_config(layout='wide')
st.title('Análise de Vendas :chart_with_upwards_trend:')

st.sidebar.title('Filtro de Vendedor')

filtro_vendedor = st.sidebar.multiselect('Escolha o vendedor', df['Vendedor'].unique())

df_filtered = df.copy()
if filtro_vendedor:
    df_filtered = df_filtered[df_filtered['Vendedor'].isin(filtro_vendedor)]

# Use the filtered DataFrame to create the derived DataFrames
df_rec_estado = get_rec_estado(df_filtered)
df_rec_month = get_rec_month(df_filtered)
df_rec_categoria = get_rec_categoria(df_filtered)
df_vendedores = get_vendedores(df_filtered)

tab1, tab2, tab3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with tab1:
    st.dataframe(df_filtered)

with tab2:
    column1, column2 = st.columns(2)
    with column1:
        st.metric('Receita Total', format_number(df_filtered['Preço'].sum(), 'R$'))
        st.plotly_chart(create_rec_estado_bar_chart(df_rec_estado), use_container_width=True)
        st.plotly_chart(create_rec_categoria_bar_chart(df_rec_categoria), use_container_width=True)
        
    with column2:
        st.metric('Quantidade de Vendas', df_filtered.shape[0])
        st.plotly_chart(create_rec_month_line_chart(df_rec_month), use_container_width=True)
        st.plotly_chart(create_rec_estado_map_chart(df_rec_estado), use_container_width=True)

with tab3:
    column1, column2 = st.columns(2)
    with column1:
        st.plotly_chart(create_vendedores_bar_chart(df_vendedores), use_container_width=True)
    with column2:
        st.plotly_chart(create_vendas_vendedores_bar_chart(df_vendedores), use_container_width=True)