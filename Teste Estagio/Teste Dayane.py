from selenium import webdriver

print("https://www.saucedemo.com/")


def test_swag_labs(driver):
    # Abrir o site
    driver.get("https://www.saucedemo.com/")

    # Fazer login
    username = "standard_user"
    password = "secret_sauce"
    login_input = driver.find_element("name", "user-name")
    login_input.send_keys(username)
    password_input = driver.find_element("name", "password")
    password_input.send_keys(password)
    login_button = driver.find_element("name", "login-button")
    login_button.click()

    # Adicionar itens ao carrinho
    product_1 = driver.find_element("name", "add-to-cart-sauce-labs-backpack")
    product_1.click()
    product_2 = driver.find_element("name", "add-to-cart-sauce-labs-bolt-t-shirt")
    product_2.click()

    # Visualizar carrinho
    driver.find_element("class name", 'shopping_cart_link').click()

    # Finalizar
    checkout_button = driver.find_element("name", "checkout")
    checkout_button.click()

    # Pegar informações de login e cadastro do arquivo
    with open("login.csv", "r") as f:
        login_info = f.readlines()
    first_name_csv = login_info[0].split(";")[0]
    print(first_name_csv)
    last_name_csv = login_info[0].split(";")[1]
    print(last_name_csv)
    postal_code_csv = login_info[0].split(";")[2]
    print(postal_code_csv)

    first_name = driver.find_element("name", "firstName")
    first_name.send_keys(first_name_csv)

    last_name = driver.find_element("name", "lastName")
    last_name.send_keys(last_name_csv)

    postal_code = driver.find_element("name", "postalCode")
    postal_code.send_keys(postal_code_csv)

    driver.find_element("name", 'continue').click()

    # Pegar o valor total
    total_price = driver.find_element("class name", "summary_info_label.summary_total_label")
    print(total_price.text)


driver = webdriver.Chrome()
test_swag_labs(driver)
