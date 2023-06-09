# -*- coding: utf-8 -*-
"""Tratamento_de_Dados_Análise_Funcionários

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eSMIlPmfpJWdH70q3W-Jqddk9o_JGIyB

## Limpeza e Tratamento de dados:

Aqui são os códigos utilizados:
"""

import pandas as pd
import seaborn as srn
import statistics as sts

"""**Para importar os dados:**"""

dataset = pd.read_csv("Churn.csv", sep = ";")

"""Para visualizar a quantidade de linhas e colunas:

"""

dataset.shape

"""Visualização da tabela:"""

dataset.head()

"""Agora, para iniciar a limpeza dos dados, colocaremos nomes respectivos para cada linha, assim renomeando as variáveis"""

dataset.columns = ["Id", "Score", "Estado", 
                   "Genêro", "Idade", "Patrimônio",
                   "Saldo", "Produtos", "TemCartCredito",
                   "Ativo", "Salário", "Saiu"]

"""Visualização após limpeza:"""

dataset.head()

"""##**Análise Exploratória**

Primeiramente, iremos analisar a variável **"Estado"**, para visualizar a ocorrência de cada um individualmente e sua frêquencia.
"""

agrupado = dataset.groupby (['Estado']).size()
agrupado.plot.bar(color = 'pink')
agrupado

"""**Problema:** Existem estados que não existe e tem estado fora do domínio da Região Sul. assim sendo, iremos eliminar.

#Agora iremos analisar a variável **"genêro"**:
"""

agrupado = dataset.groupby (['Genêro']). size()
agrupado.plot.bar(color = 'yellow')
agrupado

"""**Problema:** Resolver F, Fem e M.

**Exploração de colunas numéricas:**
#Agora, iremos analisar o **"Score"** de cada índividuo.
"""

dataset['Score'].describe()

"""Iremos analisar a partir de um *boxplot*"""

srn.boxplot(dataset['Score']).set_title('Score')

"""Agora vamos visualizar através do *histograma*:"""

srn.distplot(dataset['Score']).set_title('Score')

"""#Agora iremos analisar a **"Idade"**:"""

dataset['Idade'].describe()

"""**Boxplot**"""

srn.boxplot(dataset['Idade']).set_title('Idade')

"""**Histograma**"""

srn.distplot(dataset['Idade']).set_title('Idade')

"""#Análise do _Saldo_"""

dataset['Saldo'].describe()

"""**Boxplot**"""

srn.boxplot(dataset['Saldo']).set_title('Saldo')

"""**Histograma**"""

srn.distplot(dataset['Saldo']).set_title('Saldo')

"""#Análise de _Salário_"""

dataset['Salário'].describe()

"""**Boxplot**"""

srn.boxplot(dataset['Salário']).set_title('Salário')

"""**Hisograma**"""

srn.distplot(dataset['Salário']).set_title('Salário')

"""#**Tratamento dos dados:**

Contar os NaN de salário e genêro
"""

dataset.isnull().sum()

"""Remover NaN e substituir pela mediana

"""

dataset['Salário'].describe()

mediana = sts.median(dataset['Salário'])
mediana

dataset['Salário'].fillna(mediana, inplace=True)

dataset['Salário'].isnull().sum()

"""Em relação ao genêro:
Falta de padronização
"""

agrupado = dataset.groupby(['Genêro']).size()

dataset['Genêro'].isnull().sum()

"""Preencher Na com masculino(moda)"""

dataset['Genêro'].fillna('Masculino', inplace=True)

dataset['Genêro'].isnull().sum()

"""Padronização"""

dataset.loc[dataset['Genêro'] == 'M', 'Genêro'] = "Masculino"
dataset.loc[dataset['Genêro'].isin( ['Fem', 'F']), 'Genêro'] = "Feminino"

agrupado = dataset.groupby (['Genêro']).size()
agrupado

"""Idades fora do domínio"""

dataset['Idade'].describe()

dataset.loc[(dataset['Idade'] < 0 ) | (dataset['Idade'] > 120)]

mediana = sts.median(dataset['Idade'])
mediana

"""Substituição:"""

dataset.loc[(dataset['Idade'] < 0 ) | (dataset['Idade'] > 120), 'Idade'] = mediana

dataset.loc[(dataset['Idade'] < 0 ) | (dataset['Idade'] > 120)]

"""Excluir pelo ID"""

dataset.drop_duplicates(subset="Id", keep='first', inplace=True)
dataset[dataset.duplicated(['Id'], keep=False)]

Estados fora de domínio - Substituir pela moda - pelo valor mais comum - RS

agrupado = dataset.groupby (['Estado']).size()
agrupado

dataset.loc[dataset['Estado']. isin( ['RP', 'SP', 'TO']), 'Estado'] = "RS"
agrupado = dataset.groupby (['Estado']).size()
agrupado

"""##Tratamento de outlier"""

desv = sts.stdev(dataset['Salário'])
desv

"""Mais de 2x o desv"""

dataset.loc[dataset['Salário'] >= 2 *desv]

mediana = sts.median(dataset['Salário'])
mediana

#atribumos
dataset.loc[dataset['Salário'] >=  2 * desv, 'Salário'] = mediana
#checamos se algum atende critério
dataset.loc[dataset['Salário'] >=  2 * desv ]

plt."titulo"