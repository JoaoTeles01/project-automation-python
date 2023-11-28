import pyautogui
import csv

from pytesseract import pytesseract

# Capturar a tela e salvar como uma imagem
screenshot = pyautogui.screenshot('screenshot.png')


# OCR (Reconhecimento Óptico de Caracteres) para extrair o texto da imagem
nome = pytesseract.image_to_string(nome_region)

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Nome'])
    csv_writer.writerow([nome])
