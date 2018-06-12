from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import config

class Declaration:
    def __init__(self, browser, data):
        self.browser = browser
        self.year = data['anio']
        self.month = data['mes']
        self.data = data['datos']
    
    def start(self):
        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'button-1081')))
        except TimeoutException:
            print("Loading took too much time!")

        newDDJJ = self.browser.find_element_by_id('button-1081')

        newDDJJ.click()
    
    def selectYear(self):
        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'comboanios-1112-triggerWrap')))
        except TimeoutException:
            print("Loading took too much time!")

        trigger = self.browser.find_element_by_id('comboanios-1112-triggerWrap')

        trigger.click()

        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'boundlist-1136-listEl')))
        except TimeoutException:
            print("Loading took too much time!")

        yList = self.browser.find_element_by_id('boundlist-1136-listEl')

        years = yList.find_elements_by_class_name('x-boundlist-item')

        for year in years:
            if int(year.text) == self.year:
                year.click()
                break

    def selectMonth(self):
        trigger = self.browser.find_element_by_id('combomeses-1113-triggerWrap')

        trigger.click()

        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'boundlist-1137-listEl')))
        except TimeoutException:
            print("Loading took too much time!")

        mList = self.browser.find_element_by_id('boundlist-1137-listEl')

        months = mList.find_elements_by_class_name('x-boundlist-item')

        for month in months:
            if month.text == self.month:
                month.click()
                break

    def selectImportation(self):
        trigger = self.browser.find_element_by_id('combo-1115-triggerWrap')

        trigger.click()

        try:
            myElem = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'boundlist-1138-listEl')))
        except TimeoutException:
            print("Loading took too much time!")

        iList = self.browser.find_element_by_id('boundlist-1138-listEl')

        items = iList.find_elements_by_class_name('x-boundlist-item')

        for item in items:
            if item.text == "Manual":
                item.click()
                break

    def save(self):
        btn = self.browser.find_element_by_id('button-1129')
        btn.click()

        time.sleep(10)

    def create(self):
        self.selectYear()
        self.selectMonth()
        self.selectImportation()
        self.save()

    def enterSection(self):
        ddjjSection = "treeview-1034-record-" + str(2018) + "-" + str(config.months["Febrero"])

        try:
            _ = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, ddjjSection)))
        except TimeoutException:
            print("Loading took too much time!")

        options = self.browser.find_elements_by_class_name('x-tree-node-text')

        for option in options:
            print(option.text)
            if option.text == 'Retenciones/percepciones':
                option.click()
                break

    def newRetention(self, data):
        try:
            _ = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'button-1191')))
        except TimeoutException:
            print("Loading took too much time!")

        btn = self.browser.find_element_by_id('button-1191')
        btn.click()

    def load(self):
        self.enterSection()
        for data in self.data:
            self.newRetention(data)
        return
