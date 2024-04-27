import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=myaccount')

#dados.
email = 'glucaso333@email.com'
password = 123456
first_name = 'GLucaso'
last_name = 'Oliveira'

#-------------Cenário 1 - Criar conta-------------
#mapeamento do input para criar conta.
driver.find_element(By.ID, 'email_create').send_keys(email)

#mapeamento do click no botão de criar conta.
driver.find_element(By.ID, 'SubmitCreate').click()

#validação de troca de tela - criar conta
assert driver.find_element(By.XPATH, '//h3[@class="page-subheading" and text()="Your personal information"] ').is_displayed()

#mapeamento dos campos e preenchimento de dados - formulário de usuário.
driver.find_element(By.ID, 'id_gender1').click()
driver.find_element(By.ID, 'customer_firstname').send_keys(first_name)
driver.find_element(By.ID, 'customer_lastname').send_keys(last_name)
driver.find_element(By.ID, 'passwd').send_keys(password)
Select(driver.find_element(By.ID, 'days')).select_by_value('1')
Select(driver.find_element(By.ID, 'months')).select_by_value('1')
Select(driver.find_element(By.ID, 'years')).select_by_value('2000')
driver.find_element(By.ID, 'submitAccount').click()

#validação de troca de tela - minha conta
assert driver.find_element(By.XPATH, '//p[@class="alert alert-success"] | //p[contains(text(), "Your account has been created.")]').is_displayed()
print('Conta criada.')
time.sleep(2)

#-------------Cenário 2 - Cadastrar endereço-------------
#mapeamento do link para adicionar um endereço - Carregar tela de endereços.
driver.find_element(By.XPATH, '//a[@title="Addresses"] ').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "My addresses")] | //h1[@class="page-heading"]').is_displayed()

#mapeamento do link para a tela de preenchimento do endereço. [Carregar tela com os campos para salvar o endereço]
driver.find_element(By.XPATH, '//a[@title="Add an address"]').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "Your Addresses")] | //h1[@class="page-subheading"]').is_displayed()

#preenchimento dos dados de endereço.
driver.find_element(By.ID, 'company').send_keys('Lucas QA')
driver.find_element(By.ID, 'address1').send_keys('Rua do Teste, 404')
driver.find_element(By.ID, 'city').send_keys('Miami')
Select(driver.find_element(By.ID, 'id_state')).select_by_visible_text('Florida')
driver.find_element(By.ID, 'postcode').send_keys('32789')
Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('United States')
driver.find_element(By.ID, 'phone').send_keys('1234567890112')
driver.find_element(By.ID, 'phone_mobile').send_keys('1234567890112')
driver.find_element(By.ID, 'other').send_keys('Sem informações adicionais.')
driver.find_element(By.ID, 'alias').clear()
driver.find_element(By.ID, 'alias').send_keys('Meu endereço')
time.sleep(2)
driver.find_element(By.ID, 'submitAddress').click()

#Verificar se o endereço foi salvo.
assert driver.find_element(By.XPATH, '//h3[contains(text(), "Meu endereço")] | //h3[@class="page-subheading"]').is_displayed()
print('Endereço cadastrado.')
time.sleep(2)

#-------------Cenário 3 - Realizar login-------------
#mapeamento do botão de logout e click do mesmo. 
driver.find_element(By.XPATH, '//a[@title="Log me out"]').click()

#validação da troca de tela - tela login.
assert driver.find_element(By.XPATH, '//h1[contains(text(), "Authentication")] | //h1[@class="page-heading"]').is_displayed()

#mapeamento e adição de valores nos inputs para efetuar login.
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'passwd').send_keys(password)
driver.find_element(By.ID, 'SubmitLogin').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "My account")] | //h1[@class="page-heading"]').is_displayed()
print("Login válido.")
time.sleep(20)

print("Fim Teste.")
driver.quit()