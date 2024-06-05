from pygetwindow import getAllTitles

# Lista todos os títulos das janelas abertas
all_titles = getAllTitles()

# Imprime os títulos das janelas
for title in all_titles:
    print(f"Título: {title}")

