import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.EdgeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("detach", True)
browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
browser.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Inicialização pagina
browser.maximize_window()
browser.get("https://www.saucedemo.com/")

# Pagina Login
browser.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)
browser.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
browser.find_element(By.ID, "login-button").click()
time.sleep(1)

# Página do ‘e-commerce’
df = pd.read_csv("dados-cliente.csv")
for index, row in df.iterrows():
    WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(2)

    # Pagina carrinho
    WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,100)", "")
    time.sleep(2)
    browser.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Pagina de CheckOut
    browser.execute_script("window.scrollBy(0,-100)", "")
    time.sleep(1)
    browser.find_element(By.ID, "first-name").send_keys(df.loc[index, 'First Name'])
    time.sleep(1)
    browser.find_element(By.ID, "last-name").send_keys(df.loc[index, 'Last Name'])
    time.sleep(1)
    valor_inteiro = int(df.loc[index, 'Postal Code'])
    browser.find_element(By.ID, "postal-code").send_keys(valor_inteiro)
    time.sleep(1)
    browser.execute_script("window.scrollBy(0,100)", "")
    time.sleep(1)
    browser.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Página de Finalização
    browser.execute_script("window.scrollBy(0,250)", "")
    time.sleep(1)
    elemento = browser.find_element("//div[@class='summary_info_label summary_total_label']/text()")
    print(elemento)
    browser.find_element(By.ID, "finish").click()
    time.sleep(5)
    browser.find_element(By.ID, "back-to-products").click()

browser.quit()
