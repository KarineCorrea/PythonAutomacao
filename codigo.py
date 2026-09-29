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
pyautogui.click(x=674, y=447)
pyautogui.write('karine@gmail.com')
pyautogui.press('tab')
pyautogui.write('karine')
pyautogui.press('tab')
# fazer pausa maior na pagina do site
time.sleep(5)  # esperar 5 segundos

#passo 3 banco de dados tabela
# pip install pandas openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# passo 4 consultar abela

pyautogui.click(x=682, y=301)
pyautogui.write('celular')