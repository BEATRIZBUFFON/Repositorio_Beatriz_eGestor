import pandas as pd

df = pd.read_excel('Habilitacao.xlsx')
df = df[df['Descrição'] == 'Cancelamento de serviço']
df = df[df['Serviço'].str.contains('revenda', case=False)]
df = df.drop(['Período', 'Palavra-chave', 'Valor', 'Base mensal'], axis=1)
df['Data'] = pd.to_datetime(df['Data'])

# JANEIRO
df1 = df.loc[(df['Data'] >= '2023-01-01') &(df['Data'] <= '2023-01-31')].reset_index()
df1 = df1.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df1.rename(columns={'Descrição': 'Quantidade de Cancelamento'}, inplace=True)
df_janeiro = df1.sort_values('Quantidade de Cancelamento', ascending=False)

df_janeiro_nfemais = df_janeiro[df_janeiro['Serviço'].str.contains('nfe', case=False)].reset_index()
df_janeiro_nfemais['Serviço'] = 'NFE+'
df_janeiro_avancado = df_janeiro[df_janeiro['Serviço'].str.contains('avançado', case=False)].reset_index()
df_janeiro_avancado['Serviço'] = 'Avançado'
df_janeiro_elite = df_janeiro[df_janeiro['Serviço'].str.contains('elite', case=False)].reset_index()
df_janeiro_elite['Serviço'] = 'Elite'

# FEVEREIRO
df2 = df.loc[(df['Data'] >= '2023-02-01') &(df['Data'] <= '2023-02-28')].reset_index()
df2 = df2.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df2.rename(columns={'Descrição': 'Quantidade de Cancelamento'}, inplace=True)
df_fevereiro = df2.sort_values('Quantidade de Cancelamento', ascending=False)

df_fevereiro_nfemais = df_fevereiro[df_fevereiro['Serviço'].str.contains('nfe', case=False)].reset_index()
df_fevereiro_nfemais['Serviço'] = 'NFE+'
df_fevereiro_avancado = df_fevereiro[df_fevereiro['Serviço'].str.contains('avançado', case=False)].reset_index()
df_fevereiro_avancado['Serviço'] = 'Avançado'
df_fevereiro_elite = df_fevereiro[df_fevereiro['Serviço'].str.contains('elite', case=False)].reset_index()
df_fevereiro_elite['Serviço'] = 'Elite'

# MARÇO
df3 = df.loc[(df['Data'] >= '2023-03-01') &(df['Data'] <= '2023-03-31')].reset_index()
df3 = df3.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df3.rename(columns={'Descrição': 'Quantidade de Cancelamento'}, inplace=True)
df_marco = df3.sort_values('Quantidade de Cancelamento', ascending=False)

df_marco_nfemais = df_marco[df_marco['Serviço'].str.contains('nfe', case=False)].reset_index()
df_marco_nfemais['Serviço'] = 'NFE+'
df_marco_avancado = df_marco[df_marco['Serviço'].str.contains('avançado', case=False)].reset_index()
df_marco_avancado['Serviço'] = 'Avançado'
df_marco_elite = df_marco[df_marco['Serviço'].str.contains('elite', case=False)].reset_index()
df_marco_elite['Serviço'] = 'Elite'

# ABRIL
df4 = df.loc[(df['Data'] >= '2023-04-01') &(df['Data'] <= '2023-04-30')].reset_index()
df4 = df4.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df4.rename(columns={'Descrição': 'Quantidade de Cancelamento'}, inplace=True)
df_abril = df4.sort_values('Quantidade de Cancelamento', ascending=False)

df_abril_nfemais = df_abril[df_abril['Serviço'].str.contains('nfe', case=False)].reset_index()
df_abril_nfemais['Serviço'] = 'NFE+'
df_abril_avancado = df_abril[df_abril['Serviço'].str.contains('avançado', case=False)].reset_index()
df_abril_avancado['Serviço'] = 'Avançado'
df_abril_elite = df_abril[df_abril['Serviço'].str.contains('elite', case=False)].reset_index()
df_abril_elite['Serviço'] = 'Elite'

# MAIO
df5 = df.loc[(df['Data'] >= '2023-05-01') &(df['Data'] <= '2023-05-12')].reset_index()
df5 = df5.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df5.rename(columns={'Descrição': 'Quantidade de Cancelamento'}, inplace=True)
df_maio = df5.sort_values('Quantidade de Cancelamento', ascending=False)

df_maio_nfemais = df_maio[df_maio['Serviço'].str.contains('nfe', case=False)].reset_index()
df_maio_nfemais['Serviço'] = 'NFE+'
df_maio_avancado = df_maio[df_maio['Serviço'].str.contains('avançado', case=False)].reset_index()
df_maio_avancado['Serviço'] = 'Avançado'
df_maio_elite = df_maio[df_maio['Serviço'].str.contains('elite', case=False)].reset_index()
df_maio_elite['Serviço'] = 'Elite'

# PASSAR PARA EXCEL:
janeiro = pd.concat(   [df_janeiro_nfemais, df_janeiro_avancado, df_janeiro_elite])
janeiro.reset_index(drop=True, inplace=True)
janeiro = janeiro.sort_values(by='Quantidade de Cancelamento', ascending=False)
janeiro = janeiro.drop(['index'], axis=1)
janeiro.to_excel('Janeiro_Cancelamento.xlsx', index=False)

fevereiro = pd.concat([df_fevereiro_nfemais, df_fevereiro_avancado, df_fevereiro_elite])
fevereiro.reset_index(drop=True, inplace=True)
fevereiro = fevereiro.sort_values(by='Quantidade de Cancelamento', ascending=False)
fevereiro = fevereiro.drop(['index'], axis=1)
fevereiro.to_excel('Fevereiro_Cancelamento.xlsx', index=False)

marco = pd.concat([df_marco_nfemais, df_marco_avancado, df_marco_elite])
marco.reset_index(drop=True, inplace=True)
marco = marco.sort_values(by='Quantidade de Cancelamento', ascending=False)
marco = marco.drop(['index'], axis=1)
marco.to_excel('Marco_Cancelamento.xlsx', index=False)

abril = pd.concat([df_abril_nfemais, df_abril_avancado, df_abril_elite])
abril.reset_index(drop=True, inplace=True)
abril = abril.sort_values(by='Quantidade de Cancelamento', ascending=False)
abril = abril.drop(['index'], axis=1)
abril.to_excel('Abril_Cancelamento.xlsx', index=False)

maio = pd.concat([df_maio_nfemais, df_maio_avancado, df_maio_elite])
maio.reset_index(drop=True, inplace=True)
maio = maio.sort_values(by='Quantidade de Cancelamento', ascending=False)
maio = maio.drop(['index'], axis=1)
maio.to_excel('Maio_cancelamento.xlsx', index=False)

dfok = pd.concat([janeiro, fevereiro, marco, abril, maio], ignore_index=True)

def assign_tipo(row):
    quantidade = row['Quantidade de Cancelamento']
    if quantidade <= 5:
        return 'Até 5'
    elif 6 <= quantidade <= 9:
        return 'Entre 6 e 9'
    elif 10 <= quantidade <= 29:
        return 'Entre 10 e 29'
    else:
        return 'Acima de 30'

dfok['TIPO'] = dfok.apply(assign_tipo, axis=1)
dfok.to_excel('testealan2.xlsx', index=False)

# passar para excel/separado:

janeiro['TIPO'] = janeiro.apply(assign_tipo, axis=1)
fevereiro['TIPO'] = fevereiro.apply(assign_tipo, axis=1)
marco['TIPO'] = marco.apply(assign_tipo, axis=1)
abril['TIPO'] = abril.apply(assign_tipo, axis=1)
maio['TIPO'] = maio.apply(assign_tipo, axis=1)


def contar_tipos(df):
    tipos = df['TIPO'].value_counts().reset_index()
    tipos.colums = ['Tipo', 'Quantidade']
    return tipos

janeiro0 = contar_tipos(janeiro)
fevereiro0 = contar_tipos(fevereiro)
marco0 = contar_tipos(marco)
abril0 = contar_tipos(abril)
maio0 = contar_tipos(maio)

janeiro0.to_excel('jan.xlsx', index=False)
fevereiro0.to_excel('fev.xlsx', index=False)
marco0.to_excel('mar.xlsx', index=False)
abril0.to_excel('abr.xlsx', index=False)
maio0.to_excel('mai.xlsx', index=False)