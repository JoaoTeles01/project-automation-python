from pywinauto import application

# Substitua 'Nome do Aplicativo' pelo título da janela do aplicativo que você deseja interagir
app = application.Application().connect(title='Tela de Login')

# Substitua 'Nome do Controle' pelo nome do controle ou classe do elemento que você deseja acessar
elemento = app['Nome do Controle']

# Pegue dados do elemento
dados = elemento.window_text()
print('Dados do elemento:', dados)
