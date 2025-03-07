import plotly.express as px
from utils import df_rec_estado, df_rec_month, format_number, df_rec_categoria


rec_estado_chart = px.scatter_geo(
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

rec_month_chart = px.line(
    df_rec_month,
    x='Mês',
    y='Preço',
    markers=True,
    range_y= (df_rec_month['Preço'].min() - 10000, df_rec_month['Preço'].max() + 10000),
    color='Ano',
    title='Receita por Mês'
)

rec_estado_bar_chart = px.bar(
    df_rec_estado.head(7),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Receita por Estado',
)

# Format the y-axis values using format_number
rec_estado_bar_chart.update_yaxes(tickformat=',', tickprefix='R$')

rec_estado_bar_chart.update_yaxes(
    # tickvals=df_rec_estado.head(7)['Preço'],
    ticktext=[format_number(val, 'R$') for val in df_rec_estado.head(7)['Preço']]
)


rec_cat_bar_chart = px.bar(
    df_rec_categoria.head(7),
    x='Categoria do Produto',
    y='Preço',
    text_auto=True,
    title='Receita por Categoria',
)
rec_cat_bar_chart.update_yaxes(
    # tickvals=df_rec_estado.head(7)['Preço'],
    ticktext=[format_number(val, 'R$') for val in df_rec_categoria.head(7)['Preço']]
)