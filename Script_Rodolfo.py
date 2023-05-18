import pandas as pd
df = pd.read_excel('joseph.xlsx')
valores = df['Valor']
df['Valor'] = [float(str(valor).replace('R$ ', '').replace(',', '.')) for valor in valores]
df.loc[df['Tipo de Lancamento'].str.lower().str.contains('despesa|pagamento'), 'Valor'] *= -1
df = df.loc[:, ['Data Competencia', 'Descricao', 'Numero do Documento', 'Valor', 'Recebido de/Pago a', 'Categoria', 'Forma de Pagamento']]
novos_nomes = {df.columns[0]: "Data do financeiro", df.columns[1]: "Descrição do financeiro",
               df.columns[2]: "Número do documento", df.columns[4]: "Nome do contato",
               df.columns[5]: "Plano de contas", df.columns[6]: "Forma de Pagamento"}
df.rename(columns=novos_nomes, inplace=True)
df.to_excel('Arquivo_Ajustado2.xlsx', index=False)



