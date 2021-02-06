from selenium import webdriver
import os

google = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))

google.get('https://www.mercadolivre.com.br/ofertas#c_id=/home/promotions-recommendations/element&c_uid=bf4804c4-91c9-49a8-b3ef-68fafb2139de')


# corriendo los objetos
a = google.find_elements_by_class_name('promotion-item')

# buscando el tamanho
print(len(a))

# buscando todos los datos de los objetos
for i in a:
    print(i.text)
    print(40 * '-')
