from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput import mouse
import time


def on_double_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        elemento = driver.find_element(By.XPATH, '//div[@id="login_credentials"]/h4')
        informacao_extraida = elemento.text

        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])

        driver.get('https://reformulador.com.br/')

        driver.find_element(By.XPATH, '//textarea').send_keys(informacao_extraida)


driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

mouse_listener = mouse.Listener(on_click=on_double_click)
mouse_listener.start()

try:

    input('Pressione Enter para encerrar...')

finally:
    # Encerra os listeners
    mouse_listener.stop()

    # Fecha o navegador
    driver.quit()
