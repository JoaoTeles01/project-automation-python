import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

arquivo_dados_login = "dados_login.csv"
df = pd.read_csv(arquivo_dados_login, delimiter=';')

url_site = "https://www.saucedemo.com"
navegador = webdriver.Edge()
navegador.get(url_site)
time.sleep(5)


def login1(usuario, senha):
    e_usuario = navegador.find_element(
        By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')
    e_usuario.send_keys(usuario)
    time.sleep(1)
    e_senha = navegador.find_element(
        By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    e_senha.send_keys(senha)
    entrar = navegador.find_element(
        By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
    entrar.click()
    time.sleep(3)
    return e_usuario, e_senha


login = df['LOGIN'][0]
senha = df['SENHA'][0]

login1(login, senha)


def visualizarfinalizar(nome, sobreN, cep):
    additens()
    visualizar = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
    visualizar.click()
    time.sleep(2)
    click_checkout = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]')
    click_checkout.click()
    time.sleep(2)
    first_name = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input')
    first_name.send_keys(nome)
    time.sleep(0.5)
    lastname = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input')
    lastname.send_keys(sobreN)
    time.sleep(0.5)
    postal = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input')
    postal.send_keys(cep)
    time.sleep(1)
    click_continue = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/input')
    click_continue.click()
    time.sleep(2)
    localizatotal = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div[8]').text
    time.sleep(1)
    finaliza = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')
    finaliza.click()
    return localizatotal


def additens():
    add_primeiro_i = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    add_primeiro_i.click()
    time.sleep(2)
    add_segundo_i = navegador.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
    add_segundo_i.click()
    return add_primeiro_i, add_segundo_i


nome = df['NOME'][0]
sobreNome = df['SOBRE'][0]
cep = df['CEP'][0]

result = visualizarfinalizar(nome, sobreNome, cep)
print(result)