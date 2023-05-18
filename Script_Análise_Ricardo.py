import pandas as pd

# ETAPA
df1 = "spotter_etapa/etapa_janeiro.xlsx"
df1 = pd.read_excel(df1)

df2 = "spotter_etapa/etapa_fevereiro.xlsx"
df2 = pd.read_excel(df2)

df3 = "spotter_etapa/etapa_marco.xlsx"
df3 = pd.read_excel(df3)

df4 = "spotter_etapa/etapa_abril.xlsx"
df4 = pd.read_excel(df4)

df5 = "spotter_etapa/etapa_maio.xlsx"
df5 = pd.read_excel(df5)

def teste(df):
    df = df.drop([0, 1])
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index(drop=True)
    df['TOTAL'] = df['TOTAL'].astype(int)
    df.rename(columns={df.columns[1]: "Pré-Vendedor"}, inplace=True)
    df['Pré-Vendedor'] = df['Pré-Vendedor'].str.replace('^\$\$|\%\$|\@\@|\#\$|\@We', '', regex=True)
    return df

df1t = teste(df1)
df2t = teste(df2)
df3t = teste(df3)
df4t = teste(df4)
df5t = teste(df5)

df1t['Dia '] = pd.to_datetime(df1t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=1))
df1t = df1t.dropna(subste=['Dia '])
df1t['Dia '] = df1t['Dia '].dt.strftime('%d-%m-%Y')

df1t['Dia '] = pd.to_datetime(df1t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=1))
df1t = df1t.dropna(subset=['Dia ']) 
df1t['Dia '] = df1t['Dia '].dt.strftime('%d-%m-%Y')

df2t['Dia '] = pd.to_datetime(df2t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=2))
df2t = df2t.dropna(subset=['Dia ']) 
df2t['Dia '] = df2t['Dia '].dt.strftime('%d-%m-%Y')

df3t['Dia '] = pd.to_datetime(df3t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=3))
df3t = df3t.dropna(subset=['Dia ']) 
df3t['Dia '] = df3t['Dia '].dt.strftime('%d-%m-%Y')

df4t['Dia '] = pd.to_datetime(df4t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=4))
df4t = df4t.dropna(subset=['Dia ']) 

df4t['Dia '] = df4t['Dia '].dt.strftime('%d-%m-%Y')

df5t['Dia '] = pd.to_datetime(df5t['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=5))
df5t = df5t.dropna(subset=['Dia ']) 
df5t['Dia '] = df5t['Dia '].dt.strftime('%d-%m-%Y')

df_pronto1 = pd.concat([df1t, df2t, df3t, df4t, df5t], ignore_index=True)
df_pronto1.to_excel('Etapa.xlsx', index=False)

# TEMPERATURA
df11 = "temp_spotter/tempe_janeiro.xlsx"
df11 = pd.read_excel(df11)

df22 = "temp_spotter/tempe_fevereiro.xlsx"
df22 = pd.read_excel(df22)

df33 = "temp_spotter/tempe_marco.xlsx"
df33 = pd.read_excel(df33)

df44 = "temp_spotter/tempe_abril.xlsx"
df44 = pd.read_excel(df44)

df55 = "temp_spotter/tempe_maio.xlsx"
df55 = pd.read_excel(df55)

def teste2(df):
    df = df.drop([0, 1, 2])
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index(drop=True)
    df['TOTAL'] = df['TOTAL'].astype(int)
    df.rename(columns={df.columns[1]: "Pré-Vendedor"}, inplace=True)
    df['Pré-Vendedor'] = df['Pré-Vendedor'].str.replace('^\$\$|\%\$|\@\@|\#\$|\@We', '', regex=True)
    return df

def teste3(df):
    df = df.drop([0, 1])
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index(drop=True)
    df['TOTAL'] = df['TOTAL'].astype(int)
    df.rename(columns={df.columns[1]: "Pré-Vendedor"}, inplace=True)
    df['Pré-Vendedor'] = df['Pré-Vendedor'].str.replace('^\$\$|\%\$|\@\@|\#\$|\@We', '', regex=True)
    return df

df1p = teste2(df11)
df2p = teste2(df22)
df3p = teste2(df33)
df4p = teste2(df44)
df5p = teste3(df55)

df1p['Dia '] = pd.to_datetime(df1p['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=1))
df1p = df1p.dropna(subset=['Dia ']) 
df1p['Dia '] = df1p['Dia '].dt.strftime('%d-%m-%Y')

df2p['Dia '] = pd.to_datetime(df2p['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=2))
df2p = df2p.dropna(subset=['Dia ']) 
df2p['Dia '] = df2p['Dia '].dt.strftime('%d-%m-%Y')

df3p['Dia '] = pd.to_datetime(df3p['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=3))
df3p = df3p.dropna(subset=['Dia ']) 
df3p['Dia '] = df3p['Dia '].dt.strftime('%d-%m-%Y')

df4p['Dia '] = pd.to_datetime(df4p['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=4))
df4p = df4p.dropna(subset=['Dia ']) 
df4p['Dia '] = df4p['Dia '].dt.strftime('%d-%m-%Y')

df5p['Dia '] = pd.to_datetime(df5p['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=5))
df5p = df5p.dropna(subset=['Dia ']) 
df5p['Dia '] = df5p['Dia '].dt.strftime('%d-%m-%Y')

df_pronto2 = pd.concat([df1p, df2p, df3p, df4p, df5p], ignore_index=True)
df_pronto2.to_excel('Temperatura.xlsx', index=False)

# OCORRÊNCIA DE REUNIÃO

df111 = "spotter_ocorrencia/ocorrencia_janeiro.xlsx"
df111 = pd.read_excel(df111)

df222 = "spotter_ocorrencia/ocorrencia_fevereiro.xlsx"
df222 = pd.read_excel(df222)

df333 = "spotter_ocorrencia/ocorrencia_marco.xlsx"
df333 = pd.read_excel(df333)

df444 = "spotter_ocorrencia/ocorrencia_abril.xlsx"
df444 = pd.read_excel(df444)

df555 = "spotter_ocorrencia/ocorrencia_maio.xlsx"
df555 = pd.read_excel(df555)

def teste3(df):
    df = df.drop([0, 1])
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index(drop=True)
    df['TOTAL'] = df['TOTAL'].astype(int)
    df.rename(columns={df.columns[1]: "Pré-Vendedor"}, inplace=True)
    df['Pré-Vendedor'] = df['Pré-Vendedor'].str.replace('^\$\$|\%\$|\@\@|\#\$|\@We', '', regex=True)
    return df

df1o = teste(df111)
df2o = teste(df222)
df3o = teste(df333)
df4o = teste(df444)
df5o = teste(df555)

df1o['Dia '] = pd.to_datetime(df1o['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=1))
df1o = df1o.dropna(subset=['Dia ']) 
df1o['Dia '] = df1o['Dia '].dt.strftime('%d-%m-%Y')

df2o['Dia '] = pd.to_datetime(df2o['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=2))
df2o = df2o.dropna(subset=['Dia ']) 
df2o['Dia '] = df2o['Dia '].dt.strftime('%d-%m-%Y')

df3o['Dia '] = pd.to_datetime(df3o['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=3))
df3o = df3o.dropna(subset=['Dia ']) 
df3o['Dia '] = df3o['Dia '].dt.strftime('%d-%m-%Y')

df4o['Dia '] = pd.to_datetime(df4o['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=4))
df4o = df4o.dropna(subset=['Dia ']) 
df4o['Dia '] = df4o['Dia '].dt.strftime('%d-%m-%Y')

df5o['Dia '] = pd.to_datetime(df5o['Dia '], format='%d').apply(lambda x: x.replace(year=2023, month=5))
df5o = df5o.dropna(subset=['Dia ']) 
df5o['Dia '] = df5o['Dia '].dt.strftime('%d-%m-%Y')

df_pronto3 = pd.concat([df1o, df2o, df3o, df4o, df5o], ignore_index=True)
df_pronto3.to_excel('Ocorrencia.xlsx', index=False)


