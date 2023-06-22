from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.google.com/maps/@48.8589384,2.2646349,12z?hl=fr")

time.sleep(10)

barre_recherche = driver.find_element(By.ID, "searchboxinput")
barre_recherche.send_keys("Musée du louvre")

time.sleep(10)

itineraire = driver.find_element(By.CLASS_NAME, "eYqqWd")
itineraire.click()

time.sleep(10)

btn_search = driver.find_element(By.CLASS_NAME, "mL3xi")
btn_search.click()
