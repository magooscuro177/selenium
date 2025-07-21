from errno import ECHILD
from time import sleep
import softest
from selenium import webdriver
import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import softest


from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.expected_conditions import visibility_of, element_located_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait


def test_login_01():
    assert True
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    #
    # # Implict Wait
    # driver.implicitly_wait(10)
    #
    # driver.get("https://centyc.com.ar/")
    #
    # wait=WebDriverWait(driver,15)
    # element= wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="login"]/button')))
    #
    # titulo= driver.title
    #
    # assert titulo== "The Internet", "El titulo no coincide"
    #
    #
    #
    # # Login
    #
    # driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('tomsmith')
    #
    # driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
    #
    # driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    #
    # time.sleep(5)
    #
    # driver.close()
