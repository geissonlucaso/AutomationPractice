import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=myaccount')

# mapeamento dos elementos e atribuição de valores.
driver.find_element(By.ID, 'email').send_keys('geisson@gmaill.com')
driver.find_element(By.ID, 'passwd').send_keys('123456')
driver.find_element(By.ID, 'SubmitLogin').click()
assert driver.find_element(By.XPATH, '//h1[contains(text(), "My account")] | //h1[@class="page-heading"]').is_displayed()
print("Login válido.")
time.sleep(5)

driver.quit()
