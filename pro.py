from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://www.lvbp.com/resultados.php")
wait = WebDriverWait(driver, 10)
select_element = wait.until(EC.presence_of_element_located((By.NAME, 'week')))
week_select = Select(select_element)
week_select.select_by_value('47')
# Encuentra el elemento select para las fechas
# Crea un objeto Select con el elemento encontrado
week_select = Select(select_element)
# Espera a que la página se actualice con los resultados de la fecha seleccionada
time.sleep(5)

# Encuentra todos los enlaces de boxscore
boxscore_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="gameday.php?game="]')

# Extrae los ID de los juegos de los enlaces
game_ids = [link.get_attribute('href').split('=')[-1] for link in boxscore_links]
ids = [i for i in game_ids if i != "t"]
# Imprime los ID de los juegos
print(ids)

# Cierra el navegador
driver.quit()