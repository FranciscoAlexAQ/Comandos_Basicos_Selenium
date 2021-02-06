from selenium import webdriver
import os

# llamando el navegador del ordenador
browser = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))

# Corre el url de la página
browser.get('https://github.com')

# Haciendo click en sign in
browser.find_element_by_link_text('Sign in').click()

# Inserindo datos en los campos
browser.find_element_by_name('login').send_keys('FranciscoAlexAQ')

browser.find_element_by_name('password').send_keys('1216143a')
browser.find_element_by_name('commit').click()

browser.find_element_by_id('dashboard-repos-filter-left').send_keys('sistema')
