from os import listdir
from select import select
from shutil import move
from tkinter import image_names
from numpy import size
import pyautogui
import time
import PySimpleGUI as sg
import sys
import webbrowser

url = 'https://github.com/vitox013'

def janelaInicial():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text('Bot criado por viteeera (GitHub)', tooltip=url, enable_events=True,key=f'URL {url}', font=("Arial", 11, "underline"))],
        [sg.Image('imgs/okTeemo.png')],
        [sg.Text('Vá lá buscar seu café que eu aceito a fila')]
    ]
    return sg.Window('Queue Acceptor', layout, finalize=True,size=(360, 260), location=(2, 300),element_padding=20, font=("Arial", 11), element_justification='c', icon=r'imgs/botIcon.ico')

def janelaChampions():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Primeira opção de campeão:")],
        [sg.Input(key='opcao1')],
        [sg.Text("Segunda opção de campeão(caso 1° seja banido):")],
        [sg.Input(key='opcao2')],
        [sg.Text("Banir quem?")],
        [sg.Input(key='ban')],
        [sg.Column([[sg.Button('Iniciar BOT', font="Arial, 11", bind_return_key=True, pad=(0, 10))]], justification='center')]
    ]
    return sg.Window('Informe os Campeões', layout, finalize=True, size=(360, 260), location=(2, 300), font=("Arial", 11), margins=(10, 20),icon=r'imgs/botIcon.ico')

def botTrabalhando():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Bot está trabalhando!")],
        [sg.Image("imgs/emote.png")],
        [sg.Text('',key='mensagem')],
        [sg.Button('Parar Bot', button_color=('white', 'red'))]
    ]
    return sg.Window('Bot rodando', layout, finalize=True, size=(360, 260),location=(2, 300), element_padding=10, font="Arial, 11", element_justification='c',icon=r'imgs/botIcon.ico')

def easterEgg():
    sg.theme("DarkRed2")
    layout = [
        [sg.Text("POR FAVOR NAO FEEDE DE YASUO")],
        [sg.Text("NO MID IGUAL O CHRIS IRADO")],
        
    ]
    return sg.Window('NAO FEEDE PFV', layout, finalize=True, size=(360, 260),location=(2, 300), element_padding=30, font="Arial, 13", element_justification='c', margins=(0,0),icon=r'imgs/botIcon.ico')

# ======================= BOT =================================
def click(x, y, m):
    pyautogui.moveTo(x, y, m)
    pyautogui.click()

def locateOnScreen(imagem):
    return pyautogui.locateOnScreen(imagem, confidence=0.8)

def removeSuffix(inputString, suffix):
    if suffix and inputString.endswith(suffix):
        return inputString[:-len(suffix)]
    return inputString

def loadImages(dirPath='./imgs/'):
    fileNames = listdir(dirPath)
    targets = {}

    for file in fileNames:
        path = 'imgs/' + file
        targets[removeSuffix(file, '.png')] = path
    return targets

def search():
    buttonSearched = locateOnScreen(imagens['buttonSearch'])
    click(buttonSearched.left + 30, buttonSearched.top + 10, 1)

def selectChampion():
    selectFirstChampion = locateOnScreen(imagens['topIcon'])
    if selectFirstChampion != None:
        time.sleep(2)
        click(selectFirstChampion.left + 30, selectFirstChampion.top + 60, 1)

def buttonBan():
    time.sleep(1)
    buttonB = locateOnScreen(imagens['buttonBan'])
    click(buttonB.left + 50, buttonB.top + 30, 1)

def buttonConfirm():
    time.sleep(1)
    buttonC = locateOnScreen(imagens['buttonConfirmLigado'])
    click(buttonC.left + 50, buttonC.top + 30, 1)
    atualizaMsg("Champion selecionado")

def verificaTela():
    readWindows()
    if event == sg.WIN_CLOSED or event == 'Parar Bot':
        sys.exit()
    button_pos = locateOnScreen(imagens['button'])
    if button_pos != None:
        if button_pos != None:
            click(button_pos.left + 80, button_pos.top + 20, 0)
            time.sleep(2)
            pyautogui.moveTo(button_pos.left -30, button_pos.top + 100,0)
            atualizaMsg("Partida encontrada e aceita")
        return True
    return False

def verificaSeTodosAceitaram():
    atualizaMsg("Verificando se todos aceitaram")
    while True:
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
        flag = locateOnScreen(imagens['flagTodosAceitaram'])
        if flag != None:
            atualizaMsg('Todos aceitaram')
            return True
        if voltouParaFila():
            atualizaMsg('Recusaram, aguardando partida para aceitar')
            return False

def voltouParaFila():
    flagFila = locateOnScreen(imagens['retornouFila'])
    if flagFila != None:
        return True
    else:
        return False
        
def guardarImgChampion():
    champion = locateOnScreen(imagens['topIcon'])
    imgChampion = pyautogui.screenshot(region=(champion.left + 2, champion.top + 36, 67, 55))
    return imgChampion

def declareChampion(champion):
    global imgOpcao1
    atualizaMsg('Declarando champion')
    declareImg = locateOnScreen(imagens['declareChampion'])
    while declareImg == None and not verificaTela():
        declareImg = locateOnScreen(imagens['declareChampion'])
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
    time.sleep(1)    
    search()
    pyautogui.write(champion)
    time.sleep(2)
    if voltouParaFila():
        return False
    imgOpcao1 = guardarImgChampion()
    selectChampion()
    return True
   
def banChampion(championBan):
    atualizaMsg('Banindo')
    ban = locateOnScreen(imagens['ban']) 
    while ban == None and not verificaTela():
        ban = locateOnScreen(imagens['ban']) 
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
    time.sleep(2)
    search()
    pyautogui.write(championBan)
    selectChampion()
    time.sleep(3)
    buttonBan()
    pyautogui.moveTo(ban.left, ban.top, 1)

def verificaSeChampFoiBanido(champion):
    atualizaMsg('Aguardando as confirmacoes de ban')
    while True:
        aguardando = locateOnScreen(imagens['banimentosconfirmados'])
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
        if aguardando != None:
            break
    atualizaMsg('Verificando se o champion foi banido')

    while True:
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
        img = pyautogui.locateOnScreen(champion, confidence=0.8)
        aguardando = locateOnScreen(imagens['banimentosconfirmados']) 
        if img != None:
            atualizaMsg('Seu champion foi banido')
            return True
        if aguardando == None:
            atualizaMsg('Seu champion não foi banido')
            return False
   
def championSelect(opcao):
    confirmar1 = locateOnScreen(imagens['escolha']) 
    atualizaMsg("Esperando minha vez para selecionar")
    while confirmar1 == None:
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
        if voltouParaFila():
            return False
        confirmar1 = locateOnScreen(imagens['escolha']) 

    atualizaMsg('Minha vez de escolher um campeao')
    time.sleep(1)
    search()
    pyautogui.write(opcao)
    selectChampion()
    buttonConfirm()

def verificaInicio():
    while True:
        readWindows()
        if event == sg.WIN_CLOSED or event == 'Parar Bot':
            sys.exit()
        retornouFila = locateOnScreen(imagens['retornouFila']) 
        if retornouFila != None:
            return False
        image_pos = locateOnScreen(imagens['verificaInicio']) 
        image_pos2 = locateOnScreen(imagens['verificaInicio2']) 
        image_pos3 = locateOnScreen(imagens['verificaInicio3']) 
        if image_pos != None or image_pos2 != None or image_pos3 != None:
            return True

def atualizaMsg(mensagem):
    global janela2
    janela2['mensagem'].update(mensagem)
    readWindows()

def readWindows():
    global window 
    global event 
    global values
    window, event, values = sg.read_all_windows(timeout=1)

global imagens
imgOpcao1 = None
imagens = loadImages()

janela3 = janelaInicial()
window, event, escolhas = sg.read_all_windows(timeout=5000)
if event == sg.WINDOW_CLOSED:
    sys.exit()
elif event.startswith("URL "):
    webbrowser.open(url)
janela3.close()

janela1 = janelaChampions()
window,event,values = sg.read_all_windows()
escolhas = values

if escolhas['opcao1'].lower() == 'yasuo':
    easter = easterEgg()
    window, event, values = sg.read_all_windows(timeout=3000)
    easter.close()

if event == sg.WINDOW_CLOSED:
        sys.exit()
janela2 = botTrabalhando()
janela1.close()
atualizaMsg('Aguardando encontrar partida para aceitar')
readWindows()
partidaIniciada = False

while not partidaIniciada:
    if verificaTela():
        if verificaSeTodosAceitaram():
            if declareChampion(escolhas['opcao1']):
                banChampion(escolhas['ban'])
                print(imgOpcao1)
            if verificaSeChampFoiBanido(imgOpcao1):
                championSelect(escolhas['opcao2'])
            else:
                championSelect(escolhas['opcao1'])
            if verificaInicio():
                partidaIniciada = True
atualizaMsg('Partida será iniciada! Boa sorte!')
time.sleep(3)
atualizaMsg('Aplicativo será fechado! Até mais!')
time.sleep(3)