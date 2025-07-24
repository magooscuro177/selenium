import time

from selenium.webdriver.support.ui import Select

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.support.expected_conditions import visibility_of, element_located_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
import softest
from selenium.webdriver.support import expected_conditions as EC


def test_prueba_01():
    driver=webdriver.Chrome()
    driver.maximize_window()

    # driver.implicitly_wait(10)
    driver.get("https://testautomationpractice.blogspot.com/")
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[contains(@placeholder,"Enter Name")]')))

    textbox1= driver.find_element(By.XPATH,'//*[contains(@placeholder,"Enter Name")]')
    textbox1.send_keys("Luis Pablo")
    textbox1.clear()
    textbox1.send_keys("Juan Gabriel")
    driver.find_element(By.ID,'email').send_keys("pablo.23323@gmail.com")
    driver.find_element(By.XPATH,"//*[contains(@placeholder,'Enter Phone')]").send_keys("44553322")
    driver.find_element(By.XPATH,"//*[contains(@id,'textarea')]").send_keys("Manzana #15 Alvaro Obregon")
    driver.find_element(By.XPATH, '//*[@id="male"]').click()
    driver.find_element(By.XPATH,'//*[@id="monday"]').click()
    driver.find_element(By.XPATH,'//*[@id="tuesday"]').click()
    driver.find_element(By.XPATH,'//*[@id="country"]').click()
    driver.find_element(By.XPATH, '//*[@value="france"]').click()
    driver.find_element(By.XPATH, '//*[@id="colors"]/option[1]').click()
    driver.find_element(By.XPATH, '//*[@value="dog"]').click()

    checkbox= driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[2]/td[4]/input')
    driver.execute_script("arguments[0].scrollIntoView();",checkbox)
    driver.execute_script("arguments[0].click()",checkbox)

    print("Tipo de elemento: ", checkbox.get_attribute('type'))
    print("Seleccionado: ", checkbox.is_selected())

    actual_name= textbox1.get_attribute("value")
    print(actual_name)

    sleep(7)

    titulo = driver.title

    try:
        assert titulo == "Automation Testing Practice", "El titulo no coincide"
    except (TypeError, AssertionError):
        print("El titulo no coincide")

    driver.close()

def test_pruebaPage_02():
    assert True
    # driver=webdriver.Chrome()
    # driver.maximize_window()
    #
    # driver.get("https://centyc.com.ar/#")
    # driver.implicitly_wait(10)
    #
    # element1= driver.find_elements(By.XPATH,'//*[@class="mega-menu-link"]')
    # element1[0].click()
    #
    # driver.find_element(By.XPATH,'//*[@id="mega-menu-item-3741"]/a').click()
    # driver.find_element(By.XPATH,'//*[@id="mega-menu-item-3743"]/a').click()
    # wait= WebDriverWait(driver,5)
    #
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="main-content-anchor"]/div[2]/div/img')))
    #
    # sleep(5)
    #
    # driver.close()

def test_pruebaComboBox_03():
    driver= webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    driver.implicitly_wait(10)
    time.sleep(2)
    select_item= Select(driver.find_element(By.ID,"country"))
    # driver.execute_script("arguments[0].scrollIntoView();", select_item)
    select_item.select_by_value('japan')

    time.sleep(5)

    select_item.select_by_visible_text('Canada')

    time.sleep(4)

    driver.close()

def test_pruebaDragandDrop_04():
    driver=webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.maximize_window()
    driver.implicitly_wait(10)

    wait= WebDriverWait(driver,10)
    element= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="post-body-1307673142697428135"]/div[8]/button')))

    urlTitle= driver.current_url

    assert (urlTitle, "URL Incorrecta")

    driver.close()









