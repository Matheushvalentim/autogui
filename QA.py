import pyautogui 
import time

#ir para o microsoft edge
pyautogui.moveTo(962,1054,1)
#clicar no edge
pyautogui.click(962,1054,button='right')
#abrir o edge
pyautogui.moveTo(937,940,1)
pyautogui.click(937,940,button="left")
#Ir para o GLPI
pyautogui.moveTo(241,111,3)
time.sleep(2)
#Clicar no GLPI
pyautogui.leftClick(241,111)
#ir para condição de chamado
pyautogui.moveTo(541,271,2)
#clicar na opção
pyautogui.click(541,271,button='left')
#selecionar novo
pyautogui.moveTo(830,314,2)
#clicar em novo
pyautogui.leftClick(830,314)
#mover pesquisar
pyautogui.moveTo(316,304,1)
#clicar pesquisar
pyautogui.click(316,304,button='left')




