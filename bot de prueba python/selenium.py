from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ruta al controlador del navegador (ejemplo para Chrome)
PATH = 'ruta/del/controlador/chromedriver.exe'  # Cambia esto con la ubicación de tu controlador

# Configurar opciones del navegador (en este caso, Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Para abrir la ventana del navegador maximizada

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=PATH, options=options)

# Navegar a Google
driver.get("https://www.google.com")

# Encontrar el campo de búsqueda
search_box = driver.find_element_by_name("q")

# Escribir "Hola" en el campo de búsqueda y presionar Enter
search_box.send_keys("Hola")
search_box.send_keys(Keys.RETURN)

# Cerrar el navegador al finalizar
driver.quit()
