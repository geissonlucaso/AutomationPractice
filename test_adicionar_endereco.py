import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=myaccount')

# mapeamento dos elementos e atribuição de valores. [Preenchimento do Login]
driver.find_element(By.ID, 'email').send_keys('geisson@gmaill.com')
driver.find_element(By.ID, 'passwd').send_keys('123456')
driver.find_element(By.ID, 'SubmitLogin').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "My account")] | //h1[@class="page-heading"]').is_displayed()

#mapeamento do link para adicionar um endereço. [Carregar tela de endereços]
driver.find_element(By.XPATH, '//a[@title="Addresses"] ').click()
time.sleep(2)
assert driver.find_element(By.XPATH, '//h1[contains(text(), "My addresses")] | //h1[@class="page-heading"]').is_displayed()
time.sleep(20)

#mapeamento do link para a tela de preenchimento do endereço. [Carregar tela com os campos para salvar o endereço]
driver.find_element(By.XPATH, '//a[@title="Add an address"]').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "Your Addresses")] | //h1[@class="page-subheading"]').is_displayed()

#preenchimento dos dados de endereço.
driver.find_element(By.ID, 'company').send_keys('Minha empresa')
driver.find_element(By.ID, 'address1').send_keys('Rua Um, 45')
driver.find_element(By.ID, 'city').send_keys('Miami')
Select(driver.find_element(By.ID, 'id_state')).select_by_visible_text('Florida')
driver.find_element(By.ID, 'postcode').send_keys('32789')
Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('United States')
driver.find_element(By.ID, 'phone').send_keys('1234567890112')
driver.find_element(By.ID, 'phone_mobile').send_keys('1234567890112')
driver.find_element(By.ID, 'other').send_keys('Sem informações adicionais.')
driver.find_element(By.ID, 'submitAddress').click()

#Verificar se o endereço foi salvo.
assert driver.find_element(By.XPATH, '//h3[contains(text(), "My address")] | //h3[@class="page-subheading"]').is_displayed()

print('Cadastro de endereço válido')

