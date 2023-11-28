# Teste de Automação com Python 3.12.0 e Selenium

# No prompt de comando foi feita a instalação do selenium, webdriver e jupyter, utilizando o comando pip
# Utilizei o notebook jupyter para o desenvolvimento do código do projeto

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(EdgeChromiumDriverManager().install())

navegador = webdriver.Edge(service=servico)

# Nesse momento eu importei um arquivo em .csv, utilizado para a retirada dos dados a serem utilizados durante o processo
import pandas as pd

dados = pd.read_csv("swaglabs_login.csv", sep=";")
print(dados.head())

# Determinando os elementos a serem utilizados na etapa de login
for i, user in enumerate(dados['Usuário']):
    password = dados.loc[i, 'Senha']

# Acesso ao site
navegador.get("https://www.saucedemo.com/")

# Login a partir da base de dados do arquivo importado
navegador.find_element('xpath', '//*[@id="user-name"]').send_keys(user)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(password)
navegador.find_element('xpath', '//*[@id="login-button"]').click()

# Processos de adição de alguns produtos, verificação do carrinho e finalização
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
navegador.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
navegador.find_element('xpath', '//*[@id="continue-shopping"]').click()
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
navegador.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
navegador.find_element('xpath', '//*[@id="checkout"]').click()

# Determinando elementos a serem utilizados no cadastro de dados para a finalização da compra
for i, user in enumerate(dados['Usuário']):
    firstname = dados.loc[i, 'Primeiro Nome']
    lastname = dados.loc[i, 'Último Nome']
    postalcode = dados.loc[i, 'Código Postal']

# Cadastro a partir da base de dados do arquivo importado
navegador.find_element('xpath', '//*[@id="first-name"]').send_keys(firstname)
navegador.find_element('xpath', '//*[@id="last-name"]').send_keys(lastname)
navegador.find_element('xpath', '//*[@id="postal-code"]').send_keys(str(postalcode))
navegador.find_element('xpath', '//*[@id="continue"]').click()

# Processo para a captura de tela do valor final da compra
navegador.execute_script('window.scrollBy(0, 15)')
navegador.find_element('xpath', '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').click()
image = navegador.save_screenshot("valorfinal.png")

# Finalização
navegador.find_element('xpath', '//*[@id="finish"]').click()
