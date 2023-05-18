# Importação de pacotes utilizados
from yellowbrick.regressor import ResidualsPlot
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from dash import Dash, html, dcc
import pandas as pd
import dash
import plotly.express as px
import plotly_ecdf
import seaborn as srn
import statistics as sts
import numpy as np
import matplotlib.pyplot as plt
from math import ceil
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
pd.options.plotting.backend = 'plotly'

# Código de aplicação web construída com o framework Dash da biblioteca Plotly e com dbc usando um tema
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Lendo o arquivo em csv
df = pd.read_csv('habilitacao.csv')

#TRATAMENTO DOS DADOS A PARTIR DAQUI:

# Excluindo colunas que não são relevantes para a análise
df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1, inplace=True)

# Renomeando as colunas com nomes limpos e claros para chamar quando necessário as variáveis
df.rename(columns={df.columns[0]: "servico"}, inplace=True)
df.rename(columns={df.columns[1]: "data"}, inplace=True)
df.rename(columns={df.columns[2]: "valor"}, inplace=True)

# Passando a coluna 'setor' como String
df['servico'] = df['servico'].astype(str)

# Renomeando na coluna 'valor' a vírgula(,), por (.) para quando realizar análise estatística entender que são valores
df['valor'] = df['valor'].str.replace(',', '.')

# Ajuste na coluna 'data' e passando para Datetime com formato ideal:
index_to_drop = df[df["data"] == "Data"].index
df = df.drop(index_to_drop)
df["data"] = pd.to_datetime(df["data"], format='%d/%m/%Y')

# Criação de uma função que retorne as informações de um serviço específico a partir de uma string de busca e chame
# a funçaõ três vezes com as strings de busca adequadas, tal qual, indíces iniciais e finais da seção e retornar
#  uma subseção do df usando a função loc[]
def get_service_info(df, search_string, end_string):
    in_idx = df[df["servico"].str.startswith(search_string)].index[0]
    fi_idx = df[(df["servico"].str.startswith(end_string))
                & (df.index > in_idx)].index[0]
    return df.loc[in_idx:fi_idx]
alan_c = get_service_info(df, "Alan Carvalho", "TOTAL DE ALAN CARVALHO")
brendon = get_service_info(df, "Brendon", "TOTAL DE BRENDON")
alexia = get_service_info(df, "Alexia Branquier", "TOTAL DE ALEXIA BRANQUIER")
joao_r = get_service_info(df, "João Reis", "TOTAL DE JOãO REIS")
suelen = get_service_info(df, "Suelen Lopes", "TOTAL DE SUELEN LOPES")
fernando = get_service_info(df, "Fernando P", "TOTAL DE FERNANDO P")
priscila = get_service_info(df, "Priscila Trindade","TOTAL DE PRISCILA TRINDADE")
naiane = get_service_info(df, "Naiane Bock", "TOTAL DE NAIANE BOCK")
vinicius_d = get_service_info(df, "Vinicius Dalcin", "TOTAL DE VINICIUS DALCIN")
aline = get_service_info(df, "AlineGarcia", "TOTAL DE ALINEGARCIA")
benhur = get_service_info(df, "Benhur Carvalho", "TOTAL DE BENHUR CARVALHO")
mirela = get_service_info(df, "Mirela Magnago", "TOTAL DE MIRELA MAGNAGO")
alex = get_service_info(df, "Alex Friedrich", "TOTAL DE ALEX FRIEDRICH")
ana = get_service_info(df, "Ana Beatriz", "TOTAL DE ANA BEATRIZ")
yuri = get_service_info(df, "Yuri Martins", "TOTAL DE YURI MARTINS")
felipe = get_service_info(df, "Felipe Guerra", "TOTAL DE FELIPE GUERRA")
luiz = get_service_info(df, "Luiz Otavio", "TOTAL DE LUIZ OTAVIO")
gui_a = get_service_info(df, "Gui Augusto", "TOTAL DE GUI AUGUSTO")
alisson = get_service_info(df, "Alisson", "TOTAL DE ALISSON")
lilian = get_service_info(df, "Lilian Palmeira", "TOTAL DE LILIAN PALMEIRA")
joseph = get_service_info(df, "Joseph Kaus", "TOTAL DE JOSEPH KAUS")
camila_w = get_service_info(df, "Camila Wrasse", "TOTAL DE CAMILA WRASSE")
camila_s = get_service_info(df, "Camila Soares", "TOTAL DE CAMILA SOARES")
rodrigo = get_service_info(df, "Rodrigo Santos", "TOTAL DE RODRIGO SANTOS")
sharom = get_service_info(df, "Sharom Lopes", "TOTAL DE SHAROM LOPES")
murilo = get_service_info(df, "Pedro Murilo Leal da Silva","TOTAL DE PEDRO MURILO LEAL DA SILVA")
luis = get_service_info(df, "Luis Henrique Barcellos","TOTAL DE LUIS HENRIQUE BARCELLOS")
nathalia = get_service_info(df, "Nathalia Paola Dias", "TOTAL DE NATHALIA PAOLA DIAS")
gui_n = get_service_info(df, "Gui Netto", "TOTAL DE GUI NETTO")
gian = get_service_info(df, "Gian Borba", "TOTAL DE GIAN BORBA")
douglas = get_service_info(df, "Douglas Fritzen", "TOTAL DE DOUGLAS FRITZEN")
victor = get_service_info(df, "Victor Alves", "TOTAL DE VICTOR ALVES")
patricia = get_service_info(df, "Patricia Barcarolo", "TOTAL DE PATRICIA BARCAROLO")
rossandra = get_service_info(df, "Rossandra Killian", "TOTAL DE ROSSANDRA KILLIAN")
joao = get_service_info(df, "João Ribeiro", "TOTAL DE JOãO RIBEIRO")
alexandre = get_service_info(df, "Alexandre Fialho", "TOTAL DE ALEXANDRE FIALHO")
vanessa = get_service_info(df, "Vanessa Ortiz", "TOTAL DE VANESSA ORTIZ")
brenda = get_service_info(df, "Brenda", "TOTAL DE BRENDA")
pedro = get_service_info(df, "Pedro Reis", "TOTAL DE PEDRO REIS")
alan_a = get_service_info(df, "Alan Alves", "TOTAL DE ALAN ALVES")
ricardo = get_service_info(df, "Ricardo Golzer", "TOTAL DE RICARDO GOLZER")
mirian = get_service_info(df, "Mirian Rosso", "TOTAL DE MIRIAN ROSSO")
denis = get_service_info(df, "Denis", "TOTAL DE DENIS")
marcia = get_service_info(df, "Marcia BL", "TOTAL DE MARCIA BL")
zipline = get_service_info(df, "Zipline", "TOTAL DE ZIPLINE")
ieda = get_service_info(df, "Ieda RK", "TOTAL DE IEDA RK")
everton = get_service_info(df, "Éverton MG", "TOTAL DE ÉVERTON MG")
mariane = get_service_info(df, "Mariane WV", "TOTAL DE MARIANE WV")
vinicius_l = get_service_info(df, "Vinicius LA", "TOTAL DE VINICIUS LA")
sem_responsavel = get_service_info(df, "Sem responsável", "TOTAL DE SEM RESPONSáVEL")

# Criação de uma função que realiza as operações de exclusão de linhas e inserção de coluna 'setor', aplicando essa função a cada um dos df
def process_dataframe(df, setor):
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.drop(df.index[[0, -1]])
    df.insert(3, "setor", setor)
    return df
everton1 = process_dataframe(everton, "Financeiro")
mariane1 = process_dataframe(mariane, "Financeiro")
vinicius_l1 = process_dataframe(vinicius_l, "Financeiro")
sem_responsavel1 = process_dataframe(sem_responsavel, "Financeiro")
lilian1 = process_dataframe(lilian, "Nfemais")
ieda1 = process_dataframe(ieda, "Financeiro")
zipline1 = process_dataframe(zipline, "Financeiro")
marcia1 = process_dataframe(marcia, "Trials")
denis1 = process_dataframe(denis, "Trials")
mirian1 = process_dataframe(mirian, "Trials")
ricardo1 = process_dataframe(ricardo, "Financeiro")
pedro1 = process_dataframe(pedro, "Trials")
brenda1 = process_dataframe(brenda, "Trials")
vanessa1 = process_dataframe(vanessa, "Trials")
alan_a1 = process_dataframe(alan_a, "Inband")
joao1 = process_dataframe(joao, "Trials")
alexandre1 = process_dataframe(alexandre, "CS")
rossandra1 = process_dataframe(rossandra, "Financeiro")
victor1 = process_dataframe(victor, "Financeiro")
patricia1 = process_dataframe(patricia, "Outband")
douglas1 = process_dataframe(douglas, "Inband")
nathalia1 = process_dataframe(nathalia, "Outband")
gian1 = process_dataframe(gian, "Trials")
gui_n1 = process_dataframe(gui_n, "Trials")
luis1 = process_dataframe(luis, "CS")
murilo1 = process_dataframe(murilo, "Farmer")
sharom1 = process_dataframe(sharom, "Trials")
rodrigo1 = process_dataframe(rodrigo, "Outband")
camila_s1 = process_dataframe(camila_s, "Outband")
camila_w1 = process_dataframe(camila_w, "Trials")
joseph1 = process_dataframe(joseph, "CS")
alisson1 = process_dataframe(alisson, "Trials")
gui_a1 = process_dataframe(gui_a, "Outband")
luiz1 = process_dataframe(luiz, "Financeiro")
felipe1 = process_dataframe(felipe, "CS")
yuri1 = process_dataframe(yuri, "Farmer")
ana1 = process_dataframe(ana, "CS")
alex1 = process_dataframe(alex, "Farmer")
mirela1 = process_dataframe(mirela, "Financeiro")
benhur1 = process_dataframe(benhur, "Outband")
aline1 = process_dataframe(aline, "CS")
priscila1 = process_dataframe(priscila, "CS")
vinicius_d1 = process_dataframe(vinicius_d, "Farmer")
naiane1 = process_dataframe(naiane, "Nfemais")
fernando1 = process_dataframe(fernando, "Outband")
suelen1 = process_dataframe(suelen, "Farmer")
joao_r1 = process_dataframe(joao_r, "CS")
alexia1 = process_dataframe(alexia, "Financeiro")
alan_c1 = process_dataframe(alan_c, "Outband")
brendon1 = process_dataframe(brendon, "Outband")

# Concatenação de todos os df anteriores
dados = pd.concat([douglas1, alan_a1, naiane1, lilian1, vinicius_d1, murilo1, suelen1, alex1, yuri1, alisson1, sharom1, gui_n1,
                   gian1, joao1, vanessa1, brenda1, pedro1, mirian1, denis1, marcia1, camila_w1, joao_r1, priscila1, aline1, ana1, felipe1,
                   joseph1, alexandre1, alexia1, mirela1, luiz1, zipline1, ieda1, everton1, mariane1, ricardo1, victor1, vinicius_l1,
                   sem_responsavel1, rossandra1, brendon1, alan_c1, fernando1, benhur1, gui_a1, camila_s1, rodrigo1, nathalia1, luis1])

# Seleção da coluna com o setor específico, salvando cada seleção em um arquivo CSV, após lê cada arquivo
# e calcula a soma, mediana e média dos valores da coluna "valor" para cada setor, com arredondamento em (2) na soma e imprime o resultado na tela
df_cs = dados[dados["setor"] == "CS"]
df_cs.to_csv("df_cs.csv")
df_cs = pd.read_csv("df_cs.csv")
soma_cs = df_cs['valor'].sum().round(2)
mediana_cs = df_cs['valor'].median()
media_cs = df_cs['valor'].mean()

df_trials = dados[dados["setor"] == "Trials"]
df_trials.to_csv("df_trials.csv")
df_trials = pd.read_csv("df_trials.csv")
soma_trials = df_trials['valor'].sum().round(2)
mediana_trials = df_trials['valor'].median()
media_trials = df_trials['valor'].mean()

df_nfemais = dados[dados["setor"] == "Nfemais"]
df_nfemais.to_csv("df_nfemais.csv")
df_nfemais = pd.read_csv("df_nfemais.csv")
soma_nfemais = df_nfemais['valor'].sum().round(2)
mediana_nfemais = df_nfemais['valor'].median()
media_nfemais = df_nfemais['valor'].mean()

df_farmer = dados[dados["setor"] == "Farmer"]
df_farmer.to_csv("df_farmer.csv")
df_farmer = pd.read_csv("df_farmer.csv")
soma_farmer = df_farmer['valor'].sum().round(2)
mediana_farmer = df_farmer['valor'].median()
media_farmer = df_farmer['valor'].mean()

df_inband = dados[dados["setor"] == "Inband"]
df_inband.to_csv("df_inband.csv")
df_inband = pd.read_csv("df_inband.csv")
soma_inband = df_inband['valor'].sum().round(2)
mediana_inband = df_inband['valor'].median()
media_inband = df_inband['valor'].mean()

df_outband = dados[dados["setor"] == "Outband"]
df_outband.to_csv("df_outband.csv")
df_outband = pd.read_csv("df_outband.csv")
soma_outband = df_outband['valor'].sum().round(2)
mediana_outband = df_outband['valor'].median()
media_outband = df_outband['valor'].mean()

df_financeiro = dados[dados["setor"] == "Financeiro"]
df_financeiro.to_csv("df_financeiro.csv")
df_financeiro = pd.read_csv("df_financeiro.csv")
soma_financeiro = df_financeiro['valor'].sum().round(2)
mediana_financeiro = df_financeiro['valor'].median()
media_financeiro = df_financeiro['valor'].mean()

# Criação de um df com o resultado de todos os setores da soma, mediana e média dos valores
data1 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBOUND", "NFEMAIS", "OUTBOUND", "TRIALS"],
        "Soma": [soma_cs, soma_farmer, soma_financeiro, soma_inband, soma_nfemais, soma_outband, soma_trials]}
resultado_soma = pd.DataFrame(data1)
print(resultado_soma)

data2 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBOUND", "NFEMAIS", "OUTBOUND", "TRIALS"],
        "Mediana": [mediana_cs, mediana_farmer, mediana_financeiro, mediana_inband, mediana_nfemais, mediana_outband, mediana_trials]}
resultado_mediana = pd.DataFrame(data2)
print(resultado_mediana)

data3 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBOUND", "NFEMAIS", "OUTBOUND", "TRIALS"],
        "Média": [media_cs, media_farmer, media_financeiro, media_inband, media_nfemais, media_outband, media_trials]}
resultado_media = pd.DataFrame(data3)
print(resultado_media)


#Gráfico linhas por setor

def calcular_soma_acumulada(dados):
    dados = dados.sort_values('data')
    dados['soma_acumulada'] = dados['sum_valor'].cumsum()
    return dados['soma_acumulada'] 

valores_cs = calcular_soma_acumulada(cs_janeiro)
valores_farmer = calcular_soma_acumulada(farmer_janeiro)
valores_nfemais = calcular_soma_acumulada(nfemais_janeiro)
valores_financeiro = calcular_soma_acumulada(financeiro_janeiro)
valores_trials = calcular_soma_acumulada(trials_janeiro)
valores_outband = calcular_soma_acumulada(outband_janeiro)
valores_inband = calcular_soma_acumulada(inband_janeiro)

#Gráfico linha CS:
fig10 = px.line(valores_cs,
              x=np.linspace(1, 31, len(valores_cs)),
              y=np.array(valores_cs),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig10.update_xaxes(title='Dia do mês')
fig10.update_yaxes(title='Valor')
fig10.update_layout(title={
    'text': 'Curva de crescimento diária do Setor CS ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Farmer:
fig11 = px.line(valores_farmer,
              x=np.linspace(1, 31, len(valores_farmer)),
              y=np.array(valores_farmer),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig11.update_xaxes(title='Dia do mês')
fig11.update_yaxes(title='Valor')
fig11.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Farmer ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Nfemais:
fig12 = px.line(valores_nfemais,
              x=np.linspace(1, 31, len(valores_nfemais)),
              y=np.array(valores_nfemais),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig12.update_xaxes(title='Dia do mês')
fig12.update_yaxes(title='Valor')
fig12.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Nfemais ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Financeiro:
fig13 = px.line(valores_financeiro,
              x=np.linspace(1, 31, len(valores_financeiro)),
              y=np.array(valores_financeiro),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig13.update_xaxes(title='Dia do mês')
fig13.update_yaxes(title='Valor')
fig13.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Financeiro ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Trials:
fig14 = px.line(valores_trials,
              x=np.linspace(1, 31, len(valores_trials)),
              y=np.array(valores_trials),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig14.update_xaxes(title='Dia do mês')
fig14.update_yaxes(title='Valor')
fig14.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Trials ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Outband:
fig15 = px.line(valores_outband,
              x=np.linspace(1, 31, len(valores_outband)),
              y=np.array(valores_outband),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig15.update_xaxes(title='Dia do mês')
fig15.update_yaxes(title='Valor')
fig15.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Outbound ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Inband:
fig16 = px.line(valores_inband,
              x=np.linspace(1, 31, len(valores_inband)),
              y=np.array(valores_inband),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig16.update_xaxes(title='Dia do mês')
fig16.update_yaxes(title='Valor')
fig16.update_layout(title={
    'text': 'Curva de crescimento diária do Setor Inbound ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})


#Gráfico soma - curva crescimento POSITIVA dos setores:

df_cs['valor_pos'] = df_cs[df_cs['valor'] > 0]['valor']
df_cs1 = df_cs.dropna()

df_farmer['valor_pos'] = df_farmer[df_farmer['valor'] > 0]['valor']
df_farmer1 = df_farmer.dropna()

df_nfemais['valor_pos'] = df_nfemais[df_nfemais['valor'] > 0]['valor']
df_nfemais1 = df_nfemais.dropna()

df_financeiro['valor_pos'] = df_financeiro[df_financeiro['valor'] > 0]['valor']
df_financeiro1 = df_financeiro.dropna()

df_trials['valor_pos'] = df_trials[df_trials['valor'] > 0]['valor']
df_trials1 = df_trials.dropna()

df_outband['valor_pos'] = df_outband[df_outband['valor'] > 0]['valor']
df_outband1 = df_outband.dropna()

df_inband['valor_pos'] = df_inband[df_inband['valor'] > 0]['valor']
df_inband1 = df_inband.dropna()


def calcular_soma_acumulada_pos(dados):
    dados = dados.sort_values('data')
    dados['soma_acumulada_pos'] = dados['valor_pos'].cumsum()
    return dados['soma_acumulada_pos'] 

valores_cs1 = calcular_soma_acumulada_pos(df_cs1)
valores_farmer1 = calcular_soma_acumulada_pos(df_farmer1)
valores_nfemais1 = calcular_soma_acumulada_pos(df_nfemais1)
valores_financeiro1 = calcular_soma_acumulada_pos(df_financeiro1)
valores_trials1 = calcular_soma_acumulada_pos(df_trials1)
valores_outband1 = calcular_soma_acumulada_pos(df_outband1)
valores_inband1 = calcular_soma_acumulada_pos(df_inband1)

#Gráfico linha Trials:
fig20 = px.line(valores_trials1,
                x=np.linspace(1, 31, len(valores_trials1)),
                y=np.array(valores_trials1),
                height=500,
                color_discrete_sequence=px.colors.qualitative.Set3,
                template='plotly_dark')
fig20.update_xaxes(title='Dia do mês')
fig20.update_yaxes(title='Valor')
fig20.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor Trials ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha CS:
fig21 = px.line(valores_cs1,
                x=np.linspace(1, 31, len(valores_cs1)),
                y=np.array(valores_cs1),
                height=500,
                color_discrete_sequence=px.colors.qualitative.Set3,
                template='plotly_dark')
fig21.update_xaxes(title='Dia do mês')
fig21.update_yaxes(title='Valor')
fig21.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor CS ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Farmer:
fig22 = px.line(valores_farmer1,
                x=np.linspace(1, 31, len(valores_farmer1)),
                y=np.array(valores_farmer1),
                height=500,
                color_discrete_sequence=px.colors.qualitative.Set3,
                template='plotly_dark')
fig22.update_xaxes(title='Dia do mês')
fig22.update_yaxes(title='Valor')
fig22.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor Farmer ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Financeiro:
fig23 = px.line(valores_financeiro1,
                x=np.linspace(1, 31, len(valores_financeiro1)),
                y=np.array(valores_financeiro1),
                height=500,
                color_discrete_sequence=px.colors.qualitative.Set3,
                template='plotly_dark')
fig23.update_xaxes(title='Dia do mês')
fig23.update_yaxes(title='Valor')
fig23.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor Financeiro ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Nfemais:
fig24 = px.line(valores_nfemais1,
                x=np.linspace(1, 31, len(valores_nfemais1)),
                y=np.array(valores_nfemais1),
                height=500,
                color_discrete_sequence=px.colors.qualitative.Set3,
                template='plotly_dark')
fig24.update_xaxes(title='Dia do mês')
fig24.update_yaxes(title='Valor')
fig24.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor Nfemais ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Gráfico linha Outband:
fig26 = px.line(valores_outband1,
              x=np.linspace(1, 31, len(valores_outband1)),
              y=np.array(valores_outband1),
              height=500,
              color_discrete_sequence=px.colors.qualitative.Set3,
              template='plotly_dark')
fig26.update_xaxes(title='Dia do mês')
fig26.update_yaxes(title='Valor')
fig26.update_layout(title={
    'text': 'Curva de crescimento diária POSITIVA do Setor Outbound ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})

#Análise para conseguir valores inseridos dentro da plotação do gráfico da análise diária dos setores:
min_trials = trials_janeiro["sum_valor"].min()
max_trials = trials_janeiro["sum_valor"].max()
max_nfemais = nfemais_janeiro["sum_valor"].max()
min_financeiro = financeiro_janeiro["sum_valor"].min()

#INÍCIO DE VISUALIZAÇÃO DAS ANÁL

# Plotação do gráfico da mediana


# Dados necessários:
data2 = {"CS": [mediana_cs],
         "FARMER": [mediana_farmer],
         "FINANCEIRO": [mediana_financeiro],
         "INBOUND": [mediana_inband],
         "NFEMAIS": [mediana_nfemais],
         "OUTBOUND": [mediana_outband],
         "TRIALS": [mediana_trials]}
resultado_mediana_2 = pd.DataFrame(data2)
data3 = {"CS": [soma_cs],
         "FARMER": [soma_farmer],
         "FINANCEIRO": [soma_financeiro],
         "INBOUND": [soma_inband],
         "NFEMAIS": [soma_nfemais],
         "OUTBOUND": [soma_outband],
         "TRIALS": [soma_trials]}
resultado_soma_2 = pd.DataFrame(data3)

#Gráfico de cada setor em relação a soma diária no mês de Janeiro:
trials_janeiro = []
for date in df_trials['data'].unique():
    df_date = df_trials.loc[df_trials['data'] == date]
    sum_valor = df_date['valor'].sum()
    trials_janeiro.append({'data': date, 'sum_valor': sum_valor})
trials_janeiro = pd.DataFrame(trials_janeiro)
fig00 = px.bar(trials_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig00.update_xaxes(title='Setores')
fig00.update_yaxes(title='Valor')
fig00.update_layout(title={
    'text': 'Análise diária do Setor Trials ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
nfemais_janeiro = []
for date in df_nfemais['data'].unique():
    df_date = df_nfemais.loc[df_nfemais['data'] == date]
    sum_valor = df_date['valor'].sum()
    nfemais_janeiro.append({'data': date, 'sum_valor': sum_valor})
nfemais_janeiro = pd.DataFrame(nfemais_janeiro)
fig01 = px.bar(nfemais_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig01.update_xaxes(title='Setores')
fig01.update_yaxes(title='Valor')
fig01.update_layout(title={
    'text': 'Análise diária do Setor Nfemais ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
farmer_janeiro = []
for date in df_farmer['data'].unique():
    df_date = df_farmer.loc[df_farmer['data'] == date]
    sum_valor = df_date['valor'].sum()
    farmer_janeiro.append({'data': date, 'sum_valor': sum_valor})
farmer_janeiro = pd.DataFrame(farmer_janeiro)
fig02 = px.bar(farmer_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig02.update_xaxes(title='Setores')
fig02.update_yaxes(title='Valor')
fig02.update_layout(title={
    'text': 'Análise diária do Setor Farmer ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
cs_janeiro = []
for date in df_cs['data'].unique():
    df_date = df_cs.loc[df_cs['data'] == date]
    sum_valor = df_date['valor'].sum()
    cs_janeiro.append({'data': date, 'sum_valor': sum_valor})
cs_janeiro = pd.DataFrame(cs_janeiro)
fig03 = px.bar(cs_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig03.update_xaxes(title='Setores')
fig03.update_yaxes(title='Valor')
fig03.update_layout(title={
    'text': 'Análise diária do Setor CS ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
financeiro_janeiro = []
for date in df_financeiro['data'].unique():
    df_date = df_financeiro.loc[df_financeiro['data'] == date]
    sum_valor = df_date['valor'].sum()
    financeiro_janeiro.append({'data': date, 'sum_valor': sum_valor})
financeiro_janeiro = pd.DataFrame(financeiro_janeiro)
fig04 = px.bar(financeiro_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig04.update_xaxes(title='Setores')
fig04.update_yaxes(title='Valor')
fig04.update_layout(title={
    'text': 'Análise diária do Setor Financeiro ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
inband_janeiro = []
for date in df_inband['data'].unique():
    df_date = df_inband.loc[df_inband['data'] == date]
    sum_valor = df_date['valor'].sum()
    inband_janeiro.append({'data': date, 'sum_valor': sum_valor})
inband_janeiro = pd.DataFrame(inband_janeiro)
fig05 = px.bar(inband_janeiro,
               x='data',
               y='sum_valor',
               height=400,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig05.update_xaxes(title='Setores')
fig05.update_yaxes(title='Valor')
fig05.update_layout(title={
    'text': 'Análise diária do Setor Inbound ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
outband_janeiro = []
for date in df_outband['data'].unique():
    df_date = df_outband.loc[df_outband['data'] == date]
    sum_valor = df_date['valor'].sum()
    outband_janeiro.append({'data': date, 'sum_valor': sum_valor})
outband_janeiro = pd.DataFrame(outband_janeiro)
fig06 = px.bar(outband_janeiro,
               x='data',
               y='sum_valor',
               height=500,
               color_discrete_sequence=px.colors.qualitative.Set3,
               template='plotly_dark')
fig06.update_xaxes(title='Setores')
fig06.update_yaxes(title='Valor')
fig06.update_layout(title={
    'text': 'Análise diária do Setor Outband ao longo do mês de janeiro',
    'y': 0.9,
    'x': 0.5
})
figs = {'CS': fig03, 'Farmer': fig02,
        'Financeiro': fig04,'Inbound': fig05,
        'Nfmais': fig01, 'Outbound': fig06, 
        'Trials': fig00}
figs2 = {'CS': fig10, 'Farmer': fig11,
        'Financeiro': fig13,'Inbound': fig16,
        'Nfmais': fig12, 'Outbound': fig15, 
        'Trials': fig14}
figs3 = {'CS': fig21, 'Farmer': fig22,
        'Financeiro': fig23,
        'Nfmais': fig24, 'Outbound': fig26, 
        'Trials': fig20}


# Atribuição a 'options2' quais variáveis e valores para caixa de seleção no Dash 
options = [{'label': 'CS', 'value': 'CS'},
           {'label': 'FARMER', 'value': 'FARMER'},
           {'label': 'FINANCEIRO', 'value': 'FINANCEIRO'},
           {'label': 'INBOUND', 'value': 'INBOUND'},
           {'label': 'NFEMAIS', 'value': 'NFEMAIS'},
           {'label': 'OUTBOUND', 'value': 'OUTBOUND'},
           {'label': 'TRIALS', 'value': 'TRIALS'}]

# Gráfico soma ao longo mês janeiro
df1 = resultado_mediana_2.transpose()
fig0 = px.bar(df1,
               x=df1.index,
               y=df1.columns,
               height=500,
               color_discrete_sequence=px.colors.qualitative.G10,
               template='plotly_dark')
fig0.update_xaxes(title='Setores')
fig0.update_yaxes(title='Valor')
fig0.update_layout(title={
    'text': 'Somatório de cada setor ao longo do mês de Janeiro - 2023',
    'y': 0.9,
    'x': 0.5
})

df2 = resultado_soma_2.transpose()
fig01 = px.bar(df2,
               x=df2.index,
               y=df2.columns,
               height=500,
               color_discrete_sequence=px.colors.qualitative.G10,
               template='plotly_dark')
fig01.update_xaxes(title='Setores')
fig01.update_yaxes(title='Valor')
fig01.update_layout(title={
    'text': 'Somatório de cada setor ao longo do mês de Janeiro - 2023',
    'y': 0.9,
    'x': 0.5
})

# Criação do layout do Dashboard
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H5(""),
                dbc.Button("Dashboard Comercial - eGestor", color="primary", id="location-button", size="lg"),
                html.H5("Análise dos setores por meio do banco de dados do mês de Janeiro, com tratamento e análise de dados."),
            ], style={}),
        ]),
            dbc.Row([
                dbc.Col([
                    html.P("Selecione os setores que deseja visualizar:",
                        style={"margin-top": "10px"}),
                    dcc.Dropdown(id='var-dropdown', options=options, multi=True),
                    dcc.Graph(id="grafico", figure=fig0)
                ], md=6),
                dbc.Col([
                    html.P("Selecione os setores que deseja visualizar:",
                        style={"margin-top": "10px"}),
                    dcc.Dropdown(id='var-dropdown2', options=options, multi=True),
                    dcc.Graph(id="grafico2", figure=fig01)
                ], md=6),
            ]),
            html.Div([
                html.P("Selecione o setor que deseja visualizar a curva de crescimento diário com valores positivos e negativos:",
                        style={"margin-top": "10px"}),
                dcc.Dropdown(id='fig-dropdown2',
                             options=[{'label': k, 'value': k} for k in figs2.keys()],
                             value=list(figs2.keys())[0]
                ),
                html.Div(id='fig-container2', children=dcc.Graph(figure=figs2[list(figs2.keys())[0]])
                )
            ]),
            html.Div([
                html.P("Selecione o setor que deseja visualizar a curva de crescimento diário com valores positivos:",
                        style={"margin-top": "10px"}),
                html.P("Observação: O setor Inbound não apresenta-se no gráfico pois somente há valores negativos.",
                        style={"margin-top": "10px"}),
                dcc.Dropdown(id='fig-dropdown3',
                             options=[{'label': k, 'value': k} for k in figs3.keys()],
                             value=list(figs3.keys())[0]
                ),
                html.Div(id='fig-container3', children=dcc.Graph(figure=figs3[list(figs3.keys())[0]])
                )
            ]),
            html.Div([
                html.P("Selecione o setor que deseja visualizar:",
                        style={"margin-top": "10px"}),
                dcc.Dropdown(id='fig-dropdown',
                             options=[{'label': k, 'value': k} for k in figs.keys()],
                             value=list(figs.keys())[0]
                ),
                html.Div(id='fig-container', children=dcc.Graph(figure=figs[list(figs.keys())[0]])
                )
            ]),
            
        ]),
    )

#Criação das callbacks para ocorrer o funcionamento da dashboard:
@app.callback(
        [Output('grafico', 'figure'),
         Output('grafico2', 'figure'),
         Output('fig-container2', 'children'),
         Output('fig-container3', 'children'),
         Output('fig-container', 'children')],
        [Input('var-dropdown', 'value'),
         Input('var-dropdown2', 'value'),
         Input('fig-dropdown2', 'value'),
         Input('fig-dropdown3', 'value'),
         Input('fig-dropdown', 'value')]
)

def update_fig_and_graph(selected_vars, selected_vars2, selected_fig2, selected_fig3, selected_fig):
    df1 = resultado_mediana_2[selected_vars].transpose()
    fig0 = px.bar(df1,
                  x=df1.index,
                  y=df1.columns,
                  height=500,
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  template='plotly_dark')
    fig0.update_xaxes(title='Setores')
    fig0.update_yaxes(title='Valor')
    fig0.update_layout(title={
        'text': 'Mediana de cada setor no mês de Janeiro - 2023',
        'y': 0.9,
        'x': 0.5
    })
    df2 = resultado_soma_2[selected_vars2].transpose()
    fig01 = px.bar(df2,
                   x=df2.index,
                   y=df2.columns,
                   height=500,
                   color_discrete_sequence=px.colors.qualitative.Dark24,
                   template='plotly_dark')
    fig01.update_xaxes(title='Setores')
    fig01.update_yaxes(title='Valor')
    fig01.update_layout(title={
        'text': 'Somatório de cada setor no mês de Janeiro - 2023',
        'y': 0.9,
        'x': 0.5
    })
    fig_container2 = dcc.Graph(figure=figs2[selected_fig2])
    fig_container3 = dcc.Graph(figure=figs3[selected_fig3])
    fig_container = dcc.Graph(figure=figs[selected_fig])

    return fig0, fig01, fig_container2, fig_container3, fig_container

#Abri uma porta externa e rodar a dashboard:
app.run_server (port=8050, host='192.168.40.230')