import pandas as pd
from datetime import datetime

df1 = pd.read_csv('blaster.csv')
df1.drop(df1.columns[[0, 1, 5, 6]], axis=1, inplace=True)
df1['ultimo_acesso'] = pd.to_datetime(df1['ultimo_acesso'], format='%d/%m/%Y %H:%M:%S')
df1['ultimo_acesso'] = df1['ultimo_acesso'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y') if not pd.isnull(x) else x)
df1['ultimo_acesso'] = pd.to_datetime(df1['ultimo_acesso'], format='%d/%m/%Y')
df1['data_cadastro'] = pd.to_datetime(df1['data_cadastro'], format='%d/%m/%Y')
df1['diferenca'] = (df1['data_cadastro'] - df1['ultimo_acesso']).dt.days
df_filtrado = df1.loc[df1['diferenca'] != 0.00]
df_filtrado = df_filtrado[['nome', 'diferenca','quantidade_acesso', 'fone', 'e-mail']]
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

df58.describe()

from collections import Counter
palavras = df5['descarte']
frequencias = Counter(palavras)
for palavra, frequencia in frequencias.items():
    print(palavra, frequencia)

import plotly.express as px

df58_sorted = df58.sort_values('diferenca', ascending=False)
fig1 = px.bar(df58_sorted,
              x='diferenca',
              y='quantidade_acesso',
              color_discrete_sequence=px.colors.qualitative.Set1,
              height=400)
fig1.update_xaxes(title='diferenca', categoryorder='total descending')
fig1.update_layout(title_text='Gráfico de descartes de Telefone Incorreto em relação aos funcionários')
fig1.show()

