from os import listdir
import pyautogui
import time
import PySimpleGUI as sg
import sys
import webbrowser
import pygetwindow

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
        [sg.Column([[sg.Text('Selecione lane principal',key='mensagemLane', font=('Arial',16, 'underline'))]], visible=True, key='msgGrandes')],
        [sg.Column([[sg.Radio('','lanes', key='top',pad=(0,0)), sg.Image('imgs/top.png',pad=((0,20),0)), sg.Radio('', 'lanes', key='jungle',pad=(0,0)), sg.Image('imgs/jungle.png',pad=((0,20),0)), sg.Radio('', 'lanes',key='mid',pad=(0,0)), sg.Image('imgs/mid.png',pad=((0,20),0)), sg.Radio('', 'lanes', key='botlane',pad=(0,0)), sg.Image('imgs/botlane.png',pad=((0,20),0)), sg.Radio('', 'lanes', key='sup',pad=(0,0)), sg.Image('imgs/sup.png',pad=((0,20),0)), sg.Radio('', 'lanes', key='all',pad=(0,0)), sg.Image('imgs/all.png',pad=((0,20),0))]],visible=True ,key='laneOptions')],

        [sg.Column([[sg.Button('Confirmar Lane', font="Arial, 11", bind_return_key=True)]], justification='center', visible=True, key='buttonConfirmLanes')],
        [sg.Column([[sg.Text('', key='msgLanes')]], visible=False, key='msgLanes1',justification='center')],
        [sg.Column([[sg.Image('',key='imgLane1'),sg.Image('',key='imgLane2')]], visible=False, key='imgLanes',justification='center')],
        [sg.Column([[sg.Text('Selecione modo de jogo', font=('Arial',16, 'underline'),key='msgModo')]], visible=True,key='msgGrandeModo')],
        [sg.Radio('Escolha alternada', 'modosDeJogo', disabled=True,key='escolhaAlternada', pad=((0,5),0))],
        [sg.Radio('Ranqueada solo/duo', 'modosDeJogo',disabled=True, key='soloDuo',pad=((13,0),0))],
        [sg.Radio('Ranqueada flexível', 'modosDeJogo',disabled=True, key='flex')],
        [sg.Text("Primeira opção de campeão:")],
        [sg.Input(key='opcao1')],
        [sg.Text("Segunda opção de campeão(caso 1° seja banido):")],
        [sg.Input(key='opcao2')],
        [sg.Text("Banir quem?")],
        [sg.Input(key='ban')],
        [sg.Column([[sg.Button('Iniciar BOT', font="Arial, 11", bind_return_key=True, visible=False,pad=(0, 10),focus=True)]], justification='center')]
    ]

    return sg.Window('Informe os Campeões', layout, finalize=True,  location=(2, 300), font=("Arial", 11), margins=(10, 20),icon=r'imgs/botIcon.ico',element_justification='c')

def botTrabalhando():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Bot está trabalhando!")],
        [sg.Image("imgs/emote.png")],
        [sg.Text('',key='mensagem')],
        [sg.Button('Parar Bot', button_color=('white', 'red'))]
    ]
    return sg.Window('Bot rodando', layout, finalize=True, size=(360, 260),location=(2, 300), element_padding=10, font="Arial, 11", element_justification='c',icon=r'imgs/botIcon.ico')

# ======================= FUNCÕES GENERICAS =================================
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

def hideLanes():
    global janela1
    janela1['buttonConfirmLanes'].update(visible=False)
    janela1['buttonConfirmLanes'].hide_row()
    janela1['laneOptions'].update(visible=False)
    janela1['laneOptions'].hide_row()
    janela1['msgGrandes'].update(visible=False)
    janela1['msgGrandes'].hide_row()

def hideModos():
    global janela1
    janela1['escolhaAlternada'].update(disabled=True)
    janela1['flex'].update(disabled=True)
    janela1['soloDuo'].update(disabled=True)

def showModos():
    global janela1
    janela1['escolhaAlternada'].update(disabled=False)
    janela1['flex'].update(disabled=False)
    janela1['soloDuo'].update(disabled=False)

def attMsg(msg):
    global janela1
    janela1['msgLanes'].update(msg)
    janela1['msgLanes1'].update(visible=True)
    janela1['imgLanes'].update(visible=True)

def eventListenerFecharJogo():
    global event
    if event == sg.WIN_CLOSED or event == 'Parar Bot':
        sys.exit()

def jogoAberto():
    title = 'League of Legends'

    window = pygetwindow.getWindowsWithTitle(title=title)
    if window == []:
        print('Jogo não está aberto')
        return False
    else:
        window = pygetwindow.getWindowsWithTitle(title=title)[0]
        window.restore()
        return True


# ======================= FUNÇÕES BOT RODANDO =================================
def verificaSeJogoAberto():
    jogoAberto = locateOnScreen(imagens['verificaJogoAberto'])
    if jogoAberto != None:
        print('Jogo já está aberto')
        return True
    return False

def verificaSitAtual():
    if locateOnScreen(imagens['jogar']) != None:
        print('Precisa clicar em play')
        return 'clicar em play'
    elif locateOnScreen(imagens['grupo']) != None:
        print('Precisa clicar em grupo')
        return 'grupo'
    elif locateOnScreen(imagens['telaModoJogo']) != None:
        print('Precisar selecionar modo')
        return 'selecionar modo'
    elif locateOnScreen(imagens['saguao']) != None:
        print('Está no saguao')
        return 'no saguao'

def laneSelection():
    global window, event, values, janela1, imagens, precisaModo
    lanesEsc = []
    if not verificarSePodeStartar() or locateOnScreen(imagens['laneSelect']) != None:
        if locateOnScreen(imagens['telaModoJogo']) == None and locateOnScreen(imagens['saguao']) != None or locateOnScreen(imagens['grupo']) != None:
            hideModos()
            janela1['msgModo'].update('Modo de jogo já selecionado')
        while True:
            hideModos()
            while True:
                eventListenerFecharJogo()
                window,event,values = sg.read_all_windows()
                for x in values:
                    if values[x] == True:
                        lanesEsc.append(x)
                if len(lanesEsc) == 1:
                    if 'all' in lanesEsc:
                        attMsg('Lane confirmada')
                        janela1['mensagemLane'].update('')
                        hideLanes()
                        janela1['imgLane1'].update(imagens[lanesEsc[0]])
                        return lanesEsc
                    else:
                        janela1['mensagemLane'].update('Selecione lane secundária')
                elif len(lanesEsc) == 2:
                    if lanesEsc[0] == lanesEsc[1]:
                        janela1['mensagemLane'].update('Selecione lane principal novamente')
                        attMsg('Selecione Lanes Diferentes')
                        lanesEsc = []
                    else:
                        janela1['mensagemLane'].update('')
                        attMsg('Lanes confirmadas')
                        if locateOnScreen(imagens['saguao']) == None:
                            showModos()
                            precisaModo = True
                        if locateOnScreen(imagens['grupo']) != None:
                            hideModos()
                            janela1['msgModo'].update('Modo de jogo já selecionado')
                            precisaModo = False
                        hideLanes()
                        janela1['Iniciar BOT'].update(visible=True)
                        janela1['imgLane1'].update(imagens[lanesEsc[0]])
                        janela1['imgLane2'].update(imagens[lanesEsc[1]])
                        return lanesEsc
    else:
        hideLanes()
        hideModos()
        janela1['msgModo'].update('Modo de jogo já selecionado')
        precisaModo = False
        janela1['mensagemLane'].update('')

def championChoices():
    global window, event, values, janela1, imagens, precisaModo
    while event != 'Iniciar BOT':
        window,event,values = sg.read_all_windows()
        escolhas = values
        eventListenerFecharJogo()
        print(escolhas)
        if precisaModo:
            if escolhas['escolhaAlternada'] == True or escolhas['soloDuo'] == True or escolhas['flex'] == True:
                return escolhas
            else:
                janela1['msgModo'].update('SELECIONE MODO DE JOGO')
                event = None
        
    

def openGame():
    pyautogui.press('win')
    pyautogui.write('League of Legends')
    time.sleep(1)
    pyautogui.press('enter')
    
def clickOnPlay():
    atualizaMsg('Clicando em JOGAR')
    while True:
        readWindows()
        eventListenerFecharJogo()
        buttonPlay = locateOnScreen(imagens['jogar'])
        if buttonPlay != None:
            click(buttonPlay.left + 20, buttonPlay.top + 10, 1)
            break

def selectMode():
    global escolhas
    atualizaMsg('Selecionando modo de jogo')
    selecionou = False
    time.sleep(2)
    while not selecionou:
        readWindows()
        eventListenerFecharJogo()
        if escolhas['escolhaAlternada']:
            opcao = locateOnScreen(imagens['alternada'])
            click(opcao.left, opcao.top + 10, 1)
            selecionou = True
        elif escolhas['soloDuo']:
            opcao = locateOnScreen(imagens['rankedSolo3'])
            click(opcao.left, opcao.top + 10, 1)
            selecionou = True
        elif escolhas['flex']:
            opcao = locateOnScreen(imagens['rankedFlex'])
            click(opcao.left + 20, opcao.top + 10, 1)
            selecionou = True

    while True:
        print('Procurando botao confirmar')
        readWindows()
        eventListenerFecharJogo()
        buttonC = locateOnScreen(imagens['initialConfirm'])
        if buttonC != None:
            click(buttonC.left + 130, buttonC.top + 10, 1)
            break

def verificaAvisoAutoFill():
    time.sleep(1)
    notShow = locateOnScreen(imagens['notShowAgain'])
    readWindows()
    eventListenerFecharJogo()
    if notShow != None:
        click(notShow.left + 20, notShow.top + 5, 1)
    imgEntendido = locateOnScreen(imagens['avisoAutoFill'])
    if imgEntendido != None:
        click(imgEntendido.left + 20, imgEntendido.top + 10, 1)

def selecionarLanes():
    atualizaMsg('Selecionando as lanes')
    lane1 = locateOnScreen(imagens['laneSelect'])

    if lane1 != None:
        while True:
            readWindows()
            eventListenerFecharJogo()
            click(lane1.left - 15, lane1.top + 10, 1)
            time.sleep(0.5)
            imgLane1 = locateOnScreen(imagens[laneEsc[0]])
            if laneEsc[0] == 'all':
                click(imgLane1.left + 5, imgLane1.top + 10, 1)
                break
            else:
                click(imgLane1.left, imgLane1.top + 10, 1)
                click(lane1.left + 10, lane1.top + 10, 1)
                time.sleep(0.5)
                imgLane2 = locateOnScreen(imagens[laneEsc[1]])
                click(imgLane2.left + 5, imgLane2.top + 10, 1)
                break

def verificarSePodeStartar():
    global janela1
    imgButton = pyautogui.locateOnScreen('imgs/encontrarPartida.png', confidence=0.9)
    if imgButton != None:
        print('Usuario já selecionou lane')
        janela1['Iniciar BOT'].update(visible=True)
        return True
    else:
        print('Usuario não selecionou lane')
        return False

def aguardandoGrupo():
    atualizaMsg('Voltando pro saguao')
    imgGrupo = locateOnScreen(imagens['grupo'])
    findMatch = locateOnScreen(imagens['encontrarPartida'])
    click(imgGrupo.left + 20, imgGrupo.top + 5, 1)
    time.sleep(2)
    imgLane = locateOnScreen(imagens['laneSelectFixed'])
    if imgLane != None:
        selecionarLanes()

def iniciarVerificaTela():

    imgButton = locateOnScreen(imagens['encontrarPartida'])
    if imgButton != None:
        click(imgButton.left + 80, imgButton.top + 10, 1)
    else:
        print('Aguardando o Lider da sala iniciar')
        
def verificaTela():
    readWindows()
    eventListenerFecharJogo()
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
        eventListenerFecharJogo()
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
        eventListenerFecharJogo()
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
        eventListenerFecharJogo()
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
        eventListenerFecharJogo()
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
        eventListenerFecharJogo()
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
    global window, event, values
    window, event, values = sg.read_all_windows(timeout=1)

global imagens, precisaModo
precisaModo = False
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
laneEsc = laneSelection()
escolhas = championChoices()
janela2 = botTrabalhando()
janela1.close()

def main():    
    if not jogoAberto():
        atualizaMsg('Abrindo o jogo')
        openGame()
        while not verificaSeJogoAberto():
            readWindows()
            eventListenerFecharJogo()
        while locateOnScreen(imagens['jogar']) == None:
            print('Procurando botão play ficar disponivel')
            readWindows()
            eventListenerFecharJogo()
        print('Botao play ficou disponivel')
    if verificaSeJogoAberto():
        time.sleep(2)
        situacao = verificaSitAtual()
        if situacao == 'clicar em play':
            clickOnPlay()
            selectMode()
            time.sleep(1)
            verificaAvisoAutoFill()
            selecionarLanes()
        elif situacao == 'grupo':
            aguardandoGrupo()
        elif situacao == 'selecionar modo':
            selectMode()
            time.sleep(1)
            verificaAvisoAutoFill()
            selecionarLanes()
        elif situacao == 'no saguao':
            if not verificarSePodeStartar():
                selecionarLanes()
    
    iniciarVerificaTela()
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

main()