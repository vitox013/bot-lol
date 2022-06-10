from os import system
from select import select
from shutil import move
from numpy import size
import pyautogui
import time
import PySimpleGUI as sg
import sys

def janelaInicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Bot criado por Viteeeera (https://github.com/vitox013/bot-lol)\n\nVá lá no banheiro que o bot aceitará sozinho caso ache uma partida")]
    ]

def janelaChampions():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Primeira opção de campeão:")],
        [sg.Input(key='opcao1',)],
        [sg.Text("Segunda opção de campeão:")],
        [sg.Input(key='opcao2')],
        [sg.Text("Banir quem?")],
        [sg.Input(key='ban')],
        [sg.Button('Iniciar BOT', font="Arial, 11")]
    ]
    return sg.Window('Informe os Campeões', layout, finalize=True, size=(310, 260), location=(2, 300), element_justification='c',element_padding=5, font="Arial, 11")

def botTrabalhando():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Bot está trabalhando!")],
        [sg.Text('',key='mensagem')],
        [sg.Button('Parar Bot', button_color=('white', 'red'), )]
    ]
    return sg.Window('Bot rodando', layout, finalize=True, size=(310, 260),location=(2, 300), element_justification='c', element_padding=5, font="Arial, 11")

# ======================= BOT =================================
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    

def search():
    buttonSearched = pyautogui.locateOnScreen('imgs/buttonSearch.png', confidence=0.8)
    click(buttonSearched.left + 30, buttonSearched.top + 10)

def selectChampion():
    selectFirstChampion = pyautogui.locateOnScreen('imgs/topIcon.png', confidence=0.8)
    if selectFirstChampion != None:
        time.sleep(2)
        click(selectFirstChampion.left + 30, selectFirstChampion.top + 60)

def buttonBan():
    time.sleep(1)
    buttonB = pyautogui.locateOnScreen('imgs/buttonBan.png', confidence=0.8)
    click(buttonB.left + 50, buttonB.top + 30)

def buttonConfirm():
    time.sleep(1)
    buttonC = pyautogui.locateOnScreen('imgs/buttonConfirmLigado.png', confidence=0.8)
    click(buttonC.left + 50, buttonC.top + 30)
    print("Champion selecionado")

def verificaTela():
    readWindows()
    if event == sg.WIN_CLOSED:
        sys.exit()
    print('Procurando partida')
    button_pos = pyautogui.locateOnScreen('imgs/button.png', confidence=0.8)
    if button_pos != None:
        if button_pos != None:
            click(button_pos.left + 80, button_pos.top + 20)
            time.sleep(2)
            pyautogui.moveTo(button_pos.left -30, button_pos.top + 100)
            atualizaMsg("Partida encontrada e aceita")
        return True
    print('nao achei')
    return False

def verificaSeTodosAceitaram():
    atualizaMsg("Verificando se todos aceitaram")
    print('Verificando se todos aceitaram')
    while True:
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()
        flag = pyautogui.locateOnScreen('imgs/flagTodosAceitaram.png', confidence=0.8)
        if flag != None:
            atualizaMsg('Todos aceitaram')
            return True
        flagNao = pyautogui.locateOnScreen('imgs/retornouFila.png', confidence=0.8)
        if flagNao != None:
            return False

def guardarImgChampion():
    champion = pyautogui.locateOnScreen('imgs/topIcon.png', confidence=0.8)
    imgChampion = pyautogui.screenshot(region=(champion.left + 2, champion.top + 36, 67, 55))
    return imgChampion

def declareChampion(champion):
    atualizaMsg('Declarando champion')
    declareImg = pyautogui.locateOnScreen('imgs/declareChampion.png', confidence=0.8)
    while declareImg == None and not verificaTela():
        declareImg = pyautogui.locateOnScreen('imgs/declareChampion.png', confidence=0.8)
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()

    time.sleep(2)    
    search()
    pyautogui.write(champion)
    time.sleep(3)
    img = guardarImgChampion()
    time.sleep(1)
    selectChampion()
    return img
   
def banChampion(championBan):
    atualizaMsg('Banindo')
    ban = pyautogui.locateOnScreen('imgs/ban.png', confidence=0.8)
    while ban == None and not verificaTela():
        ban = pyautogui.locateOnScreen('imgs/ban.png', confidence=0.8)
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()
    time.sleep(2)
    search()
    pyautogui.write(championBan)
    selectChampion()
    time.sleep(3)
    buttonBan()
    pyautogui.moveTo(ban.left, ban.top)

def verificaSeChampFoiBanido(champion):
    atualizaMsg('Aguardando as confirmacoes de ban')
    while True:
        aguardando = pyautogui.locateOnScreen('imgs/banimentosconfirmados.png', confidence=0.8)
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()
        if aguardando != None:
            break
    atualizaMsg('Verificando se o champion foi banido')

    while True:
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()
        img = pyautogui.locateOnScreen(champion, confidence=0.8)
        aguardando = pyautogui.locateOnScreen('imgs/banimentosconfirmados.png', confidence=0.8)
        if img != None:
            atualizaMsg('Seu champion foi banido')
            return True
        if aguardando == None:
            atualizaMsg('Seu champion não foi banido')
            return False
   
def championSelect(opcao):
    confirmar1 = pyautogui.locateOnScreen('imgs/escolha.png', confidence=0.8)
    atualizaMsg("Esperando minha vez para selecionar")
    while confirmar1 == None and not verificaTela():
        readWindows()
        if event == sg.WIN_CLOSED:
            sys.exit()
        if verificaTela():
            return False
        confirmar1 = pyautogui.locateOnScreen('imgs/escolha.png', confidence=0.8)

    atualizaMsg('Minha vez de escolher um campeao')
    time.sleep(2)
    search()
    pyautogui.write(opcao)
    selectChampion()
    time.sleep(2)
    buttonConfirm()

def verificaInicio():
    image_pos = pyautogui.locateOnScreen('imgs/verificaInicio.png', confidence=0.8)
    image_pos2 = pyautogui.locateOnScreen('imgs/verificaInicio2.png', confidence=0.8)
    image_pos3 = pyautogui.locateOnScreen('imgs/verificaInicio3.png', confidence=0.8)
    if image_pos != None or image_pos2 != None or image_pos3 != None:
        return False
    return True

def atualizaMsg(mensagem):
    global janela2
    janela2['mensagem'].update(mensagem)
    readWindows()

def readWindows():
    global window, event, escolhas
    window, event,escolhas = sg.read_all_windows(timeout=10)

janela1, janela2 = janelaChampions(), None
partidaIniciada = False
window, event,escolhas = sg.read_all_windows()


if event == sg.WIN_CLOSED:
    sys.exit()

janela2 = botTrabalhando()
janela1.close()
atualizaMsg('Aguardando encontrar partida para aceitar')
readWindows()

while not partidaIniciada:
    if verificaTela():
        if verificaSeTodosAceitaram():
            img = declareChampion(escolhas['opcao1'])
            banChampion(escolhas['ban'])
            banido = verificaSeChampFoiBanido(img)
            if banido == True:
                championSelect(escolhas['opcao2'])
            else:
                championSelect(escolhas['opcao1'])
            partidaIniciada = True
atualizaMsg('Partida será iniciada! Boa sorte!')
time.sleep(3)
atualizaMsg('Aplicativo será fechado! Até mais!')
time.sleep(3)




