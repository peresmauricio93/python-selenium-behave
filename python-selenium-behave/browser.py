from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Browser(object):
    # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    # Define o tempo máximo para carregamento da página
    driver.implicitly_wait(20)
    # Maximiza a janela do browser ao ser iniciado
    driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()