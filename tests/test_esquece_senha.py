import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=myaccount')

#mapeamento do link para 'forgot your password'.
driver.find_element(By.XPATH, '//a[@title="Recover your forgotten password"]').click()

#verificação da tela aberta - 'Forgot your password'
assert driver.find_element(By.XPATH, '//h1[@class="page-subheading"] | //h1[contains(text(), "Forgot your password?")]').is_displayed()

#preenche o email para recuperar a senha.
driver.find_element(By.ID, 'email').send_keys('gluks@email.com')
time.sleep(2)

#click no botão de recuperação de senha.
driver.find_element(By.XPATH, '//*[@type="submit" and @class="btn btn-default button button-medium"]').click()

#verifica a confirmação do email - referencia ao box verde de confirmação.
driver.find_element(By.XPATH, '//p[@class="alert alert-success"]').is_displayed()

print('Senha resetada.')
time.sleep(2)

driver.quit()