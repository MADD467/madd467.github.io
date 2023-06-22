from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.google.com/maps/@48.8587374,2.1822302,11z")

time.sleep(5)

search_bar = driver.find_element(By.ID, "searchboxinput")
search_bar.send_keys("Musée du Quai d'Orsay")

time.sleep(5)

btn_itineraire = driver.find_element(By.ID, "hArJGc")
btn_itineraire.click()

time.sleep(10)

magnifying_glass = driver.find_element(By.CLASS_NAME, "mL3xi")
magnifying_glass.click()
