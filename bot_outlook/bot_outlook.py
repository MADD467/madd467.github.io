from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# creer une variable qui declenche le driver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get(
    "")#ENTREZ L'URL DU SITE DANS LEQUEL VOUS VOULEZ VOUS CONNECTEZ

time.sleep(5)

mail = driver.find_element(By.ID, "i0116")
mail.send_keys("")#ENTREZ VOTRE MAIL

suivant_btn = driver.find_element(By.ID, "idSIButton9")
suivant_btn.click()

time.sleep(5)

mdp = driver.find_element(By.ID, "i0118")
mdp.send_keys("")# ENTREZ VOTRE MDP

btn_connect = driver.find_element(By.ID, "idSIButton9")
btn_connect.click()

time.sleep(5)

click_on_NON = driver.find_element(By.ID, "idBtn_Back").click()
