from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from objects.rpa_objects import RpaObjects
import pandas as pd
import os as os


rpaObj = RpaObjects()

class RpaFunctions(Browser):
    def get_element(self, locator):
        # aguarda elemento estar visível na tela
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # retorna elemento
        return self.driver.find_element(By.XPATH, locator)

    def acess_page(self):
        # acessa url passada
        self.driver.get('https://www.rpachallenge.com/')

    def button_start(self):
        # Clicar no botão start
        self.driver.find_element(By.XPATH, rpaObj.button_start).click()
        self.screenshot('./screenshot/start.png')

    def read_excel(self, users):
        data = pd.read_excel('./excel/challenge.xlsx')
        for i, r in data.iterrows():
            user = {
                'id': i + 1,
                'first': str(r['First Name']),
                'last': str(r['Last Name ']),
                'company': str(r['Company Name']),
                'role': str(r['Role in Company']),
                'address': str(r['Address']),
                'email': str(r['Email']),
                'phone': str(r['Phone Number']),
            }
            print(user)
            users.append(user)
        return users

    def preencher_tudo(self, users):
        for user in users:
            self.driver.find_element(By.XPATH, rpaObj.first_name).send_keys(user['first'])
            self.driver.find_element(By.XPATH, rpaObj.last_name).send_keys(user['last'])
            self.driver.find_element(By.XPATH, rpaObj.company_name).send_keys(user['company'])
            self.driver.find_element(By.XPATH, rpaObj.role_in_company).send_keys(user['role'])
            self.driver.find_element(By.XPATH, rpaObj.address).send_keys(user['address'])
            self.driver.find_element(By.XPATH, rpaObj.email).send_keys(user['email'])
            self.driver.find_element(By.XPATH, rpaObj.phone_number).send_keys(user['phone'])

            # Screenshot apos preencher um usuario
            self.screenshot(f'./screenshot/example-{user["id"]}.png')

            # Submit apos preencher um usuario
            self.driver.find_element(By.XPATH, rpaObj.button_submit).click()

    def screenshot(self, path):
        self.driver.save_screenshot(path)
    def delete_archives(self):
        dir = './screenshot'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    def validate_congratulations(self):
        # Validar a tela Congratulations!
        self.driver.find_element(By.XPATH, rpaObj.congratulations).is_displayed()
        self.screenshot('./screenshot/congratulations-11.png')
