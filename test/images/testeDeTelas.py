import pyautogui
import pytesseract
import pandas as pd
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

def extrair_texto_da_imagem(imagem):
    texto = pytesseract.image_to_string(imagem)
    return texto

def coletar_informacoes_da_tela():
    x, y, largura, altura = 1351, 108, 1406, 713
    imagem = pyautogui.screenshot(region=(x, y, largura, altura))

    texto_extraido = extrair_texto_da_imagem(imagem)

    return {'TextoExtraido': texto_extraido}

def exportar_para_csv(informacoes, nome_arquivo='dados.csv'):
    try:
        df = pd.read_csv(nome_arquivo)
    except FileNotFoundError:
        df = pd.DataFrame()

    df = df.append(informacoes, ignore_index=True)

    df.to_csv(nome_arquivo, index=False)
    print(f'Dados exportados para {nome_arquivo}')

while True:
    if keyboard.is_pressed('F2'):
        informacoes = coletar_informacoes_da_tela()
        exportar_para_csv(informacoes)
