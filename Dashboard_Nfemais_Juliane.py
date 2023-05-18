import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from datetime import datetime
from collections import Counter
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#Tratamento e gráficos
df1 = pd.read_csv('blaster.csv')
df_novo = df1[df1['plano'] == 'Gratuito']
df1 = pd.DataFrame(df_novo)
df1.drop(df1.columns[[0, 1, 5, 6]], axis=1, inplace=True)
df1['ultimo_acesso'] = pd.to_datetime(df1['ultimo_acesso'], format='%d/%m/%Y %H:%M:%S')
df1['ultimo_acesso'] = df1['ultimo_acesso'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y') if not pd.isnull(x) else x)
df1['ultimo_acesso'] = pd.to_datetime(df1['ultimo_acesso'], format='%d/%m/%Y')
df1['data_cadastro'] = pd.to_datetime(df1['data_cadastro'], format='%d/%m/%Y')
df1['diferenca'] = (df1['data_cadastro'] - df1['ultimo_acesso']).dt.days
df_filtrado = df1.loc[df1['diferenca'] != 0.00]
df_filtrado = df_filtrado[['nome', 'diferenca', 'quantidade_acesso', 'data_cadastro', 'ultimo_acesso', 'fone', 'e-mail']]
df_blaster = df_filtrado.dropna(subset=['diferenca'])


df = pd.read_excel('geral_meses.xlsx')
df = df.drop([0,1,2,3])
df = df.drop(df.index[df.shape[0] - 1])
df.rename(columns={df.columns[0]: "nome"}, inplace=True)
df.rename(columns={df.columns[1]: "angolano"}, inplace=True)       
df.rename(columns={df.columns[2]: "duplicado_revendas"}, inplace=True)
df.rename(columns={df.columns[3]: "duplicado_rd"}, inplace=True)
df.rename(columns={df.columns[4]: "estudante"}, inplace=True)
df.rename(columns={df.columns[5]: "cliente"}, inplace=True)
df.rename(columns={df.columns[6]: "migracao_sistema"}, inplace=True)
df.rename(columns={df.columns[7]: "arrumando_base"}, inplace=True)
df.rename(columns={df.columns[8]: "contrato_outra_ferram"}, inplace=True)
df.rename(columns={df.columns[9]: "falta_funcionalidades"}, inplace=True)
df.rename(columns={df.columns[10]: "sem_interesse"}, inplace=True)
df.rename(columns={df.columns[11]: "sem_qualificacao"}, inplace=True)
df.rename(columns={df.columns[12]: "recusado_ven_reun"}, inplace=True)
df.rename(columns={df.columns[13]: "crm"}, inplace=True)
df.rename(columns={df.columns[14]: "site_nao_existe"}, inplace=True)
df.rename(columns={df.columns[15]: "lgpd"}, inplace=True)
df.rename(columns={df.columns[16]: "telefone_incorreto"}, inplace=True)
df.rename(columns={df.columns[17]: "agendamento_esgotado"}, inplace=True)
df.rename(columns={df.columns[18]: "contato_esgotadas"}, inplace=True)
df.rename(columns={df.columns[19]: "versao_4"}, inplace=True)
df.rename(columns={df.columns[20]: "total"}, inplace=True)

esta_presente = df_blaster['nome'].isin(df['nome'])
linhas_selecionadas = df_blaster[esta_presente]
novo_df = df.merge(linhas_selecionadas[['nome']], on='nome')
def origem(row):
    cols = ['angolano', 'duplicado_revendas', 'duplicado_rd', 'estudante', 'cliente', 'migracao_sistema', 'arrumando_base', 
        'contrato_outra_ferram', 'falta_funcionalidades', 'sem_interesse', 'sem_qualificacao', 'recusado_ven_reun', 'crm',  
        'site_nao_existe', 'lgpd', 'telefone_incorreto', 'agendamento_esgotado', 'contato_esgotadas', 'versao_4']   
    origens = [col for col in cols if pd.notna(row[col])]
    return ', '.join(origens)

novo_df['descarte'] = novo_df.apply(lambda row: origem(row), axis=1)
novo_df.drop(novo_df.columns[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
df58 = pd.merge(linhas_selecionadas, novo_df, on='nome', how='left')
df58.to_excel('nfemais_3_meuses_ju.xlsx', index=False)

df_selecionado = df58.query("'2023-01-01' <= data_cadastro <= '2023-01-31'")
df_selecionado.to_excel('df_janeironfemais.xlsx', index=False)
palavras = df58['descarte']
frequencias = Counter(palavras)
dicionario = {'palavra': [], 'frequencia': []}
for palavra, frequencia in frequencias.items():
    dicionario['palavra'].append(palavra)
    dicionario['frequencia'].append(frequencia)

df_descarte = pd.DataFrame(dicionario)
df_descarte = df_descarte.sort_values(by='frequencia', ascending=False)
df_descarte = df_descarte.head(5)

df_descarte['palavra'] = df_descarte['palavra'].replace({'contato_esgotadas': 'Contato Esgotado',
                                                         'sem_interesse': 'Sem Interesse',
                                                         'telefone_incorreto': 'Telefone Incorreto',
                                                         'crm': 'CRM',
                                                         'duplicado_rd': 'Duplicado RD Station'})
#Gráfico Pizza:
fig02 = px.bar(df_descarte,
              x='palavra',
              y='frequencia',
              height=400,
              labels={'frequencia': 'Quantidade de Descartes', 'palavra': 'Motivos de descartes em destaque'},
              color_discrete_sequence=px.colors.sequential.RdBu)
fig02.update_traces(hovertemplate='%{label}: %{value}')
fig02.update_layout(title_text='Quantidade de Descartes nos Motivos em destaque', title_x=0.5)
fig02.update_layout(
    plot_bgcolor=dbc.themes.CYBORG['dark'],
    paper_bgcolor=dbc.themes.CYBORG['dark'],
)

df80 = df58.query('-90 <= diferenca < -80')
df70 = df58.query('-79 <= diferenca < -70')
df60 = df58.query('-69 <= diferenca < -60')
df50 = df58.query('-59 <= diferenca < -50')
df40 = df58.query('-49 <= diferenca < -40')
df30 = df58.query('-39 <= diferenca < -30')
df20 = df58.query('-29 <= diferenca < -20')
df10 = df58.query('-19 <= diferenca < -10')
df00 = df58.query('-9 <= diferenca < -1')

data = [{'media': df80['quantidade_acesso'].mean().round(2), 'quantidade': df80['nome'].count(), 'nome': ' Acima de 80 dias'},
        {'media': df70['quantidade_acesso'].mean().round(2), 'quantidade': df70['nome'].count(), 'nome': ' Entre 80 e 70 dias'},
        {'media': df60['quantidade_acesso'].mean().round(2), 'quantidade': df60['nome'].count(), 'nome': ' Entre 70 e 60 dias'},
        {'media': df50['quantidade_acesso'].mean().round(2), 'quantidade': df50['nome'].count(), 'nome': ' Entre 60 e 50 dias'},
        {'media': df40['quantidade_acesso'].mean().round(2), 'quantidade': df40['nome'].count(), 'nome': ' Entre 50 e 40 dias'},
        {'media': df30['quantidade_acesso'].mean().round(2), 'quantidade': df30['nome'].count(), 'nome': ' Entre 40 e 30 dias'},
        {'media': df20['quantidade_acesso'].mean().round(2), 'quantidade': df20['nome'].count(), 'nome': ' Entre 30 e 20 dias'},
        {'media': df10['quantidade_acesso'].mean().round(2), 'quantidade': df10['nome'].count(), 'nome': ' Entre 20 e 10 dias'},
        {'media': df00['quantidade_acesso'].mean().round(2), 'quantidade': df00['nome'].count(), 'nome': ' Entre 10 e 0 dias'}]

df_resultado = pd.DataFrame(data)

#Gráfico de barras

color_scale = ['#992200', '#b22800', '#cc2d00', '#e53300', '#ff3900', '#ff4c19', '#ff6033']
fig03 = px.bar(df_resultado,
              x='quantidade',
              y='nome',
              color='media',
              height=400,
              custom_data=['media'],
              labels={'nome': 'Intervalo de dias ', 'quantidade': 'Quantidade de acessos', 'media': 'Média de Acessos'},
              color_continuous_scale=color_scale)

fig03.update_xaxes(title='Quantidade de Pessoas que Acessaram em Certo Período') 
fig03.update_yaxes(title='Faixa de Tempo de DIAS')
fig03.update_layout(title_text='Acessos por Faixa de Tempo entre CADASTRO e ÚLTIMO ACESSO', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')


#Ideia:

min_value = df58['diferenca'].min()
nome_min_value = df58.loc[df58['diferenca'] == min_value, 'nome'].iloc[0]
print(f"O maior valor de diferença entre cadastro e último acesso é de {min_value}, correspondente a: {nome_min_value}.")

max_value = df58['diferenca'].max()
nome_max_value = df58.loc[df58['diferenca'] == max_value, 'nome'].iloc[0]
print(f"O menor valor de diferença entre cadastro e último acesso é de {max_value}, correspondente a: {nome_max_value}.")

#App.Layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4(" "),
            html.Div([
            html.H5(""),
            dbc.Button("Dashboard Nfemais - eGestor", color="dark", id="location-button", size="lg")
            ], style={}),
            html.H4(" "),
            html.H5("Selecione o período da data desejada para informar a quantidade de acessos neste tempo. "),
            html.H5(" "),
            html.Div([
            dcc.DatePickerRange(
                id='date-picker',
                min_date_allowed=df58['data_cadastro'].min(),
                max_date_allowed=df58['ultimo_acesso'].max(),
                start_date=df58['data_cadastro'].min(),
                end_date=df58['ultimo_acesso'].max()
            ),
        html.Div(id='message-container'),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                    html.H5("227 leads foram registrados no Blaster e descartados no Spotter", className="card-text1"),
                    html.H5("Há registro da maior diferença de dias de acesso: 87 dias e da menor diferença de dias: 0 dias, ou seja ocorreu o cadastro e último acesso no mesmo dia.", className="card-text1")
                    ]
                    ),style={"width": "30rem",
                              "background-color": "#e3dfdf",
                              "border-radius": "10px",
                              "padding": "10px",
                              "color":"black"},
                    ),
                ], md=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                    html.H5("O motivo de descarte em que mais ocorreu foi: Contatos Esgotados (119), seguido por Lead Sem interesse (55).",
                            className="card-text2 font-weight-bold")]), style={"width": "30rem",
                                                                              "background-color": "#e3dfdf",
                                                                              "border-radius": "10px",
                                                                              "padding": "10px",
                                                                              "color":"black"},
                                                                              ),
        ], md=6),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="grafico", figure=fig03)
        ], md=6, style={"margin-top": "10px", "margin-right": "0"}),       
        dbc.Col([
            dcc.Graph(id="grafico2", figure=fig02)
        ], md=5, style={"margin-top": "10px", "margin-left": "0"}),
                ])
            ])
        ]),
    ])
])
])

@app.callback(
    dash.dependencies.Output('message-container', 'children'), 
    [dash.dependencies.Input('date-picker', 'start_date'),
     dash.dependencies.Input('date-picker', 'end_date')])
def update_message(start_date, end_date):
    filtered_df = df58[(df58['data_cadastro'] >= start_date) & (df58['ultimo_acesso'] <= end_date)]
    total_quantidade = filtered_df['quantidade_acesso'].sum()
    message = f"A data selecionada apresenta quantidade de {total_quantidade} acessos neste período, referente a Planos Gratuitos."
    return html.Div([
        html.P(message)
    ])

app.run_server(port=8080, host='192.168.30.230')
