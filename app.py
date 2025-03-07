import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from charts import rec_estado_chart, rec_month_chart, rec_estado_bar_chart, rec_cat_bar_chart


st.set_page_config(layout='wide')
st.title('Análise de Vendas :chart_with_upwards_trend:')


tab1, tab2, tab3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with tab1:
    st.dataframe(df)

with tab2:
    column1, column2 = st.columns(2)
    with column1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(rec_estado_chart, use_container_width=True)
        st.plotly_chart(rec_estado_bar_chart, use_container_width=True)
        
    with column2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0], 'R$'))
        st.plotly_chart(rec_month_chart, use_container_width=True)
        st.plotly_chart(rec_cat_bar_chart, use_container_width=True)