from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import config

def loginUser(data):
    elem = browser.find_element_by_id('cuit')  # Find the search box
    elem.send_keys(data['cuit'])

    passElem = browser.find_element_by_id('clave')
    passElem.send_keys(data['password'])

    enterElem = browser.find_element_by_class_name('entrar')
    clickElem = enterElem.find_element_by_tag_name('a')

    clickElem.click()

    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'cuit_representado')))
    except TimeoutException:
        print("Loading took too much time!")

def selectRepresentedUser(data):
    select = Select(browser.find_element_by_id('cuit_representado'))

    select.select_by_value(data['empresa']['cuit'])

    time.sleep(1)

def enterArciba():
    servicios = browser.find_elements_by_class_name('contiene_servicio')

    for servicio in servicios:
        servicioName = servicio.find_element_by_class_name('titulo_servicio')
        if servicioName.text == 'e-Arciba':
            servicio.click()

def logout():
    return

def start():
    clients = config.clients

    for client in clients:
        browser.get(config.service[0])

        data = clients[client]
        
        loginUser(data)
        
        selectRepresentedUser(data)

        enterArciba()

        logout()

delay = 20
browser = webdriver.Firefox()
start()