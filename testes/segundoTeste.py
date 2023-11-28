import os
import requests
import subprocess
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import schedule
import time

# Automatização de Download de Imagens de Gatos
def baixar_imagens_gatos(numero_de_imagens=5):
    pasta_destino = 'imagens_de_gatos'
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    url_api_gatos = 'https://api.thecatapi.com/v1/images/search'

    for _ in range(numero_de_imagens):
        resposta = requests.get(url_api_gatos)
        dados_json = resposta.json()
        url_imagem = dados_json[0]['url']

        resposta_imagem = requests.get(url_imagem)

        nome_arquivo = os.path.join(pasta_destino, f'gato_{_ + 1}.jpg')
        with open(nome_arquivo, 'wb') as arquivo:
            arquivo.write(resposta_imagem.content)

        print(f'Imagem {_ + 1} baixada com sucesso.')

# Automatização de Abrir Navegador e Pesquisar no Google
def pesquisar_no_google(termo):
    webbrowser.open('https://www.google.com')
    time.sleep(2)  # Aguarda a página abrir completamente
    pyautogui.write(termo)
    pyautogui.press('enter')

# Automatização de Manipulação de Dados com Pandas
def manipular_dados():
    dados = {'Nome': ['Alice', 'Bob', 'Charlie'],
             'Idade': [25, 30, 35],
             'Cidade': ['A', 'B', 'C']}

    df = pd.DataFrame(dados)
    print("DataFrame Original:")
    print(df)

    # Modificando os dados
    df['Idade'] = df['Idade'] + 1

    # Salvando em um arquivo CSV
    df.to_csv('dados_modificados.csv', index=False)
    print("\nDataFrame Modificado:")
    print(df)

# Automatização de Execução de Comandos do Sistema
def executar_comando_do_sistema():
    # Exemplo: Listar arquivos no diretório atual
    subprocess.run('dir', shell=True)

# Agendamento de Tarefas
def tarefa_agendada():
    print("Esta tarefa foi agendada e está sendo executada agora.")

if __name__ == "__main__":
    # Automatização de Download de Imagens de Gatos
    baixar_imagens_gatos()

    # Automatização de Abrir Navegador e Pesquisar no Google
    pesquisar_no_google('Python Automation')

    # Automatização de Manipulação de Dados com Pandas
    manipular_dados()

    # Automatização de Execução de Comandos do Sistema
    executar_comando_do_sistema()

    # Agendamento de Tarefas
    schedule.every(1).minutes.do(tarefa_agendada)

    while True:
        schedule.run_pending()
        time.sleep(1)
