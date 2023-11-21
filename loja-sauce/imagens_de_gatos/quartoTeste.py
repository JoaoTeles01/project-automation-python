import pyperclip
from pynput import keyboard
import pygetwindow as gw
import time
import requests
import pyautogui

# URL da página web de destino
url_destino = 'https://exemplo.com/receber-dados'

# Flag para rastrear o estado do clique
clique_inicializado = False

# Timestamp do último clique
ultimo_clique_tempo = 0


def on_press(key):
    global clique_inicializado, ultimo_clique_tempo

    try:
        # Exibe o caractere associado à tecla pressionada
        print(f'Key pressed: {key.char}')
    except AttributeError:
        # Se a tecla não tiver um caractere associado (por exemplo, teclas especiais)
        print(f'Special key pressed: {key}')

    # Lógica para interagir com a aplicação quando uma tecla específica for pressionada
    if key.char == 'a':
        interagir_com_aplicacao()

    # Lógica para capturar duplo clique do mouse
    if key == keyboard.Key.ctrl:
        clique_inicializado = True
        ultimo_clique_tempo = time.time()


def on_release(key):
    global clique_inicializado, ultimo_clique_tempo

    print(f'Key released: {key}')

    # Lógica para encerrar o programa quando a tecla Esc for pressionada
    if key == keyboard.Key.esc:
        return False

    # Lógica para capturar duplo clique do mouse
    if key == keyboard.Key.ctrl:
        if clique_inicializado and time.time() - ultimo_clique_tempo < 0.5:
            print('Duplo clique detectado!')
            # Aqui adicionamos a lógica para extrair dados da aplicação
            dados_extraidos = extrair_texto_do_notepad()
            print('Dados extraídos:', dados_extraidos)

            # Aqui adicionamos a lógica para enviar os dados para a página web
            enviar_dados_para_web(dados_extraidos)

            clique_inicializado = False


def interagir_com_aplicacao():
    # Lógica para interagir com a interface gráfica da aplicação usando pygetwindow
    janela_notepad = gw.getWindowsWithTitle('Bloco de Notas')[0]
    janela_notepad.activate()
    # Adicione aqui a lógica específica para interagir com a aplicação


def extrair_texto_do_notepad():
    # Localiza a janela do Bloco de Notas
    janela_notepad = gw.getWindowsWithTitle('Bloco de Notas')[0]

    # Foca na janela do Bloco de Notas
    janela_notepad.activate()

    # Pausa para garantir que a janela tenha o foco
    time.sleep(1)

    # Simula Ctrl+A para selecionar to do o texto
    pyautogui.hotkey('ctrl', 'a')

    # Simula Ctrl+C para copiar o texto para a área de transferência
    pyautogui.hotkey('ctrl', 'c')

    # Pausa para garantir que a área de transferência seja atualizada
    time.sleep(1)

    # Obtém o texto da área de transferência
    texto_copiado = pyperclip.paste()

    return texto_copiado


# Exemplo de uso
texto_extraido = extrair_texto_do_notepad()

print('Texto extraído do Bloco de Notas:', texto_extraido)


def enviar_dados_para_web(dados):
    try:
        # Envia os dados para a página web usando uma solicitação POST
        resposta = requests.post(url_destino, data=dados)
        resposta.raise_for_status()
        print('Dados enviados com sucesso para a página web!')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao enviar dados para a página web: {e}')


# Listener para capturar eventos de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
