"""
Automação Web e Busca de Informações com Python
Desafio:
Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:

Dólar
Euro
Ouro
Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing

Para isso, vamos criar uma automação web:

Usaremos o selenium
Importante: baixar o webdriver


pip install selenium
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# abrir um navegador
# navegador = webdriver.Chrome()

# caso queira deixar na mesma pasta do seu código
navegador = webdriver.Chrome("cotandoMoedasSelenium\chromedriver.exe")

"""
Se quiser que a automação seja feita em segundo plano, ou seja, sem aparecer
na tela, ative as seguintes linhas de código
"""
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)


navegador.get("https://www.google.com/")

# Passo 1: Pegar a cotação do Dólar
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Passo 3: Pegar a cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit()

"""
Agora vamos atualizar a nossa base de preços com as novas cotações
Importando a base de dados
"""
# Passo 4: Importar a lista de produtos
import pandas as pd

tabela = pd.read_excel("cotandoMoedasSelenium\Produtos.xlsx")
print(tabela)

"""
Atualizando os preços e o cálculo do Preço Final
"""
# Passo 5: Recalcular o preço de cada produto
# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)

print(tabela)

"""
Agora vamos exportar a nova base de preços atualizada

"""
# Passo 6: Salvar os novos preços dos produtos
tabela.to_excel("Produtos Novo.xlsx", index=False)
