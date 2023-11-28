import csv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Produto import Produto

WAIT_TIME = 1
SAUCEDEMO_URL = 'https://www.saucedemo.com/'


def read_login_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return next(reader)


def start_selenium():
    service = Service()
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.get(SAUCEDEMO_URL)
    return driver


def login(driver, login_data):
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

    email_field.send_keys(login_data[0])
    password_field.send_keys(login_data[1])

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
    login_button.click()


def add_items_to_cart(driver, produtos):
    for item in produtos:
        add_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, item.xpath)))
        add_button.click()
        time.sleep(WAIT_TIME)


def checkout(driver):
    cart_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "shopping_cart_container")))
    cart_icon.click()
    checkout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "checkout")))
    checkout_button.click()
    time.sleep(WAIT_TIME)


def minhasInformacoes(driver, user_data):
    first_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
    last_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name")))
    postal_code_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "postal-code")))
    time.sleep(WAIT_TIME)

    first_name_field.send_keys(user_data[0])
    last_name_field.send_keys(user_data[1])
    postal_code_field.send_keys(user_data[2])
    time.sleep(WAIT_TIME)

    continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "continue")))
    continue_button.click()


def print_total(driver):
    time.sleep(WAIT_TIME)
    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]'))).text
    print(f"Valor total da compra: {total}")


def main():
    file_path = 'data.csv'

    p1 = Produto('//*[@id="add-to-cart-sauce-labs-backpack"]')
    p2 = Produto('//*[@id="add-to-cart-sauce-labs-bike-light"]')
    p3 = Produto('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    produtos = [p1, p2, p3]

    user_data = ['João', 'Silva', '12345']
    login_data = read_login_data(file_path)

    driver = start_selenium()
    login(driver, login_data)
    add_items_to_cart(driver, produtos)
    checkout(driver)

    minhasInformacoes(driver, user_data)
    print_total(driver)

    driver.quit()


if __name__ == "__main__":
    main()