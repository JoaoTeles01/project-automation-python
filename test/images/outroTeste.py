import pyautogui
import time

# Aguarde alguns segundos para dar tempo de você posicionar o mouse na posição desejada
time.sleep(5)

# Obtenha as coordenadas do ponto inicial (canto superior esquerdo da região)
x_inicial, y_inicial = pyautogui.position()
print(f"Coordenadas do ponto inicial: ({x_inicial}, {y_inicial})")

# Aguarde alguns segundos para dar tempo de você posicionar o mouse na posição desejada
time.sleep(5)

# Obtenha as coordenadas do ponto final (canto inferior direito da região)
x_final, y_final = pyautogui.position()
print(f"Coordenadas do ponto final: ({x_final}, {y_final})")

# Calcule a largura e altura da região
largura = x_final - x_inicial
altura = y_final - y_inicial



print(f"Largura da região: {largura}")
print(f"Altura da região: {altura}")
