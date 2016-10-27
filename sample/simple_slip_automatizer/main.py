from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.qualicorp.com.br/canalcliente/f/t/loginMan")
driver.find_element_by_id('txtUsuario').send_keys("41018776885")
driver.find_element_by_id('txtSenha').send_keys("***")
driver.find_element_by_id('txtSenha').send_keys(Keys.RETURN)
driver.find_element_by_class_name('mais_acessados').click()
