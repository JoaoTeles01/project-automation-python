import pyautogui
import time

# Aguarde alguns segundos para posicionar o cursor corretamente
time.sleep(5)

# Obtenha a posição atual do cursor
x, y = pyautogui.position()
print(f"Posição do cursor: ({x}, {y})")

# Execute cliques simulados do mouse
pyautogui.click(x, y)
