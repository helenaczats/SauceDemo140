# 1- Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2- Classe (opcional)
class Teste_Produtos():

    # 2.1 Atributos (campos e variáveis que guardam info)
    url = "https://www.saucedemo.com"
    
    # 2.2 Funcões e Métodos
    def setup_method(self, method):                 # método de inicializacão dos testes
        self.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)             # define o tempo de espera padrão por elementos em x segundos
        
    def teardown_method(self, method):              # método de finalizacão dos testes
        self.driver.quit()                          # encerra/destrói o objeto do Selenium Webdriver da memória
        
    def  test_selecionar_produto(self):     # método de teste
        self.driver.get(self.url)                   # abre o navegador
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")       #escreve no campo user-name
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")       #escreve a senha
        
    