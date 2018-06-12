from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import json
import config
from user import User

def selectMes():
    mesesTrigger = browser.find_element_by_id('combomeses-1113-triggerWrap')

    mesesTrigger.click()

    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'boundlist-1137-listEl')))
    except TimeoutException:
        print("Loading took too much time!")

    mesesList = browser.find_element_by_id('boundlist-1137-listEl')

    meses = mesesList.find_elements_by_class_name('x-boundlist-item')

    for mes in meses:
        if mes.text == "Febrero":
            mes.click()
            break

def crearDDJJ():
    btn = browser.find_element_by_id('button-1129')

    btn.click()

def cargarDDJJ():
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'button-1081')))
    except TimeoutException:
        print("Loading took too much time!")

    newDDJJ = browser.find_element_by_id('button-1081')

    newDDJJ.click()

    selectAnio()

    selectMes()
    
    selectImportacion()

    crearDDJJ()

def logout():
    return

def start():
    clients = config.clients[0]

    for client in clients:
        browser.get(config.service[0])
        
        u = User(browser, client)

        u.login()

        u.selectRepresentedUser()

        u.enterArciba()

        u.cargarDDJJ()

        u.logout()

delay = 20
browser = webdriver.Firefox()
start()