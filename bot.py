import pyautogui
import time

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def verificaTela():
    button_pos = pyautogui.locateOnScreen('button.png', confidence=0.8)
    if button_pos != None:
        click(button_pos.left + 80, button_pos.top + 20)
        print("\tPartida encontrada")
        return True
    return False

def verificaInicio():
    image_pos = pyautogui.locateOnScreen('verificaInicio.png', confidence=0.8)
    if image_pos != None:
        return False
    return True
    

def main():
    print("\n\n\tBot criado por Viteeeera (https://github.com/vitox013/bot-lol)\n\n\tVá lá no banheiro que o bot aceitará sozinho caso ache uma partida\n\n")
    while verificaInicio():
        time.sleep(2)
        verificaTela()
    print("\n\n\tPartida iniciada, Boa partida!")
    print("\n\n\tApp será fechado!")
    time.sleep(5)
   

main()

