import time
import pyautogui

lista_de_logs = ['Ga', 'he', 'Le', 'Lu', 'Ma', 'Pe', 'Re', 'ro']

contador = (len(lista_de_logs)) - 1

def fechar():  # Fechar conta
    pyautogui.PAUSE = 2
    pyautogui.click(1878, 118)
    pyautogui.click(1750, 270)
    pyautogui.click(1037, 603)

def abrir(usuario):  # Abrir nova conta
    usuario = usuario
    pyautogui.PAUSE = 2
    pyautogui.click(1678, 153)
    pyautogui.click(1835, 234)
    pyautogui.press('backspace', presses=25)
    pyautogui.write(usuario)
    pyautogui.click(1703, 285)
    pyautogui.click(1738, 361)
    time.sleep(1)

pyautogui.alert('NÃO USE O COMPUTADOR ATE O PROCESSO TERMINAR, CERTIFIQUE-SE QUE O CAPS LOCK ESTA DESATIVADO!!')

            # abrir o navegador
pyautogui.PAUSE = 2
pyautogui.press("winleft")
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://gamehag.com/pt')
pyautogui.press("enter")
time.sleep(4)

while contador >= 0 :
    fechar()
    time.sleep(2)
    abrir(lista_de_logs[contador])
    time.sleep(2)
    contador -= 1

pyautogui.alert("TUDO FEITO !!")
