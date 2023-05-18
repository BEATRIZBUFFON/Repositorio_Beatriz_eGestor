# Importação de pacotes utilizados
from yellowbrick.regressor import ResidualsPlot
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
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
df = pd.read_csv('Fattura_Janeiro_2023.csv')

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


df['servico'].drop_duplicates()

#dashboard automaizado para gerar análise gráfica e insights de qualuqer relatório padronizado. 
#foi criado um script para interpretar
# Criação de uma função que retorne as informações de um serviço específico a partir de uma string de busca e chame
# a funçaõ três vezes com as strings de busca adequadas, tal qual, indíces iniciais e finais da seção e retornar
#  uma subseção do df usando a função loc[]
def get_service_info(df, search_string, end_string):
    try:
        in_idx = df[df["servico"].str.startswith(search_string)].index[0]
        fi_idx = df[(df["servico"].str.startswith(end_string))
                    & (df.index > in_idx)].index[0]
        return df.loc[in_idx:fi_idx]
    except IndexError:
        return None

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
deivison = get_service_info(df,"Deivison AE", "TOTAL DE DEIVISON AE" ) 
rodrigo_p = get_service_info(df,"Rodrigo P. Fortes", "TOTAL DE RODRIGO P. FORTES") 
bruno = get_service_info(df,"Bruno G. Dias", "TOTAL DE BRUNO G. DIAS") 
pedro_b = get_service_info(df,"Pedro Batista", "TOTAL DE PEDRO BATISTA") 
juliano = get_service_info(df,"Juliano Guerra Paim", "TOTAL DE JULIANO GUERRA PAIM") 
priscila_s = get_service_info(df,"Priscila Soldera", "TOTAL DE PRISCILA SOLDERA") 
jenima = get_service_info(df,"Jemima", "TOTAL DE JEMIMA") 
diego = get_service_info(df,"Diego Polippo", "TOTAL DE DIEGO POLIPPO") 
gabriel = get_service_info(df,"Gabriel Bublitz", "TOTAL DE GABRIEL BUBLITZ") 
marcelo = get_service_info(df,"Marcelo Prates", "TOTAL DE MARCELO PRATES") 
camila_c = get_service_info(df,"Camila Cella", "TOTAL DE CAMILA CELLA") 
caroline = get_service_info(df,"Caroline Gabert", "TOTAL DE CAROLINE GABERT") 
graziele = get_service_info(df,"Graziele Lacerda", "TOTAL DE GRAZIELE LACERDA") 
sandra = get_service_info(df,"Sandra Rizzi", "TOTAL DE SANDRA RIZZI") 
victor_c = get_service_info(df,"Victor Cepillo", "TOTAL DE VICTOR CEPILLO") 
wellington = get_service_info(df,"Wellington Reis", "TOTAL DE WELLINGTON REIS") 
sara = get_service_info(df,"Sara Palmeira", "TOTAL DE SARA PALMEIRA") 
cicero = get_service_info(df,"Cícero Costa", "TOTAL DE CíCERO COSTA")
nathalia_p = get_service_info(df,"NathaliaPrieto", "TOTAL DE NATHALIAPRIETO")
giovanni = get_service_info(df,"Giovanni Zanela", "TOTAL DE GIOVANNI ZANELA") 
felipe_t = get_service_info(df,"Felipe Trindade Fiorini", "TOTAL DE FELIPE TRINDADE FIORINI") 

# Criação de uma função que realiza as operações de exclusão de linhas e inserção de coluna 'setor', aplicando essa função a cada um dos df
def process_dataframe(df, setor):
    if df is None:
        return None
    try:
        df = df.drop(df.index[[0, -1]])
        df.insert(3, "setor", setor)
        return df
    except IndexError:
        return None

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
deivison1 = process_dataframe(deivison, "Financeiro")
rodrigo_p1 = process_dataframe(rodrigo_p, "Financeiro")
bruno1 = process_dataframe(bruno, "Financeiro")
pedro_b1 = process_dataframe(pedro_b, "Financeiro")
juliano1 = process_dataframe(juliano, "Financeiro")
priscila_s1 = process_dataframe(priscila_s, "Financeiro")
jenima1 = process_dataframe(jenima, "Financeiro")
diego1 = process_dataframe(diego, "Financeiro")
gabriel1 = process_dataframe(gabriel, "CS")
marcelo1 = process_dataframe(marcelo, "Financeiro")
camila_c1 = process_dataframe(camila_c, "CS")
caroline1 = process_dataframe(caroline, "Financeiro")
graziele1 = process_dataframe(graziele, "Financeiro")
sandra1 = process_dataframe(sandra, "Financeiro")
victor_c1 = process_dataframe(victor_c, "CS")
wellington1 = process_dataframe(wellington, "Inband")
sara1 = process_dataframe(sara, "Financeiro")
cicero1 = process_dataframe(cicero, "Trials")
nathalia_p1 = process_dataframe(nathalia_p, "CS")
giovanni1 = process_dataframe(giovanni, "Outband")
felipe_t1 = process_dataframe(felipe_t, "Trials")


# Concatenação de todos os df anteriores
dados = pd.concat([douglas1, alan_a1, naiane1, lilian1, vinicius_d1, murilo1, suelen1, alex1, yuri1, alisson1, sharom1, gui_n1,
                   gian1, joao1, vanessa1, brenda1, pedro1, mirian1, denis1, marcia1, camila_w1, joao_r1, priscila1, aline1, ana1, felipe1,
                   joseph1, alexandre1, alexia1, mirela1, luiz1, zipline1, ieda1, everton1, mariane1, ricardo1, victor1, vinicius_l1,
                   sem_responsavel1, rossandra1, brendon1, alan_c1, fernando1, benhur1, gui_a1, camila_s1, rodrigo1, nathalia1, luis1, deivison1, 
                   rodrigo_p1, bruno1, pedro_b1, juliano1 , priscila_s1, jenima1, diego1 , gabriel1, marcelo1 , camila_c1, caroline1, graziele1,
                   sandra1, victor_c1, wellington1, sara1, nathalia_p1, giovanni1 , felipe_t1])
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
data1 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBAND", "NFEMAIS", "OUTBAND", "TRIALS"],
        "Soma": [soma_cs, soma_farmer, soma_financeiro, soma_inband, soma_nfemais, soma_outband, soma_trials]}
resultado_soma = pd.DataFrame(data1)
print(resultado_soma)

data2 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBAND", "NFEMAIS", "OUTBAND", "TRIALS"],
        "Mediana": [mediana_cs, mediana_farmer, mediana_financeiro, mediana_inband, mediana_nfemais, mediana_outband, mediana_trials]}
resultado_mediana = pd.DataFrame(data2)
print(resultado_mediana)

data3 = {"DataFrame": ["CS", "FARMER", "FINANCEIRO", "INBAND", "NFEMAIS", "OUTBAND", "TRIALS"],
        "Média": [media_cs, media_farmer, media_financeiro, media_inband, media_nfemais, media_outband, media_trials]}
resultado_media = pd.DataFrame(data3)
print(resultado_media)


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
    'text': 'Análise diária do Setor Nfemais ao longo do mês',
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
    'text': 'Análise diária do Setor Nfemais ao longo do mês',
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
    'text': 'Análise diária do Setor Farmer ao longo do mês',
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
    'text': 'Análise diária do Setor CS ao longo do mês',
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
    'text': 'Análise diária do Setor Financeiro ao longo do mês',
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
    'text': 'Análise diária do Setor Inband ao longo do mês',
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
    'text': 'Análise diária do Setor Outband ao longo do mês',
    'y': 0.9,
    'x': 0.5
})
figs = {'CS': fig03, 'Farmer': fig02,
        'Financeiro': fig04,'Inband': fig05,
        'Nfmais': fig01, 'Outband': fig06, 
        'Trials': fig00}


# Atribuição a 'options2' quais variáveis e valores para caixa de seleção no Dash 
options = [{'label': 'CS', 'value': 'CS'},
           {'label': 'FARMER', 'value': 'FARMER'},
           {'label': 'FINANCEIRO', 'value': 'FINANCEIRO'},
           {'label': 'INBAND', 'value': 'INBAND'},
           {'label': 'NFEMAIS', 'value': 'NFEMAIS'},
           {'label': 'OUTBAND', 'value': 'OUTBAND'},
           {'label': 'TRIALS', 'value': 'TRIALS'}]

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




df_data_cs = cs_janeiro['data'].drop_duplicates()
df_data2_cs = df_data_cs.value_counts().sort_index()
x1 = np.linspace(1, len(df_data2_cs), len(valores_cs))

fig10 = px.line(x=df_data2_cs.index,
                    y=np.array(valores_cs), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig10.update_xaxes(title='Dia do mês')
fig10.update_yaxes(title='Valor')
fig10.update_layout(title={
        'text': 'Curva de crescimento diária do Setor CS ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


df_data_farmer = farmer_janeiro['data'].drop_duplicates()
df_data2_farmer = df_data_farmer.value_counts().sort_index()
x2 = np.linspace(1, len(df_data2_farmer), len(valores_farmer))

fig11 = px.line(x=df_data2_farmer.index,
                    y=np.array(valores_farmer), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig11.update_xaxes(title='Dia do mês')
fig11.update_yaxes(title='Valor')
fig11.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Farmer ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


df_data_nfemais = nfemais_janeiro['data'].drop_duplicates()
df_data2_nfemais = df_data_nfemais.value_counts().sort_index()
x3 = np.linspace(1, len(df_data2_nfemais), len(valores_nfemais))

fig12 = px.line(x=df_data2_nfemais.index,
                    y=np.array(valores_nfemais), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig12.update_xaxes(title='Dia do mês')
fig12.update_yaxes(title='Valor')
fig12.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Nfemais ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


df_data_financeiro = financeiro_janeiro['data'].drop_duplicates()
df_data2_financeiro = df_data_financeiro.value_counts().sort_index()
x4 = np.linspace(1, len(df_data2_financeiro), len(valores_financeiro))

fig13 = px.line(x=df_data2_financeiro.index,
                    y=np.array(valores_financeiro), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig13.update_xaxes(title='Dia do mês')
fig13.update_yaxes(title='Valor')
fig13.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Financeiro ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


df_data_trials = trials_janeiro['data'].drop_duplicates()
df_data2_trials = df_data_trials.value_counts().sort_index()
x5 = np.linspace(1, len(df_data2_trials), len(valores_trials))

fig14 = px.line(x=df_data2_trials.index,
                    y=np.array(valores_trials), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig14.update_xaxes(title='Dia do mês')
fig14.update_yaxes(title='Valor')
fig14.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Trials ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })



df_data_outband = outband_janeiro['data'].drop_duplicates()
df_data2_outband = df_data_outband.value_counts().sort_index()
x6 = np.linspace(1, len(df_data2_outband), len(valores_outband))

fig15 = px.line(x=df_data2_outband.index,
                    y=np.array(valores_outband), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig15.update_xaxes(title='Dia do mês')
fig15.update_yaxes(title='Valor')
fig15.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Outband ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


df_data_inband = inband_janeiro['data'].drop_duplicates()
df_data2_inband = df_data_inband.value_counts().sort_index()
x7 = np.linspace(1, len(df_data2_inband), len(valores_inband))

fig16 = px.line(x=df_data2_inband.index,
                    y=np.array(valores_inband), 
                    height=500,
                    color_discrete_sequence=px.colors.qualitative.Set3,
                    template='plotly_dark')
fig16.update_xaxes(title='Dia do mês')
fig16.update_yaxes(title='Valor')
fig16.update_layout(title={
        'text': 'Curva de crescimento diária do Setor Inband ao longo do mês',
        'y': 0.9,
        'x': 0.5
    })


figs2 = {'CS': fig10, 'Farmer': fig11,
        'Financeiro': fig13,'Inband': fig16,
        'Nfmais': fig12, 'Outband': fig15, 
        'Trials': fig14}
#Análise para conseguir valores inseridos dentro da plotação do gráfico da análise diária dos setores:
min_trials = trials_janeiro["sum_valor"].min()
max_trials = trials_janeiro["sum_valor"].max()
max_nfemais = nfemais_janeiro["sum_valor"].max()
min_financeiro = financeiro_janeiro["sum_valor"].min()

#INÍCIO DE VISUALIZAÇÃO DAS ANÁLISES 

# Plotação do gráfico de soma
fig2 = px.bar(resultado_soma,
              x='DataFrame',
              y='Soma',
              height=500,
              color_discrete_sequence=px.colors.qualitative.G10,
              template='plotly_dark')
fig2.update_xaxes(title='Setores')
fig2.update_yaxes(title='Valor')
fig2.update_layout(title={
    'text': 'Gráfico de barras das somas de cada setor',
    'y': 0.9,
    'x': 0.5
})
fig2.update_layout(annotations=[{
    'text': 'Outband possui maior valor',
    'xref': 'x',
    'yref': 'y',
    'x': 5,
    'y': 5000,
    'showarrow': True,
    'ax': 90,
    'ay': -60,
    'font': dict(
        family="Nunito",
        size=20,
        color="#78f9ff"
    )
}])

# Plotação do gráfico da mediana
resultado_mediana
fig3 = px.bar(resultado_mediana,
              x='DataFrame',
              y='Mediana',
              height=500,
              color_discrete_sequence=px.colors.qualitative.G10,
              template='plotly_dark')
fig3.update_xaxes(title='Setores')
fig3.update_yaxes(title='Valor')
fig3.update_layout(title={
    'text': 'Gráfico de barras da mediana de cada setor',
    'y': 0.9,
    'x': 0.5
})
fig3.update_layout(annotations=[{
    'text': 'Outband possui maior mediana',
    'xref': 'x',
    'yref': 'y',
    'x': 5,
    'y': 20,
    'showarrow': True,
    'ax': 100,
    'ay': -60,
    'font': dict(
        family="Nunito",
        size=20,
        color="#78f9ff"
    )
}])

# Dados necessários:
data2 = {"CS": [mediana_cs],
         "FARMER": [mediana_farmer],
         "FINANCEIRO": [mediana_financeiro],
         "INBAND": [mediana_inband],
         "NFEMAIS": [mediana_nfemais],
         "OUTBAND": [mediana_outband],
         "TRIALS": [mediana_trials]}
resultado_mediana_2 = pd.DataFrame(data2)
data3 = {"CS": [soma_cs],
         "FARMER": [soma_farmer],
         "FINANCEIRO": [soma_financeiro],
         "INBAND": [soma_inband],
         "NFEMAIS": [soma_nfemais],
         "OUTBAND": [soma_outband],
         "TRIALS": [soma_trials]}
resultado_soma_2 = pd.DataFrame(data3)


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
    'text': 'Somatório de cada setor ao longo do mês em 2023',
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
    'text': 'Somatório de cada setor ao longo do mês em 2023',
    'y': 0.9,
    'x': 0.5
})

# Criação do layout do Dashboard
app.layout = dbc.Container([
    dbc.Col([
            html.Div([
                html.H5(""),
                dbc.Button("Dashboard Comercial - eGestor", color="primary", id="location-button", size="lg")
            ], style={}),
            html.Div([
                html.P("Selecione o setor que deseja visualizar a curva de crescimento diário:",
                        style={"margin-top": "10px"}),
                dcc.Dropdown(id='fig-dropdown2',
                             options=[{'label': k, 'value': k} for k in figs2.keys()],
                             value=list(figs2.keys())[0]
                ),
                html.Div(id='fig-container2', children=dcc.Graph(figure=figs2[list(figs2.keys())[0]])
                )
            ]),
            html.Div([
                html.P("Selecione o setor que deseja visualizar:",
                        style={'width': '50%', "margin-top": "10px"}),
                dcc.Dropdown(id='fig-dropdown',
                             options=[{'label': k, 'value': k} for k in figs.keys()],
                             value=list(figs.keys())[0]
                ),
                html.Div(id='fig-container', children=dcc.Graph(figure=figs[list(figs.keys())[0]])
                )
            ]),
        ]),
    ])

@app.callback(
    [Output('fig-container', 'children'),
     Output('fig-container2', 'children')],
    [Input('fig-dropdown', 'value'),
     Input('fig-dropdown2', 'value')]
)
def update_fig_and_graph_and_upload(selected_fig, selected_fig2):
    fig_container = dcc.Graph(figure=figs[selected_fig])
    fig_container2 = dcc.Graph(figure=figs2[selected_fig2])
    return fig_container, fig_container2

app.run_server(port='8060', host='192.168.40.230')

