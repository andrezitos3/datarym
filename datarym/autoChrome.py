from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())

# Iniciar uma instância do ChromeDriver
driver = webdriver.Chrome(service=service)

# Acessar a página inicial do Google
driver.get("https://www.google.com")

# Localizar a barra de pesquisa pelo nome do elemento
search_box = driver.find_element("name", "q")

# Inserir o termo de pesquisa
search_box.send_keys("Selenium Python")

# Enviar o formulário de pesquisa
search_box.send_keys(Keys.RETURN)

# Esperar alguns segundos para visualizar os resultados
time.sleep(3)

# Fechar o navegador
driver.quit()
