import pandas as pd
import seaborn as srn
import statistics  as sts
import numpy as np
import matplotlib.pyplot as plt
from math import ceil
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from yellowbrick.regressor import ResidualsPlot 
pd.options.plotting.backend = 'plotly'
import plotly.express as px
import plotly_ecdf
import dataframe_image as dfi
import pandas as pd
import numpy as np

"""##Sobre os dados:

O banco de dados apresenta 33 observações e 4 variáveis, de modo que foram extraídos do Spotter, analisando as seguintes variáveis:

1. `func`: Funcionários da empresa;
1. `exc_lgpd`: Exclusões da Lei Geral de proteção de Dados (LGPD)
1. `num_inc`: Números incorretos ou que não existem;
1. `blacklist`: Blacklist

Para realizar a importação dos dados:
"""

dataset = pd.read_csv("dados1.csv")
dataset.head(50)

dataset['num_inc'].sum()

"""##Análise descritiva de exclusões **LGPD**

Aqui foi realizada a plotação do gráfico para analisar a quantidade de `exc_lgpd` realizadas de cada funcionário, respectivamente.
"""

fig1 = px.bar(dataset,
              x='func', 
              y='exc_lgpd',
              color='exc_lgpd', 
              height=400,  
              color_continuous_scale=px.colors.sequential.Viridis_r)
fig1.update_xaxes(title = 'Funcionários')
fig1.update_yaxes(title = 'Descartes em Exclusões LGPD')
fig1.update_layout(title_text='Gráfico de barras de descartes em Exclusões LGPD em relação aos funcionários')

v

"""**Jennifer Dallanora** com maior descarte em exclusões;

**Eduarda Fragoso, Gabriel Martins, Gabriela Motta, Matheus Mesquista, Felipe Fiorini** com números entre 80 a 42 descartes; 

**Restante**; números baixos

No gráfico de dispersão há a possibilidade de ocorrer uma visualização boa em relação aos outliers, porém não há correlação, pois a variável y, caracterizada por `func` não é dependente da váriavel x, carcaterizada por `exc_lgpd` pois não há a ocorrência de causa e efeito.

- Joseph: percebe-se que os outliers pertencem a setores distintos. Os funcionarios que apresentam o menor número ou números nulos são os funcionários mais antigos e mais experientes.

## A seguir, foi plotado um histograma para analisar a frequência da variável `exc_lgpd`.

**Frequência** entre a quantidade de funcionários descartando em Exclusões por LGPD. Outro meio de visualização, atráves do histograma.
"""

dataset.plot(kind='hist', x='exc_lgpd')

"""
Pela visualização imediata do gráfico identifica - se uma frequência de que a maioria dos funcionários possuem poucas exclusões por LGPD. Porém tem um pequeno número de pessoas que possuem uma margem de exclusão entre 40 a 100 casos, aproximademente, aparentando ser um outlier superior, possível de melhor identificação no boxplot. Possivelmente este outlier é positivo pois entendem qual a destinação adequada de quando um lead pede para exclusão de seu cadastro."""

dataset.plot.box(x='exc_lgpd')

"""##Análise descritiva de números incorretos

Para analisar os descartes de números incorretos foi plotado um histograma para analisar a frequência da variável `num_inc`.
"""

fig2 = px.bar(dataset,
              x='func', 
              y='num_inc',
              color='num_inc', 
              height=400,  
              color_continuous_scale=px.colors.sequential.Viridis_r)
fig2.update_xaxes(title = 'Funcionários')
fig2.update_yaxes(title = 'Descartes em Números Incorretos')
fig2.update_layout(title_text='Gráfico de barras de descartes em Número Incorretos em relação aos funcionários')

"""Em relação a opção de motivo de descarte como número incorreto, os números são bem mais altos em relação às exclusões de LGPD, apresentando uma **frequência maior de descartes entre a quantidade de 0 a 199.** 

**Kauhan Cunha** apresenta com maior quantidade de descartes em números incorretos, considerando - se um outlier positivo ou neagtivo?


Possibilidade: Receber mais leads; realizou o encaminhamento correto; (...?)

"""

dataset.plot(kind='hist', x='num_inc')

"""##Análise descritiva correlacionando exclusões LGPD e números incorretos

Aqui é realizada uma análise em relação aos descartes de exclusões de LGPD  e de números incorretos, de modo que a partir do gráfico de dispersão conseguimos analisar se apresenta uma correlação ou não, podendo ser linear, positiva ou negativa.
"""

color_discrete_sequence=px.colors.qualitative.G10,

import scipy.stats
x = (0, 5, 1, 20, 0, 5, 0, 2, 71, 43, 80, 8, 1, 2, 47, 9, 6, 2, 0, 3, 16, 0, 16, 0, 12, 0, 17, 125, 16, 0, 42, 0, 9, 3)
y = (184, 1003, 43, 1676, 152, 463, 0, 300, 855, 600, 907, 512, 298, 429, 955, 181, 465, 70, 119, 105, 446, 253, 125, 0, 772, 0, 392, 487, 534, 0, 820, 0, 157, 356)
scipy.stats.pearsonr(x,y)

"""**Coeficiente de correlação:** 0.4658466069387056

**Valor p:** 0.005492800432890679
Valor de p <= 0.05 (prob <= 5%) = diferença signficativa entre os grupos.

O coeficiente de correlação é positiva moderada, ou seja, possui um aumento no valor da uma variável de **exc_lgpd** quando a variável **num_inc** também aumenta. Sendo assim, é possível identificar que quanto mais descartes de exclusões por LGPD tem, mais descartes por números incorretos vai haver.

Por qual motivo está ocorrendo isto?

##Análise descritiva da Blacklist

Para analisar a variável `blacklist` foi plotado um histograma, apresentando a visualização da frequência.
"""

dataset.plot(kind='hist', x='blacklist', color='skyblue')

"""Diante da visualização do gráfico, nota - se uma frequência maior entre 0 a 19 entradas na Blacklist, tal que 28 funcionários estão nesta frequência. Assim, podemos analisar pelo boxplot que outros funcionários que estão fora desta frequência maior são outliers da variável `blacklist`."""

dataset.plot.box(x='blacklist')

"""Em relação a visualização no boxplot, notamos que há sete outliers e um em específico mais distante, de modo que em geral a mediana é 1 e o outlier maior é de 209 entradas na Blacklist.

Qual motivo para uma grande discrepância?

#**Análise de entradas de leads:**

##Agora iremos analisar a relação de entradas de leads para cada funcionário e as exclusões LGPD.

## Sobre os dados:
O banco de dados apresenta 33 observações e 5 variáveis, de modo que foram extraídos do Spotter, analisando as seguintes variáveis:

`func`: Funcionários da empresa;

`exc_lgpd`: Exclusões da Lei Geral de proteção de Dados (LGPD)

`num_inc`: Números incorretos ou que não existem;

`blacklist`: Blacklist

`ent`: Entrada de leads
"""

df = pd.read_csv("planilha.csv")
df.head(32)

df.plot.box(x='ent')

"""Boxplot: apresenta dados que possibilita visualizar que entre os 32 funcionários, 

1.   **o mínimo de entrada de leads foi: 0**; 
2.   **o máximo de entrada de leads foi: 19.756**;
3.   **a mediana é de 6277 = MEDIANA:  tendência central para distribuições numéricas distorcidas;**

## **Entradas de leads e Exclusões LGPD:**
"""

fig2 = px.bar(df,
              x='func', 
              y='exc_lgpd',
              color='ent', 
              height=400,  
              color_discrete_sequence=px.colors.qualitative.T10)
fig2.update_xaxes(title = 'Exclusões LGPD')
fig2.update_yaxes(title = 'Entrada de Leads')
fig2.update_layout(title_text='Gráfico de barras da entrada de leads em função dos descartes em exclusões LGPD')

"""* Em relação aos funcionários que descartaram até 10 exclusões LGPD, foram os que mais receberam a entrada de leads. 

**Ana Paula Ramos** foi a que mais recebeu leads, porém a quantidade de descartes em exclusões lgpd foi muito pequena comparado a entrada.

Neste gráfico é possível identificar a visualização melhor de funcionários que possuem maiores quantidades de entradas de leads pelo tamanho da bolha e pela cor a quantidade de descartas de exclusões LGPD. 

**Destaque:**

Em relação aos outliers das exclusões LGPD no primeiro gráfico do relatório que foram identificados: Jennifer Dallanora, Gabriel Martins e a Eduarda Fragoso, neste gráfico de bolhas é possível visualizar que estão entre os que mais tiveram exclusões (cor rosa) e receberam um número menor de entrada de leads.

Jennifer Dallanora foi a que mais descartou em exclusões lgpd e a quantidade de entrada de leads está perto do valor da mediana de números totais de todos os funcionários.
"""

df.plot.scatter(x= 'exc_lgpd', y= 'ent')

"""### Resultado do coeficiente de correlação e valor p, correlacionando as variáveis `exc_lgpd`e `ent`:

"""

import scipy.stats
x = (0, 5, 1, 20, 0, 5, 0, 2, 71, 43, 80, 8, 1, 2, 47, 9, 6, 2, 0, 3, 16, 0, 16, 0, 12, 0, 17, 125, 16, 0, 42, 9, 3)
y = (2391, 8015, 875, 8429, 2617, 5833, 0, 4622, 4622, 15269, 11293, 12555, 11293, 11975, 18905, 19756, 15393, 1751, 3773, 1068, 11534, 2816, 2450, 2062, 8236, 0, 7721, 10992, 6277, 0, 13237, 1755, 13006)
scipy.stats.pearsonr(x,y)

"""Possui uma correlação fraca, indicando que existe uma correlação muito baixa em relação às entradas de leads e excluções LGPD, de modo que uma variável não dependa da outra.

## **Entradas de leads e Números incorretos:**
"""

figu = px.scatter(df, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
figu.update_layout(title = 'Números incorretos  x Entradas de leads')
figu.update_xaxes(title = 'Números incorretos')
figu.update_yaxes(title = 'Entradas de leads')
figu.show()

"""Acima, é possível identificar o "outlier" identificado no gráfico de análise de números incorretos no ínicio do relatório, tal que um funcionário (Kauhan Cunha) possui uma quantidade de entrada de leads perto da mediana do total dos funcionários com o maior número de descartes em números incorretos.
Ainda assim, outro funcionário com um número de entrada de leads menor que a mediana do total, com 4622 possui uma quantidade grande de descartes, sendo: 855.  

Agora em relação a funcionaŕios com maiores entradas de leads são os que apresentam os menores descartes em números incorretos, em destaque: Ana paula Ramos.
"""

df.plot.scatter(x= 'num_inc', y= 'ent')

"""### Resultado do coeficiente de correlação e valor p, correlacionando as variáveis `num_inc`e `ent`:"""



"""Neste gráfico de dispersão, é possível identificar uma correlação linear positiva moderada, ou seja, há uma dependência entre a variável x e y. É observável que quanto maior a entrada de leads, mais descartes na opção de números incorretos acontece, entretanto essa crescente dependência acontece linearmente mais no ínicio do gráfico.

##**Análise por setor**

##Sobre os dados:

O banco de dados apresenta 5 variáveis, as quais estãos listadas abaixo e as observações depende de quantos funcionários estão no setor.

1. `func`: Funcionários da empresa;
1. `exc_lgpd`: Exclusões da Lei Geral de proteção de Dados (LGPD)
1. `num_inc`: Números incorretos ou que não existem;
1. `blacklist`: Blacklist
1. `ent`: Entrada de leads
"""

df1 = pd.read_csv("canais_ib.csv")
df1.head()

fig = px.scatter(df1, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df1, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

"""Nos canais ib, dois funcionários possuem números com grande discrepância, tal que a Jennifer Dallanora tem o triplo de exclusões LGPD em relação ao Matheus e a entrada de leads são parecidas, porém em relação ao descarte em números incorretos acontece o contrário, Matheus apareseta o dobro de descartes em números incorretos."""

df2 = pd.read_csv("canais_ob.csv")
df2.head(20)

fig = px.scatter(df2, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df2, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

"""No setor de canais ob, 3 funcionários apresentam números de entradas de leads e exclusões LGPD na mesma faixa, entretanto há um funcionário(Augusto) com quantidade grande e com baixo descartes em exclusões LGPD comparado com os demais. Entretanto, esse mesmo funcionário é um dos que mais apresenta descartes em números incorretos. Ainda assim, Kauhan é o que mais realizou descartes tanto em exclusões LGPD e números incorretos."""

df3 = pd.read_csv("nfemais.csv")
df3.head(10)

fig = px.scatter(df3, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df3, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

"""Em relação aos descartes em exclusões LGPD no setor NFeMais, há um funcionário que não possui nenhum registro em exclusões, ainda que sua entrada de leads é pequena, porém nos descartes em números incorretos seu descarte está razoável em relação a entrada de leads. Há uma discrepância (talvez pelo tempo do funcionário na empresa?), visto que outros dois funcionários possuem números altos de entradas e descartes em números incorretos."""

df4 = pd.read_csv("planilhaf.csv")
df4.head()

fig = px.scatter(df4, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df4, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

"""Em relação ao setor de planilhas, nos descartes de exclusões LGPD e números incorretos os funcionários que possuem registros de descartes estão em "mesmas posições", tal que Pedro Machado se encontra nos dois com mais descartes e maior entrada de leads neste ano.

"""

df5 = pd.read_csv("vendedores.csv")
df5.head()

fig = px.scatter(df5, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df5, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

df6 = pd.read_csv("trials.csv")
df6.head()

fig = px.scatter(df6, x = "exc_lgpd", y = "ent", size = "ent", color = 'exc_lgpd', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Exclusões LGPD  x Entradas de leads')
fig.update_xaxes(title = 'Exclusões LGPD')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

fig = px.scatter(df6, x = "num_inc", y = "ent", size = "ent", color = 'num_inc', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

"""No setor dos vendores, Wellington é o funcionário que mais apresenta registros de descartes, uma vez, que um funcionário dos vendedores, não é possível de visualizar no gráfico, pois ele apresenta 0 descartes nas duas opcçoes.

##Sobre os dados:

O banco de dados apresenta 11 observações e 31 variáveis, as quais são respectivamente: o dia de ínicio de cada mês até novembro e os nomes dos funcionários.
"""

df_mes = pd.read_csv("dado.csv")
df_mes.head(50)

df_mes.describe()

df_media = pd.read_csv("media2.csv")
df_media.head(50)

df_media.plot.scatter(x= 'mean', y= 'func')

import matplotlib.pyplot as plt

nomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
media = [217.36, 1796.00, 1088.63, 1603.00, 1048.54, 469.33, 816.66, 924.40, 1309.90, 1388.09, 206.20, 1141.36, 1129.30, 1372.66, 1718.63, 437.50, 857.88, 1099.20, 896.71, 1053.62, 1023.36, 583.66, 438.75, 1257.66, 872.33, 1458.25, 1026.63, 1924.12, 1182.36]
plt.plot(nomes, media, 'k--')
plt.plot (nomes,media, 'go')
plt.figure(figsize=(100, 4000))
plt.show()

import matplotlib.pyplot as plt

nomes = ["Alisson  Leal", "Ana Paula Ramos",	"Andressa Ely",	"Augusto Barreto",	"Beatriz Kowas",	"Brendon Silva",	"Clarine Mantai",	"Daniel Escobar",	"Eduarda Fragoso",	"Felipe Fiorini",	"Fernando Penz",	"Frederico Vargas",	"Gabriel Martins",	"Gabriel Padoin",	"Gabriele Motta",	"Henrique Lima",	"Jeniffer Soares",	"Jennifer Dallanora", "Kalleo Ethur",	"Kauhan Cunha",	"Matheus Mesquita",	"Milena Schuquel Machado",	"Paola Lanes Viaro",	"Patrícia Lima",	"Patrícia Melo",	"Pedro  Machado",	"Renata Lopes",	"Tamires Cattani",	"Wellington Reis"]
media = [217.36, 1796.00, 1088.63, 1603.00, 1048.54, 469.33, 816.66, 924.40, 1309.90, 1388.09, 206.20, 1141.36, 1129.30, 1372.66, 1718.63, 437.50, 857.88, 1099.20, 896.71, 1053.62, 1023.36, 583.66, 438.75, 1257.66, 872.33, 1458.25, 1026.63, 1924.12, 1182.36]
plt.plot(media, nomes, 'k--')
plt.plot (media,nomes, 'go')
plt.figure(figsize=(100, 4000))
plt.show()

"""Gráfico de análise através da médias do somatório da entrada de leads de cada funcionário. Fernando Penz se identifica com a menor média e Tamires com a maior média. """

fig = px.scatter(df_media, x = "mean", y = "mean", size = "mean", color = 'mean', 
               hover_name = "func", log_x = True, size_max = 60, width = 800)
fig.update_layout(title = 'Números incorretos  x Entradas de leads')
fig.update_xaxes(title = 'Números incorretos')
fig.update_yaxes(title = 'Entradas de leads')
fig.show()

df_media.plot.box(x='mean')

"""# **Análise mensal de cada funcionário**

##Sobre os dados:

O banco de dados apresenta 06 observações e 12 variáveis, tal qual são respectivamente, os setores e os meses do ano.

Observações: 
1. `canais_ob`: Setor de Canais Outband
1. `canais_ib`: Setor de Canais Inband
1. `nfemais`: Setor de NFeMais
1. `planilha`: Setor de Planilhas
1. `vendedor`: Setor de Vendedores
1. `trials`: Setor de Trials

Variáveis:
1. `jan`: Mês de janeiro
1. `fev`: Mês de fevereiro
1. `mar`: Mês de março
1. `abr`: Mês de abril
1. `maio`: Mês de maio
1. `jun`: Mês de junho
1. `jul`: Mês de julho
1. `ago`: Mês de agosto
1. `set`: Mês de setembro
1. `out`: Mês de outubro
1. `nov`: Mês de novembro
"""

dataframe = pd.read_csv("media_m_s.csv")
dataframe.head(6)

dataframe.describe()

"""Abaixo segue gráficos das médias de cada setor por cada mês:

##Canais OB
"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [1343,	1630.5,	1608.5, 605.66,	1102.66,	908,	1331.4,	628,	906.54,	906.36,	811.81]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

"""##Canais IB"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [590,	992.2,	1586.5,	1869,	1888,	1271.5,	691.5,	788.5,	887,	831,	719]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

"""## NFeMais"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [557.75,	5.25,	445.25,	1275.25,	1419,	860.5,	842.25,	900.5,	1466.35,	1490.75,	905.5]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

"""## Planilha"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [0, 0,	0,	0,	0,	0,	0,	519,	1072.5,	944.5,	818]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

"""## Vendedor"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [247.66,	689.66,	318.33,	257.66,	861,	265.66,	477.66,	840.66,	452,	1111.33,	872]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

"""## Trials"""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [1212.25,	1022,	1425.125,	1346.625,	1167.375,	963.125,	977.5,	1409.25,	1180.125,	1135.75,	701]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.show()

plt.figure()
plt.subplot(3,2,1)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [1343,	1630.5,	1608.5, 605.66,	1102.66,	908,	1331.4,	628,	906.54,	906.36,	811.81]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.subplot(3,2,2)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [590,	992.2,	1586.5,	1869,	1888,	1271.5,	691.5,	788.5,	887,	831,	719]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.subplot(3,2,3)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [557.75,	5.25,	445.25,	1275.25,	1419,	860.5,	842.25,	900.5,	1466.35,	1490.75,	905.5]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.subplot(3,2,4)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [0, 0,	0,	0,	0,	0,	0,	519,	1072.5,	944.5,	818]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.subplot(3,2,5)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [247.66,	689.66,	318.33,	257.66,	861,	265.66,	477.66,	840.66,	452,	1111.33,	872]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')
plt.subplot(3,2,6)
meses = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov"]
setor = [1212.25,	1022,	1425.125,	1346.625,	1167.375,	963.125,	977.5,	1409.25,	1180.125,	1135.75,	701]
plt.plot(meses, setor, 'k--')
plt.plot (meses,setor, 'go')

"""Cabais OB, Canais IB, 

NFeMais, Planilha,

Vendedor, Trials

##Análise descritiva dos gráficos:

Os canais OB possuem um aumento de janeiro a março, porém de março até abril apresenta - se uma queda agressiva, registrando menor valor de entrada de leads em todo o anos; e ao longo dos demais meses do ano, não apresenta números constantes e sim com aumento, recaída e sucessivamente. Entretanto, nos canais IB, possuem de janeiro até maio um aumento constante, apresentando uma queda contínua de maio até julho e no restante dos meses estabiliza em torno da entrada de 800 leads.

No setor de vendedores é possível visualizar e analisar que não mantém uma constante durante certo período do ano, tal qual, durante todo o período anual há uma crescente e descrescente nas entradas de leads e comparado com os outros setores, possui um número baixo de entrada de leads, chegando a até em torno de 1000.

O NFeMais possue uma evolução um pouco constante, tal qual de fevereiro até maio registra aumento constante, registrando queda em junho e se estabilizando durante os dois próximos meses, em seguida aumenta novamente. No gráfico possibilita visualização de que em 2 trimestres dos anos as quedas e aumentos são as mesmas.

Em relação ao setor de planilhas nota - se uma diferença bruta em relação aos demais setores, visto que, em 6 meses do ano não apresenta - se nenhum registro, e após dois meses ocorre um volume crecente de leads, indo de 0 até em torno de 1000 e decaíndo em seguida no próximo mês.

Em relaçao aos Trials, o seu gráfico é um pouco parecido com o do NFeMais, porém as quedas e aumentos em dois periódos dos anos são mais "aberto". Em fevereiro a março apresenta um aumento e tem uma queda constante por 4 meses e no mês de julho até agosto demonstra um aumento e logo após até dezembro vai se decaíndo aos poucos.

Nos meses de maio e outubro é quando ocorre números de entradas de leads parcialmente parecidos em todos os setores
"""
