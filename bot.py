import pyautogui
import time

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click


def verificaTela():
    button_pos = pyautogui.locateOnScreen('botaoAceitarOk.png', confidence=0.8)
    if button_pos != None:
        click(button_pos.left + 80, button_pos.top + 20)
        return True
    return False

def verificaInicio():
    image_pos = pyautogui.locateOnScreen('verificaInicio.png', confidence=0.9)
    if image_pos != None:
        return False
    return True
    

def main():
    while verificaInicio():
        verificaTela()
        print('Aguardando para aceitar')   

main()

