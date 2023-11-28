import time
from pygetwindow import getWindowsWithTitle
from pywinauto import Desktop, Application

# Nome da janela da aplicação
app_title = "Tela de Login"

# Espera até que a aplicação esteja aberta
while True:
    try:
        app_window = getWindowsWithTitle(app_title)[0]
        break
    except IndexError:
        print(f"A aplicação '{app_title}' não está aberta. Aguardando...")
        time.sleep(1)

# Traz a janela para o foco
app_window.activate()

time.sleep(2)

# Use o pywinauto para interagir com a aplicação
app = Application().connect(title=app_title)
main_dlg = app[app_title]

# Localize os controles pai TkChild2 e TkChild5
tk_child2 = main_dlg.child_window(class_name="TkChild2")
tk_child5 = main_dlg.child_window(class_name="TkChild5")

# Agora, localize as caixas de texto dentro dos controles pai
campo1 = tk_child2.getValue()
campo2 = tk_child5.getValue()

# Captura os valores dos campos
valor_campo1 = campo1.get_value()
valor_campo2 = campo2.get_value()

# Exibe os valores capturados
print(f"Campo 1: {valor_campo1}")
print(f"Campo 2: {valor_campo2}")
