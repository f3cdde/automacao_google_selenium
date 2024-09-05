# Importando as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurando o driver do navegador (neste exemplo, usamos o Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Abrindo o navegador e acessando o Google
driver.get('https://www.google.com')

# Encontrando o campo de busca e digitando a consulta
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium Python')
search_box.send_keys(Keys.RETURN)

# Esperando alguns segundos para os resultados carregarem
time.sleep(3)

# Capturando os títulos dos resultados da pesquisa
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for index, result in enumerate(results):
    print(f"{index + 1}. {result.text}")

# Fechando o navegador
driver.quit()
