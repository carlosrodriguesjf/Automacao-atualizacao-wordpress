# PROJETO AUTOMAÇÃO DA ATUALIZAÇÃO DO WORDPRESS

import pyautogui
import pyperclip
import webbrowser
from time import sleep

# constantes

lista = []
lista_codigo = []

# acessar o siga e mudar de páginas

webbrowser.open('https://siga.ufjf.br')

# leitura dos arquivos com login e senha

with open('login_siga.txt','r',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:
        lista.append(linha)




# acesso ao siga

sleep(2)
pyautogui.click(381,467,duration=2)
pyautogui.write(lista[0])

sleep(1)
pyautogui.click(560,565,duration=2)
pyautogui.write(lista[1])

pyautogui.click(643,673, duration=2)
sleep(2)

# clicar em sites

pyautogui.click(1350,307, duration=2)
sleep(2)

# clicar em meus sites

pyautogui.click(81,300, duration=2)
sleep(2)

# clicar no site central de atendimento JF

pyautogui.click(90,357, duration=2)
sleep(2)

# mover para paginas

pyautogui.moveTo(54,437, duration=2)
sleep(2)

# clicar em todas as paginas

pyautogui.click(293,436, duration=2)
sleep(2)

# clicar duas vezes na página de rolagem

pyautogui.doubleClick(1906,964, duration=2)
sleep(2)

# clicar em Formularios

pyautogui.click(318,702, duration=2)
sleep(2)

# clicar na area de codigo

pyautogui.click(814,795, duration=2)
sleep(2)

# apertar control + A

pyautogui.hotkey('ctrl','a')
sleep(2)

# apertar delete

pyautogui.hotkey('del')
sleep(2)


# clicar na area de codigo

pyautogui.click(814,795, duration=2)
sleep(2)



# ler arquivo com atualização

with open('pagina_alterada.txt','r',newline='',encoding='utf-8') as arquivo_codigo:
    for linha_codigo in arquivo_codigo:
        lista_codigo.append(linha_codigo)





# colar arquivo com a atualização


#clicar em atualizar







# agendar a automatizacao