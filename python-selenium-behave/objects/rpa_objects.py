from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

browser = Browser()
class RpaObjects(object):

    # Objetos mapeados
    button_start = '//button[text()="Start"]'
    round_1 = '//button[text()="Round 1"]'
    first_name = '//input[@ng-reflect-name="labelFirstName"]'
    last_name = '//input[@ng-reflect-name="labelLastName"]'
    company_name = '//input[@ng-reflect-name="labelCompanyName"]'
    role_in_company = '//input[@ng-reflect-name="labelRole"]'
    address = '//input[@ng-reflect-name="labelAddress"]'
    email = '//input[@ng-reflect-name="labelEmail"]'
    phone_number = '//input[@ng-reflect-name="labelPhone"]'
    button_submit = '//input[@type="submit"]'
    congratulations = '//div[text()="Congratulations!"]'
