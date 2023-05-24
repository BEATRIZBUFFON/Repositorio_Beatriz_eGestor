import pandas as pd
import cufflinks as cf
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import datetime

df = pd.read_excel('marco_abril_maio0 (4).xlsx')
df['inicio'] = pd.to_datetime(df['inicio'])
df['fim'] = pd.to_datetime(df['fim'])
df['data'] = df['inicio'].dt.date
df['inicio'] = df['inicio'].dt.time.apply(lambda x: x.strftime('%H:%M'))
df['fim'] = df['fim'].dt.time.apply(lambda x: x.strftime('%H:%M'))
def atribuir_setor(row):
    if row['nome'] in ['FERNANDOPENZ', 'RODRIGO', 'WELLINGTONREIS']:
        return 'CLOSER REVENDAS'
    elif row['nome'] in ['ANARAMOS', 'LARISSAMORAIS', 'PEDROMACHADO', 'GIANFRANCODALCIN', 'JENIFFERSOARES']:
        return 'NFEMAIS+'
    elif row['nome'] in ['ESTEFANICAMPOS', 'ALMIRERTEL', 'PAULAFIORAVANTE', 'PEDROFREITAS']:
        return 'PLANILHAS'
    elif row['nome'] in ['ANDRESSALIMA', 'EDUARDAFRAGOSO', 'DANIELOLIVEIRA', 'FELIPEFIORINI', 'GABRIELEMOTTA', 'GABRIELMARTINS', 'PATRICIALIMA', 'RENATA']:
        return 'TRIALS'
    elif row['nome'] in ['BEATRIZKOWAS', 'AUGUSTOBARRETO', 'KALLEOETHUR', 'MARCELOMACHADO']:
        return 'OUTBAND'
    elif row['nome'] in ['GUILHERMENETTO', 'LILIAN', 'VANESSA', 'NAIANEBOCK', 'ALISSON', 'CAMILAW', 'ANDRESSAELY' ]:
        return 'CLOSERS'
    else:
        return None
df['setor'] = df.apply(atribuir_setor, axis=1)

setores_validos = ['CLOSER REVENDAS', 'NFEMAIS+', 'PLANILHAS', 'TRIALS', 'OUTBAND', 'CLOSERS']
df = df[df['setor'].isin(setores_validos)]

df_filtrado = df.loc[df['duracao'] >= 6]
df_agrupado5 = df_filtrado.groupby(['nome', 'data'])['duracao'].sum() / 60
df_agrupado5['setor'] = df_agrupado5.apply(atribuir_setor, axis=1)
df_agrupado5 = df_agrupado5.round().astype(int)
df_agrupado55 = df_agrupado5.reset_index()
df_agrupado55['setor'] = df_agrupado55.apply(atribuir_setor, axis=1)
df_agrupado55.to_excel('Duracao.xlsx', index=False)

df_filtrado2 = df.loc[df['duracao'] >= 6]
df_agrupado55 = df_filtrado2.groupby(['nome', 'data'])['duracao'].count()
df_agrupado55 = df_agrupado55.round().astype(int)
df_agrupado55 = pd.DataFrame({'nome': df_agrupado55.index, 'quantidade': df_agrupado55.values})
df_agrupado555 = df_agrupado55.reset_index()
df_agrupado555['setor'] = df_agrupado555.apply(atribuir_setor, axis=1)
df_agrupado555.to_excel('Quantidade.xlsx', index=False)

df_jump = df.loc[df['duracao'] < 6]
df_jump2 = df_jump.groupby(['nome', 'data'])['duracao'].sum() / 60
df_jump3 = df_jump2.round().astype(int).reset_index()
dfjump = pd.DataFrame({'nome': df_jump3['nome'], 'data': df_jump3['data'], 'minutos': df_jump3['duracao']})
df_filtro = df.loc[df['duracao'] < 6]
df_agrup2 = df_filtro.groupby(['nome', 'data'])['duracao'].count()
df_agrup2 = df_agrup2.astype(int)
df_resul2 = pd.DataFrame({'nome': df_agrup2['nome'], 'data': df_agrup2['data'], 'quantidade': df_agrup2['quantidade']})
df_agrup2 = df_agrup2.reset_index()
df_agrup2['setor'] = df_agrup2.apply(atribuir_setor, axis=1)
teste = df_agrup2
teste.to_excel('Jump.xlsx', index=False)

df["horario_arredondado"] = pd.to_datetime(df["inicio"]).dt.floor("H") + pd.to_timedelta(((pd.to_datetime(df["inicio"]).dt.minute // 10) * 10).astype(str) + "min")
horarios = pd.date_range(start="09:00", end="18:00", freq="10min")
df_horarios = pd.DataFrame({"horario_arredondado": horarios})
df_merge = pd.merge(df_horarios, df, on="horario_arredondado", how="left")
cf.go_offline()
fig = px.bar(df_merge, x="horario_arredondado", y="duracao")
df["horario_arredondado"] = pd.to_datetime(df["inicio"]).dt.floor("H") + pd.to_datetime(((pd.to_datetime(df["inicio"]).dt.minute // 10) * 10).astype(str) + "min")
horarios = pd.date_range(start="09:00", end="18:00", freq="10min")
df_horarios = pd.DataFrame({"horario_arredondado": horarios})
df_merge = pd.merge(df_horarios, df, on="horario_arrendodado", how="left")
df_merge["horario_arredondado"] = df_merge["horario_arredondado"].dt.strftime("%H:%M:%S")
df_merge['duracao'] = (df_merge['duracao']/60).round(0)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])   
today = datetime.datetime.now().date()

app.layout = html.Div([
    html.Label(' ', style={'color': 'white'}),
    dcc.DatePickerRange(
    id='date-picker-range',
    start_date_placeholder_text="Data início",
    end_date_placeholder_text="Data fim",
    calendar_orientation='vertical',
    minimum_nights=0,
    style={
        'backgroundColor': 'black',
        'color': 'black'
    },
),
    html.Br(),
    html.Div(id='output-data'),
    html.Label('Setor:', style={'color': 'gray'}),
    dcc.Dropdown(
        id='setor-dropdown',
        options=[
            {'label': 'Nfemais', 'value': 'nfemais'},
            {'label': 'Pré - Vendas', 'value': 'pre-vendas'},
            {'label': 'Vendas', 'value': 'vendas'},
            {'label': 'Pós - Vendas', 'value': 'pos-vendas'},
            {'label': 'Revendas', 'value': 'revendas'},
            {'label': 'Trials', 'value': 'trials'},
            {'label': 'Suporte', 'value': 'suporte'},
            {'label': 'Financerio/CS', 'value': 'financeiro/cs'},
            {'label': 'Closer', 'value': 'closer'},
            {'label': 'Planilhas', 'value': 'planilhas'},
            {'label': 'Farmer', 'value': 'farmer'},
            {'label': 'Administrativo', 'value': 'adm'},
        ],
         value='nfemais',
         style={
        'width': '200px',
        'backgroundColor': 'black',
        'color': 'black'},
    ), 
    html.Label('Nome:', style={'color': 'gray'}),
    dcc.Dropdown(
        id='nome-dropdown',
        options=[
            {'label': 'Adilson da Silva', 'value': 'ADILSON'}, 
            {'label': 'Alan Alves', 'value': 'ALAN'}, 
            {'label': 'Alan Carvalho', 'value': 'ALANCARVALHO'}, 
            {'label': 'Alexia Branquier', 'value': 'ALEXIABRANQUIER'}, 
            {'label': 'Aline Garcia', 'value': 'ALINEGARCIA'}, 
            {'label': 'Alisson Leal', 'value': 'ALISSON'}, 
            {'label': 'Almir Ertel', 'value': 'ALMIRERTEL'}, 
            {'label': 'Ana Noal', 'value': 'ANANOAL'}, 
            {'label': 'Ana Ramos', 'value': 'ANARAMOS'}, 
            {'label': 'Anderson Lima', 'value': 'ANDERSONLIMA'}, 
            {'label': 'Andressa Ely', 'value': 'ANDRESSAELY'}, 
            {'label': 'Andressa Lima', 'value': 'ANDRESSALIMA'}, 
            {'label': 'Augusto Barreto', 'value': 'AUGUSTOBARRETO'}, 
            {'label': 'Beatriz Buffon', 'value': 'BEATRIZBUFFON'},
            {'label': 'Beatriz Kowas', 'value': 'BEATRIZKOWAS'},
            {'label': 'Camila Wrasse', 'value': 'CAMILAW'}, 
            {'label': 'Daniel Oliveira', 'value': 'DANIELOLIVEIRA'},
            {'label': 'Deivison Elias', 'value': 'DEIVISON'},
            {'label': 'Dionathan Martins', 'value': 'DIONATHANMARTINS'},
            {'label': 'Douglas Teixeira', 'value': 'DOUGLASTEIXEIRA'},
            {'label': 'Eduarda Donadel', 'value': 'EDUARDADONADEL'},
            {'label': 'Eduarda Fragoso', 'value': 'EDUARDAFRAGOSO'},
            {'label': 'Elizandro Roos', 'value': 'ELIZANDROROOS'},
            {'label': 'Pedro Escobar', 'value': 'ESCOBAR'},
            {'label': 'Estefani Campos', 'value': 'ESTEFANICAMPOS'},
            {'label': 'Everton Massen', 'value': 'EVERTON'},
            {'label': 'Felipe Fiorini', 'value': 'FELIPEFIORINI'},
            {'label': 'Fernanda Toebe', 'value': 'FERNANDATOEBE'},
            {'label': 'Fernando Penz', 'value': 'FERNANDOPENZ'},
            {'label': 'Frederico Vargas', 'value': 'FREDERICOVARGAS'},
            {'label': 'Gabriela Motta', 'value': 'GABRIELEMOTTA'},
            {'label': 'Gabriel Martins', 'value': 'GABRIELMARTINS'},
            {'label': 'Gabriel Padoin', 'value': 'GABRIELPADOIN'},
            {'label': 'Gian Borba', 'value': 'GIAN'}, 
            {'label': 'Gian Franco Dalcin', 'value': 'GIANFRANCODALCIN'},
            {'label': 'Giobanni Zanela', 'value': 'GIOVANNIZANELA'},
            {'label': 'Guilherme Netto', 'value': 'GUILHERMENETTO'},
            {'label': 'Haigon Silva', 'value': 'HAIGONSILVA'},
            {'label': 'Henrique Zeilmann', 'value': 'HENRIQUEZEILMANN'},
            {'label': 'Igor Augusto', 'value': 'IGORAUGUSTO'},
            {'label': 'Jefferson Oliveira', 'value': 'JEFFERSONOLIVEIRA'},
            {'label': 'Jeniffer Soares', 'value': 'JENIFFERSOARES'},
            {'label': 'Jennifer Dallanora', 'value': 'JENNIFERDALLANORA'},
            {'label': 'João Ribeiro', 'value': 'JOAO'},
            {'label': 'João Palmeira', 'value': 'JOAOPALMEIRA'},
            {'label': 'Joseph Kaus', 'value': 'JOSEPH'},
            {'label': 'Juliana Kozoroski', 'value': 'JULIANA'},
            {'label': 'Juliana Rocha', 'value': 'JULIANEROCHA'},
            {'label': 'Kalleo Ethur', 'value': 'KALLEOETHUR'},
            {'label': 'Jeferson Kasper', 'value': 'KASPER'},
            {'label': 'Kauhan Cunha', 'value': 'KAUHANCUNHA'},
            {'label': 'Kayane Crestani', 'value': 'KAYANE'},
            {'label': 'Kelli Scotti', 'value': 'KELLI'},
            {'label': 'Lilian Palmeira', 'value': 'LILIAN'},
            {'label': 'Louise Sobrosa', 'value': 'LOUISE'},
            {'label': 'Lucas Godoy', 'value': 'LUCASGODOY'},
            {'label': 'Lucca Larrossa', 'value': 'LUCCALARROSSA'},
            {'label': 'Luís Barcellos', 'value': 'LUIS'},
            {'label': 'Luiz Mello', 'value': 'LUIZMELLO'},
            {'label': 'Luiz Otavio', 'value': 'LUIZOTAVIO'},
            {'label': 'Vinicius Maier', 'value': 'MAIER'},
            {'label': 'Marcelo Machado', 'value': 'MARCELOMACHADO'},
            {'label': 'Marcia Lopes', 'value': 'MARCIA'},
            {'label': 'Maria Eduarda Vargas', 'value': 'MARIAEDUARDAVARGAS'},
            {'label': 'Matheus Mesquita', 'value': 'MATHEUSMESQUITA'},
            {'label': 'Milena Machado', 'value': 'MILENAMACHADO'},
            {'label': 'Mirela Magnago', 'value': 'MIRELAMAGNAGO'},
            {'label': 'Pedro Murilo', 'value': 'MURILO'},
            {'label': 'Naiane Bock', 'value': 'NAIANEBOCK'},
            {'label': 'Nicolas Santos', 'value': 'NICOLASSANTOS'},
            {'label': 'Paola Bortoloto', 'value': 'PAOLABORTOLOTO'},
            {'label': 'Patricia Alves', 'value': 'PATRICIA'},
            {'label': 'Patricia Lima', 'value': 'PATRICIALIMA'},
            {'label': 'Patricia Melo', 'value': 'PATRICIAMELO'},
            {'label': 'Paula Fioravante', 'value': 'PAULAFIORAVANTE'},
            {'label': 'Pedro Machado', 'value': 'PEDROMACHADO'},
            {'label': 'Priscila Soldera', 'value': 'PRISCILA'},
            {'label': 'Priscila Trindade', 'value': 'PRISCILATRINDADE'},
            {'label': 'Rafaela Ferreira', 'value': 'RAFAELA'},
            {'label': 'Raissa Tolfo', 'value': 'RAISSATOLFO'},
            {'label': 'Renata Lopes', 'value': 'RENATA'},
            {'label': 'Ricardo Gölzer', 'value': 'RICARDO'},
            {'label': 'Rodrigo Silva', 'value': 'RODRIGO'},
            {'label': 'Sara Palmeira', 'value': 'SARAPALMEIRA'},
            {'label': 'Suelen Rossi', 'value': 'SUELENROSSI'},
            {'label': 'Thiago Lopes', 'value': 'THIAGOLOPES'},
            {'label': 'Vanessa Ortiz', 'value': 'VANESSA'},
            {'label': 'Victor Alves da Silva', 'value': 'VICTOR'},
            {'label': 'Victor Souza', 'value': 'VICTORSOUZA'},
            {'label': 'Vinicius Azevedo', 'value': 'VINICIUS'},
            {'label': 'Wellington Reis', 'value': 'WELLINGTONREIS'},
            {'label': 'Yuri Martins', 'value': 'YURI'},
        ],
        value='pedro',
        style={
        'width': '200px',
        'backgroundColor': 'black',
        'color': 'black'},
    ),
    dcc.Graph(id='grafico')
])

@app.callback(
    dash.dependencies.Output('grafico', 'figure'),
    [dash.dependencies.Input('setor-dropdown', 'value'),
     dash.dependencies.Input('nome-dropdown', 'value'),
     dash.dependencies.Input('date-picker-range', 'start_date'),
     dash.dependencies.Input('date-picker-range', 'end_date')])
def update_figure(selected_setor, selected_nome, start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    filtered_df = df_merge[(df_merge.setor == selected_setor) & (
        df_merge.nome == selected_nome)]
    filtered_df = filtered_df[(filtered_df['data'] >= start_date) & (filtered_df['data'] <= end_date)]
    fig = px.bar(filtered_df,
                 x="horario_arredondado",
                 y="duracao",
                 height=500,
                 color_discrete_sequence=px.colors.qualitative.G10,
                 labels={'horario_arredondado': 'Data/Hora',
                         'duracao': 'Duração da ligação(min)'},
                 template='plotly_dark')
    fig.update_xaxes(title='Hórarios')
    fig.update_yaxes(title='Duração da Ligação em Minuto)')
    fig.update_layout(title={
        'text': 'Intervalo de Tempo em Ligações por Minuto',
        'y': 0.9,
        'x': 0.5
    })
    return fig

app.run_server(port='8060', host='192.168.30.230')
