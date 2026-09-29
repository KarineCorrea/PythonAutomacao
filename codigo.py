# bibliotecas = pacotes de codigo
# pip install pyautogui


import pyautogui
import time
# pyautogui.click()  # clicar
# pyautogui.write('Hello World')  # escrever
# pyautogui.press('enter')  # apertar tecla
# pyautogui.hotkey('ctrl', 'c')  # apertar varias teclas
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# passo a passo do seu programa
# passo 1: Entrar no sistema da empresa
# abriria o navegador

pyautogui.press('win')  # apertar tecla windows
pyautogui.write('chrome')  # escrever
pyautogui.press('enter')  # apertar tecla enter

pyautogui.write(link)
pyautogui.press('enter')  # apertar tecla enter
# fazer pausa maior na pagina do site
time.sleep(5)  # esperar 5 segundos


#passo 2 fazer login
pyautogui.click(x=673, y=376)  # clicar no campo de email
pyautogui.write('karine@gmail.com')
pyautogui.press('tab')
pyautogui.write('karine')
pyautogui.press('tab')
pyautogui.press('enter')  # apertar tecla enter
# fazer pausa maior na pagina do site
time.sleep(5)  # esperar 5 segundos

#passo 3 banco de dados tabela
# pip install pandas openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    # passo 4 consultar abel
    pyautogui.click(x=552, y=261)
    codigo = tabela.loc[linha, "codigo"]
    #codigo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")

    pyautogui.press("enter")  # apertar tecla enter
    pyautogui.scroll(5000)