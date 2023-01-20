#pip install pyautogui
#pyperclip vem automatico com o pyautogui

#pip install openpyxl
#pip install pandas
#numpy e pytz vem automatico com pandas

#para quem usar o jupyter ao invés de print() use display()
#serve para formatar melhor o print
#jupyter deve ser instalado com o comando a seguir
#pip install jupyter
#e pode ser aberto no terminal com o comando a seguir
#jupyter notebook

"""
Use o código a seguir para descobrir qual a posição de um item que queira clicar
Lembre-se: a posição na sua tela é diferente da posição na minha tela
por isso, altere os valores indicados com comentários
"""
# time.sleep(5)
# print(pyautogui.position())

"""
Desafio:
Todos os dias, o nosso sistema atualiza as vendas do dia anterior. 
O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, 
assim que começar a trabalhar, com o faturamento e a quantidade de produtos 
vendidos no dia anterior
E-mail da diretoria: seugmail+diretoria@gmail.com
Local onde o sistema disponibiliza as vendas do dia anterior: 
https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado
"""

import pyautogui
import pyperclip
import time

try:
    pyautogui.PAUSE = 1

    # pyautogui.click -> clicar
    # pyautogui.press -> apertar 1 tecla
    # pyautogui.hotkey -> conjunto de teclas
    # pyautogui.write -> escreve um texto

    # Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive)
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    #alerta de inicialização
    pyautogui.alert("Atenção, não mexa em nada até a automação acabar!")
    #se seu google tiver a inicialização com esolha de perfil, habilite a linha a seguir
    #pyautogui.click(x=435, y=369) #altere as coordenadas para selecionar seu perfil
    pyautogui.hotkey("ctrl", "t")
    pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    time.sleep(5)

    # Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
    pyautogui.click(x=435, y=369, clicks=2) #coloque as cordenadas referente a tela de seu computador
    time.sleep(2)

    # Passo 3: Fazer o download da base de vendas
    pyautogui.click(x=435, y=369, button='right') # clicar no arquivo com botao direito
    pyautogui.click(x=684, y=928) # clicar no fazer download
    time.sleep(5) # esperar o download acabar
    #se seu computadar não pede para confirmar a permissão de salvar, desative a linha a seguir
    pyautogui.press('enter') # clicar em salvar
    time.sleep(5) # esperar o download acabar

    """
    Vamos agora ler o arquivo baixado para pegar os indicadores
    - Faturamento
    - Quantidade de Produtos
    """

    # Passo 4: Importar a base de vendas pro Python
    import pandas as pd

    #na linha a seguir coloque a url do local de seu arquivo
    tabela = pd.read_excel(r"Caminho onde seu arquivo é salvo por padrão")

    print(tabela)

    # Passo 5: Calcular os indicadores da empresa
    faturamento = tabela["Valor Final"].sum()
    print(faturamento)
    quantidade = tabela["Quantidade"].sum()
    print(quantidade)

    """
    Vamos agora enviar um e-mail pelo gmail
    """

    # Passo 6: Enviar um e-mail para a diretoria com os indicadores de venda

    # abrir aba
    pyautogui.hotkey("ctrl", "t")

    # entrar no link do email - https://mail.google.com/mail/u/0/#inbox
    pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(5)

    # clicar no botão escrever
    pyautogui.click(x=167, y=244)

    # preencher as informações do e-mail
    pyautogui.write("Coloque o Email Destinatário")
    pyautogui.press("tab") # selecionar o email

    pyautogui.press("tab") # pular para o campo de assunto
    pyperclip.copy("Relatório de Vendas")
    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("tab") # pular para o campo de corpo do email

    texto = f"""
    Prezados,

    Segue relatório de vendas.
    Faturamento: R${faturamento:,.2f}
    Quantidade de produtos vendidos: {quantidade:,}

    Qualquer dúvida estou à disposição.
    Att.,
    Lucas Ribeiro
    """

    # formatação dos números (moeda, dinheiro)

    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")

    # enviar o e-mail
    pyautogui.hotkey("ctrl", "enter")

    #acabou
    pyautogui.alert("Pronto, código executado com sucesso!")
except Exception:
    pyautogui.alert("Verifique seu código, algo deu errado na execução!\n"
    "Dica: confira se você alterou o caminho do arquivo\n"
    "Ou se você alterou as coordenadas de clique corretamente")



