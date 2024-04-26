import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=myaccount')

#mapeamento do input para criar conta.
driver.find_element(By.ID, 'email_create').send_keys('gluks@email.com')

#mapeamento do click no botão de criar conta.
driver.find_element(By.ID, 'SubmitCreate').click()

#validação de troca de tela - criar conta
assert driver.find_element(By.XPATH, '//h3[@class="page-subheading" and text()="Your personal information"] ').is_displayed()
time.sleep(2)

#mapeamento dos campos e preenchimento de dados - formulário de usuário.
driver.find_element(By.ID, 'id_gender1').click()
driver.find_element(By.ID, 'customer_firstname').send_keys('Ususário')
driver.find_element(By.ID, 'customer_lastname').send_keys('Final')
driver.find_element(By.ID, 'passwd').send_keys('12345')
Select(driver.find_element(By.ID, 'days')).select_by_value('1')
Select(driver.find_element(By.ID, 'months')).select_by_value('1')
Select(driver.find_element(By.ID, 'years')).select_by_value('2000')
driver.find_element(By.ID, 'submitAccount').click()

#validação de troca de tela - minha conta
assert driver.find_element(By.XPATH, '//p[@class="alert alert-success"] | //p[contains(text(), "Your account has been created.")]').is_displayed()
print('Conta cadastrada.')
time.sleep(2)
