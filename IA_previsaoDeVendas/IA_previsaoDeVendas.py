"""
Passo a Passo de um Projeto de Ciência de Dados
Passo 1: Entendimento do Desafio
Passo 2: Entendimento da Área/Empresa
Passo 3: Extração/Obtenção de Dados
Passo 4: Ajuste de Dados (Tratamento/Limpeza)
Passo 5: Análise Exploratória
Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
Passo 7: Interpretação de Resultados

Projeto Ciência de Dados - Previsão de Vendas
-Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
-Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing
"""

# pip install matplotlib
# pip install seaborn
# pip install scikit-learn
# pip install pandas

#Importar a Base de dados
import pandas as pd
tabela = pd.read_csv(r"IA_previsaoDeVendas\advertising.csv")
print(tabela)

# Análise Exploratória
# Vamos tentar visualizar como as informações de cada item estão distribuídas
# Vamos ver a correlação entre cada um dos itens

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()

# outra forma de ver a mesma análise
# sns.pairplot(tabela)
# plt.show()


# Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# Separando em dados de treino e dados de teste

from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# Regressão Linear
# RandomForest (Árvore de Decisão)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias aritificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# Teste da AI e Avaliação do Melhor Modelo
# Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

from sklearn import metrics

# criar as previsoes
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))  

#Visualização Gráfica das Previsões

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

#Como fazer uma nova previsao?
# importar a nova_tabela com o pandas (a nova tabela tem que ter os dados de TV, Radio e Jornal)
# previsao = modelo_randomforest.predict(nova_tabela)
# print(previsao)
nova_tabela = pd.read_csv(r"IA_previsaoDeVendas\novos.csv")
print(nova_tabela)
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

#Qual a importância de cada variável para as vendas?

sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

# Caso queira comparar Radio com Jornal
# print(df[["Radio", "Jornal"]].sum())