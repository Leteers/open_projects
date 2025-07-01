import webbrowser

# Список ссылок, которые нужно открыть
list_of_urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.youtube.com"
]

# Перебираем ссылки и открываем каждую в Chrome
for url in list_of_urls:
    webbrowser.open_new_tab(url)