from select import select
from shutil import move
import pyautogui
import time
import keyboard


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
    button_pos = pyautogui.locateOnScreen('imgs/button.png', confidence=0.8)
    if button_pos != None:
        if button_pos != None:
            click(button_pos.left + 80, button_pos.top + 20)
            time.sleep(2)
            pyautogui.moveTo(button_pos.left -30, button_pos.top + 100)
            print("\n\nPartida encontrada e aceita")
        return True
    return False

def verificaSeTodosAceitaram():
    print("\n\nVerificando se todos aceitaram")
    while True:
        flag = pyautogui.locateOnScreen('imgs/flagTodosAceitaram.png', confidence=0.8)
        if flag != None:
            print('\n\nTodos aceitaram')
            return True
        flagNao = pyautogui.locateOnScreen('imgs/retornouFila.png', confidence=0.8)
        if flagNao != None:
            return False

def guardarImgChampion():
    champion = pyautogui.locateOnScreen('imgs/topIcon.png', confidence=0.8)
    imgChampion = pyautogui.screenshot(region=(champion.left + 2, champion.top + 36, 67, 55))
    return imgChampion

def declareChampion(champion):
    declareImg = pyautogui.locateOnScreen('imgs/declareChampion.png', confidence=0.8)
    while declareImg == None and not verificaTela():
        declareImg = pyautogui.locateOnScreen('imgs/declareChampion.png', confidence=0.8)

    time.sleep(2)    
    search()
    pyautogui.write(champion)
    time.sleep(3)
    img = guardarImgChampion()
    time.sleep(1)
    selectChampion()
    return img
   
def banChampion(championBan):
    ban = pyautogui.locateOnScreen('imgs/ban.png', confidence=0.8)
    while ban == None and not verificaTela():
        ban = pyautogui.locateOnScreen('imgs/ban.png', confidence=0.8)
    time.sleep(2)
    search()
    pyautogui.write(championBan)
    selectChampion()
    time.sleep(3)
    buttonBan()
    pyautogui.moveTo(ban.left, ban.top)

def verificaSeChampFoiBanido(champion):
    aguardando = pyautogui.locateOnScreen('imgs/banimentosconfirmados.png', confidence=0.8)
    print('\n\nAguardando as confirmacoes de ban')
    while aguardando == None:
        aguardando = pyautogui.locateOnScreen('imgs/banimentosconfirmados.png', confidence=0.8)
    print('\n\nVerificando se o champion foi banido')
    while True:
        img = pyautogui.locateOnScreen(champion, confidence=0.8)
        aguardando = pyautogui.locateOnScreen('imgs/banimentosconfirmados.png', confidence=0.8)
        if img != None:
            print('\n\nSeu champion foi banido')
            return True
        if aguardando == None:
            print('\n\nSeu champion não foi banido')
            return False
   
def championSelect(opcao):
    confirmar1 = pyautogui.locateOnScreen('imgs/escolha.png', confidence=0.8)
    print("\n\nEsperando minha vez para selecionar")
    while confirmar1 == None and not verificaTela():
        if verificaTela():
            return False
        confirmar1 = pyautogui.locateOnScreen('imgs/escolha.png', confidence=0.8)
    print('\n\nMinha vez de escolher um campeao')
    time.sleep(2)
    search()
    pyautogui.write(opcao)
    selectChampion()
    time.sleep(2)
    buttonConfirm()

def verificaInicio():
    if keyboard.is_pressed("delete"):
        return False
    image_pos = pyautogui.locateOnScreen('imgs/verificaInicio.png', confidence=0.8)
    image_pos2 = pyautogui.locateOnScreen('imgs/verificaInicio2.png', confidence=0.8)
    image_pos3 = pyautogui.locateOnScreen('imgs/verificaInicio3.png', confidence=0.8)
    if image_pos != None or image_pos2 != None or image_pos3 != None:
        return False
    return True

def main():

    print("\n\nBot criado por Viteeeera (https://github.com/vitox013/bot-lol)\n\nVá lá no banheiro que o bot aceitará sozinho caso ache uma partida\n\nO programa fechará sozinho quando a tela de loading começar, mas caso queira fechar antes é só pressionar CTRL+C no terminal")

    opcao1 = input('\n\nPrimeira opcao de champion: \n')
    ban = input('\n\nBanir quem? \n')
    opcao2 = input('\n\nSegunda opção de champion caso o primeiro seja banido:\n')

    print("\n\nAguardando a partida ser encontrada")
    while verificaInicio():
        if verificaTela():
            if verificaSeTodosAceitaram():
                img = declareChampion(opcao1)
                banChampion(ban)
                banido = verificaSeChampFoiBanido(img)
                if banido == True:
                    championSelect(opcao2)
                else:
                    championSelect(opcao1)
                    
    
    print("\n\n\tPartida iniciada, Boa partida!")
    print("\n\n\tApp será fechado!")
    time.sleep(3)
   
main()

