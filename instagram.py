# Description: This script will open a browser and login to instagram. It will then search for a hashtag and like the first image.
# Descrição: Este script abrirá um navegador e fará login no Instagram. Em seguida, procurará uma hashtag e curtirá a primeira imagem.
import pyautogui
from pyautogui import ImageNotFoundException
import webbrowser
from time import sleep
# open page browser and open instagram
# abrir página do navegador e abrir o Instagram
webbrowser.open_new_tab('https://www.instagram.com/')
sleep(5)
# enter user
# inserir usuário
'''pyautogui.click(x=-975,y=363, duration=1)
sleep(1)
pyautogui.typewrite('user', interval=0.25)
sleep(1)'''
# enter password
# inserir senha
'''pyautogui.click(x=-1012,y=420, duration=1)
sleep(1)
pyautogui.typewrite('password', interval=0.25)
sleep(1)'''
# click login
# clicar em login
pyautogui.click(-952,470,duration=4)
sleep(5)
# click not now to no save browser
# clicar em não agora para não salvar o navegador
'''pyautogui.click(x=-1012,y=420, duration=1)
sleep(1)'''
# click not now to no save password
# clicar em não agora para não salvar a senha
pyautogui.click(-914,640,duration=1)
sleep(1)
# search for a hashtag
# procurar uma hashtag
pyautogui.click(-1383,345, duration=2)
sleep(1)
# click hastag
# clicar na hashtag
pyautogui.click(-1263,253, duration=1)
sleep(1)
pyautogui.typewrite('Nike', interval=0.25)
sleep(1)
# click coordinate first post of hashtag
# clicar na coordenada do primeiro post da hashtag
pyautogui.click(-1189,322, duration=2)
sleep(1)
# verify if the image is liked
# verificar se a imagem foi curtida
pyautogui.click(-1214,950, duration=2)
sleep(1)
# if the image is liked, do nothing and pause bot for 24 hours
# se a imagem foi curtida, não fazer nada e pausar o bot por 24 horas
try:
    heart = pyautogui.locateCenterOnScreen('heart.png')
except ImageNotFoundException:
    heart = None

sleep(1)
if heart is not None:
    sleep(86400)

    # if the image is not liked click like
    # se a imagem não foi curtida, clicar em curtir
else:
    pyautogui.click(-1055,669, duration=2)
    sleep(5)
    # if the image is not comment, comment image
    # se a imagem não foi comentada, comentar a imagem
    pyautogui.click(-999,673, duration=2)  # Coordenada para o campo de comentário
    sleep(1)
    pyautogui.click(-927,806, duration=2)
    sleep(1)
    pyautogui.typewrite('Nice post!', interval=0.25)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # pause bot for 24 hours
    # pausar o bot por 24 horas
    sleep(86400)

# logout of instagram
# fazer logout do Instagram
pyautogui.click(-1310,954, duration=2)  # Coordenada para o botão de logout
sleep(1)
# close browser
# fechar o navegador
pyautogui.hotkey('ctrl', 'w')
# after 24 hours, repeat process
# após 24 horas, repetir o processo