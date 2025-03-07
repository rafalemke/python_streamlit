import plotly.express as px
from utils import format_number

def create_rec_estado_bar_chart(df_rec_estado):
    chart = px.bar(
        df_rec_estado.head(7),
        x='Local da compra',
        y='Preço',
        text_auto=True,
        title='Receita por Estado'
    )
    chart.update_yaxes(
        # tickvals=df_rec_estado.head(7)['Preço'],
        ticktext=[format_number(val, 'R$') for val in df_rec_estado.head(7)['Preço']]
    )
    return chart

def create_rec_month_line_chart(df_rec_month):
    chart = px.line(
        df_rec_month,
        x='Mês',
        y='Preço',
        markers=True,
        range_y=(df_rec_month['Preço'].min() - 10000, df_rec_month['Preço'].max() + 10000),
        color='Ano',
        title='Receita por Mês'
    )
    return chart

def create_rec_categoria_bar_chart(df_rec_categoria):
    chart = px.bar(
        df_rec_categoria.head(7),
        x='Categoria do Produto',
        y='Preço',
        text_auto=True,
        title='Receita por Categoria'
    )
    chart.update_yaxes(
        # tickvals=df_rec_categoria.head(7)['Preço'],
        ticktext=[format_number(val, 'R$') for val in df_rec_categoria.head(7)['Preço']]
    )
    return chart

def create_vendedores_bar_chart(df_vendedores):
    chart = px.bar(
        df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
        x='sum',
        y=df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
        text_auto=True,
        title='Receita por Vendedor'
    )
    return chart

def create_vendas_vendedores_bar_chart(df_vendedores):
    chart = px.bar(
        df_vendedores[['count']].sort_values('count', ascending=False).head(7),
        x='count',
        y=df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
        text_auto=True,
        title='Vendas por Vendedor'
    )
    return chart

def create_rec_estado_map_chart(df_rec_estado):
    chart = px.scatter_geo(
        df_rec_estado,
        lat='lat',
        lon='lon',
        scope='south america',
        size='Preço',
        template='plotly_dark',
        color='Preço',
        hover_name='Local da compra',
        hover_data={'lat': False, 'lon': False},
        size_max=60,
        projection='natural earth',
        title='Receita por Estado'
    )
    return chart