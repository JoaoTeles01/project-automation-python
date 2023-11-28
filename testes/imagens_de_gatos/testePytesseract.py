from PIL import Image
import pytesseract

# Caminho para o arquivo Tesseract OCR no seu sistema
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carregue a imagem do screenshot
caminho_screenshot = r'C:\Users\rodri\OneDrive\Imagens\Capturas de tela'
screenshot = Image.open(caminho_screenshot)

# Use o PyTesseract para extrair texto
texto_extraido = pytesseract.image_to_string(screenshot)

# Imprima o texto extraído
print(texto_extraido)
