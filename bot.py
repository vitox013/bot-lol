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
        [sg.Column([[sg.Checkbox('', key='top',pad=(0,0)), sg.Image('imgs/top.png',pad=((0,20),0)), sg.Checkbox('', key='jungle',pad=(0,0)), sg.Image('imgs/jungle.png',pad=((0,20),0)), sg.Checkbox('', key='mid',pad=(0,0)), sg.Image('imgs/mid.png',pad=((0,20),0)), sg.Checkbox('', key='botlane',pad=(0,0)), sg.Image('imgs/botlane.png',pad=((0,20),0)), sg.Checkbox('', key='sup',pad=(0,0)), sg.Image('imgs/sup.png',pad=((0,20),0)), sg.Checkbox('', key='all',pad=(0,0)), sg.Image('imgs/all.png',pad=((0,20),0))]],visible=True ,key='laneOptions')],

        [sg.Column([[sg.Button('Confirmar Lanes', font="Arial, 11", bind_return_key=True)]], justification='center', visible=True, key='buttonConfirmLanes')],
        [sg.Column([[sg.Text('',key='msgLanes')]], justification='center')],
        [sg.Column([[sg.Image('',key='imgLane1'),sg.Image('',key='imgLane2')]], justification='center')],
        [sg.Text("Primeira opção de campeão:")],
        [sg.Input(key='opcao1')],
        [sg.Text("Segunda opção de campeão(caso 1° seja banido):")],
        [sg.Input(key='opcao2')],
        [sg.Text("Banir quem?")],
        [sg.Input(key='ban')],
        [sg.Column([[sg.Button('Iniciar BOT', font="Arial, 11", bind_return_key=True, pad=(0, 10))]], justification='center')]
    ]

    return sg.Window('Informe os Campeões', layout, finalize=True, size=(460, 360), location=(2, 300), font=("Arial", 11), margins=(10, 20),icon=r'imgs/botIcon.ico')

def botTrabalhando():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Bot está trabalhando!")],
        [sg.Image("imgs/emote.png")],
        [sg.Text('',key='mensagem')],
        [sg.Button('Parar Bot', button_color=('white', 'red'))]
    ]
    return sg.Window('Bot rodando', layout, finalize=True, size=(360, 260),location=(-500, 300), element_padding=10, font="Arial, 11", element_justification='c',icon=r'imgs/botIcon.ico')

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
    if voltouParaFila():
        return False
    if selectFirstChampion != None:
        time.sleep(1)
        click(selectFirstChampion.left + 30, selectFirstChampion.top + 60, 1)

def buttonBan():
    buttonB = locateOnScreen(imagens['buttonBan'])
    click(buttonB.left + 50, buttonB.top + 30, 1)

def buttonConfirm():
    if voltouParaFila():
        return False
    time.sleep(1)
    buttonC = locateOnScreen(imagens['buttonConfirmLigado'])
    click(buttonC.left + 50, buttonC.top + 30, 1)

def openGame():
    pyautogui.press('win')

def laneSelection():
    global window, event, values, janela1, imagens

    lanesEsc = {}
    escolheuSo2 = False
    while True:
        while not escolheuSo2:
            print('No loope escolheuSo2')
            if event == sg.WIN_CLOSED:
                sys.exit()
            window,event,values = sg.read_all_windows()
            for x in values:
                if values[x] == True:
                    lanesEsc[x] = x
            if len(lanesEsc) == 2:
                if 'all' in lanesEsc:
                    janela1['msgLanes'].update('Selecione só PREENCHER')
                    lanesEsc = {}
                    print('Contem all em lanesEsc')
                else:
                    janela1['msgLanes'].update('Lanes confirmadas')
                    janela1['buttonConfirmLanes'].update(visible=False)
                    janela1['laneOptions'].update(visible=False)
                    janela1['imgLane1'].update(imagens['top'])
                    escolheuSo2 = True
            print(lanesEsc)    
        while event != 'Iniciar BOT':
            print('Esperando iniciar bot')
            window,event,values = sg.read_all_windows()
            escolhas = values
            if event == sg.WIN_CLOSED:
                sys.exit()
        return escolhas

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
        atualizaMsg('Voltou p/ fila, aguardando partida')
        return True
    else:
        return False
        
def guardarImgChampion():
    global boxPlayer
    champion = locateOnScreen(imagens['topIcon'])
    imgChampion = pyautogui.screenshot(region=(champion.left + 2, champion.top + 36, 67, 55))
    imgPlayer = locateOnScreen(imagens['barraLateral'])
    boxPlayer = pyautogui.screenshot(region=(imgPlayer.left+20,imgPlayer.top+18, 200, 70))
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
    time.sleep(1)
    search()
    pyautogui.write(championBan)
    selectChampion()
    buttonBan()
    pyautogui.moveTo(ban.left, ban.top, 1)
    if locateOnScreen(imagens['banirAliado']) != None:
        bCanc = locateOnScreen(imagens['cancelarBan'])
        print('Precisa cancelar ban')
        click(bCanc.left + 20, bCanc.top + 10, 1)
        

def championSelect(opcao1, opcao2):
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
    foiPickado = locateOnScreen(boxPlayer)
    search()
    if foiPickado != None:
        pyautogui.write(opcao1) 
        atualizaMsg(opcao1 + ' foi selecionado')
        print(opcao1 + ' foi selecionado')
    else:
        pyautogui.write(opcao2)
        atualizaMsg(opcao2 + ' foi selecionado')
        print(opcao2 + ' foi selecionado')
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
boxPlayer = None
imagens = loadImages()

janela3 = janelaInicial()
window, event, values = sg.read_all_windows(timeout=5000)
if event == sg.WINDOW_CLOSED:
    sys.exit()
elif event.startswith("URL "):
    webbrowser.open(url)
janela3.close()

janela1 = janelaChampions()
escolhas = laneSelection()

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
                championSelect(escolhas['opcao1'], escolhas['opcao2'])
            if verificaInicio():
                partidaIniciada = True
atualizaMsg('Partida será iniciada! Boa sorte!')
time.sleep(3)
atualizaMsg('Aplicativo será fechado! Até mais!')
time.sleep(3)