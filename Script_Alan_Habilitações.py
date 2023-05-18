import pandas as pd

df = pd.read_excel('Habilitacao.xlsx')

df = df[df['Descrição'] == 'Habilitação de serviço']
df = df[df['Serviço'].str.contains('revenda', case=False)]
df = df.drop(['Período', 'Palavra-chave', 'Valor', 'Base mensal'], axis=1)
df['Data'] = pd.to_datetime(df['Data'])

# JANEIRO
df1 = df.loc[(df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-01-31')].reset_index()
df1 = df1.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df1.rename(columns={'Descrição': 'Quantidade de Habilitação'}, inplace=True)
df_janeiro = df1.sort_values('Quantidade de Habilitação', ascending=False)

df_janeiro_nfemais = df_janeiro[df_janeiro['Serviço'].str.contains('nfe', case=False)].reset_index()
df_janeiro_nfemais['Serviço'] = 'NFE+'
df_janeiro_avancado = df_janeiro[df_janeiro['Serviço'].str.contains('avançado', case=False)].reset_index()
df_janeiro_avancado['Serviço'] = 'Avançado'
df_janeiro_elite = df_janeiro[df_janeiro['Serviço'].str.contains('elite', case=False)].reset_index()
df_janeiro_elite['Serviço'] = 'Elite'

# FEVEREIRO
df2 = df.loc[(df['Data'] >= '2023-02-01') &(df['Data'] <= '2023-02-28')].reset_index()
df2 = df2.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df2.rename(columns={'Descrição': 'Quantidade de Habilitação'}, inplace=True)
df_fevereiro = df2.sort_values('Quantidade de Habilitação', ascending=False)

df_fevereiro_nfemais = df_fevereiro[df_fevereiro['Serviço'].str.contains('nfe', case=False)].reset_index()
df_fevereiro_nfemais['Serviço'] = 'NFE+'
df_fevereiro_avancado = df_fevereiro[df_fevereiro['Serviço'].str.contains('avançado', case=False)].reset_index()
df_fevereiro_avancado['Serviço'] = 'Avançado'
df_fevereiro_elite = df_fevereiro[df_fevereiro['Serviço'].str.contains('elite', case=False)].reset_index()
df_fevereiro_elite['Serviço'] = 'Elite'

# MARÇO
df3 = df.loc[(df['Data'] >= '2023-03-01') &(df['Data'] <= '2023-03-31')].reset_index()
df3 = df3.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df3.rename(columns={'Descrição': 'Quantidade de Habilitação'}, inplace=True)
df_marco = df3.sort_values('Quantidade de Habilitação', ascending=False)

df_marco_nfemais = df_marco[df_marco['Serviço'].str.contains('nfe', case=False)].reset_index()
df_marco_nfemais['Serviço'] = 'NFE+'
df_marco_avancado = df_marco[df_marco['Serviço'].str.contains('avançado', case=False)].reset_index()
df_marco_avancado['Serviço'] = 'Avançado'
df_marco_elite = df_marco[df_marco['Serviço'].str.contains('elite', case=False)].reset_index()
df_marco_elite['Serviço'] = 'Elite'

# ABRIL
df4 = df.loc[(df['Data'] >= '2023-04-01') & (df['Data'] <= '2023-04-30')].reset_index()
df4 = df4.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df4.rename(columns={'Descrição': 'Quantidade de Habilitação'}, inplace=True)
df_abril = df4.sort_values('Quantidade de Habilitação', ascending=False)

df_abril_nfemais = df_abril[df_abril['Serviço'].str.contains('nfe', case=False)].reset_index()
df_abril_nfemais['Serviço'] = 'NFE+'
df_abril_avancado = df_abril[df_abril['Serviço'].str.contains('avançado', case=False)].reset_index()
df_abril_avancado['Serviço'] = 'Avançado'
df_abril_elite = df_abril[df_abril['Serviço'].str.contains('elite', case=False)].reset_index()
df_abril_elite['Serviço'] = 'Elite'

# MAIO

df5 = df.loc[(df['Data'] >= '2023-05-01') & (df['Data'] <= '2023-05-12')].reset_index()
df5 = df5.groupby('Cliente').agg({'Descrição': 'count', 'Serviço': 'first', 'Data': 'first'}).reset_index()
df5.rename(columns={'Descrição': 'Quantidade de Habilitação'}, inplace=True)
df_maio = df5.sort_values('Quantidade de Habilitação', ascending=False)

df_maio_nfemais = df_maio[df_maio['Serviço'].str.contains('nfe', case=False)].reset_index()
df_maio_nfemais['Serviço'] = 'NFE+'
df_maio_avancado = df_maio[df_maio['Serviço'].str.contains('avançado', case=False)].reset_index()
df_maio_avancado['Serviço'] = 'Avançado'
df_maio_elite = df_maio[df_maio['Serviço'].str.contains('elite', case=False)].reset_index()
df_maio_elite['Serviço'] = 'Elite'

# PASSAR PARA EXCEL:
janeiro = pd.concat([df_janeiro_nfemais, df_janeiro_avancado, df_janeiro_elite])
janeiro.reset_index(drop=True, inplace=True)
janeiro = janeiro.sort_values(by='Quantidade de Habilitação', ascending=False)
janeiro = janeiro.drop(['index'], axis=1)
janeiro.to_excel('Janeiro_Habilitacao.xlsx', index=False)

fevereiro = pd.concat([df_fevereiro_nfemais, df_fevereiro_avancado, df_fevereiro_elite])
fevereiro.reset_index(drop=True, inplace=True)
fevereiro = fevereiro.sort_values(by='Quantidade de Habilitação', ascending=False)
fevereiro = fevereiro.drop(['index'], axis=1)
fevereiro.to_excel('Fevereiro_Habilitacao.xlsx', index=False)

marco = pd.concat([df_marco_nfemais, df_marco_avancado, df_marco_elite])
marco.reset_index(drop=True, inplace=True)
marco = marco.sort_values(by='Quantidade de Habilitação', ascending=False)
marco = marco.drop(['index'], axis=1)
marco.to_excel('Marco_Habilitacao.xlsx', index=False)

abril = pd.concat([df_abril_nfemais, df_abril_avancado, df_abril_elite])
abril.reset_index(drop=True, inplace=True)
abril = abril.sort_values(by='Quantidade de Habilitação', ascending=False)
abril = abril.drop(['index'], axis=1)
abril.to_excel('Abril_Habilitacao.xlsx', index=False)

maio = pd.concat([df_maio_nfemais, df_maio_avancado, df_maio_elite])
maio.reset_index(drop=True, inplace=True)
maio = maio.sort_values(by='Quantidade de Habilitação', ascending=False)
maio = maio.drop(['index'], axis=1)
maio.to_excel('Maio_Habilitacao.xlsx', index=False)
