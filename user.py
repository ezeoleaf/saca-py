from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from declaration import Declaration
import time

class User:
    def __init__(self, browser, data):
        self.name = data['nombre']
        self.cuit = data['cuit']
        self.password = data['pass']
        self.browser = browser
        self.company = data['empresa']
        self.declarations = data['declaraciones']

    def login(self):
        elem = self.browser.find_element_by_id('cuit')
        elem.send_keys(self.cuit)

        passElem = self.browser.find_element_by_id('clave')
        passElem.send_keys(self.password)

        enterElem = self.browser.find_element_by_class_name('entrar')
        clickElem = enterElem.find_element_by_tag_name('a')

        clickElem.click()

        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'cuit_representado')))
        except TimeoutException:
            print("Loading took too much time!")

    def selectRepresentedUser(self):
        select = Select(self.browser.find_element_by_id('cuit_representado'))

        select.select_by_value(self.company['cuit'])

        time.sleep(1)

    def enterArciba(self):
        servicios = self.browser.find_elements_by_class_name('contiene_servicio')

        for servicio in servicios:
            servicioName = servicio.find_element_by_class_name('titulo_servicio')
            if servicioName.text == 'e-Arciba':
                servicio.click()
                break
    
    def cargarDDJJ(self):
        for declaration in self.declarations:
            dj = Declaration(self.browser, declaration)
            dj.parseCSV()
            dj.start()
            dj.create()
            dj.load()

    def logout(self):
        return