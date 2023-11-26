import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://suap.ifto.edu.br/accounts/login/?next=/")

title = driver.title

print(f"O titulo da pagina web é: {title}")
driver.implicitly_wait(500)

user = driver.find_element(By.XPATH, '//*[@id="id_username"]')
password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
button_continue = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/form/div[5]/input')

#user_dig = input("Digite seu usuario: ")
# password_dig = input("Digite sua senha: ")

user.send_keys(user_dig)
password.send_keys(password2_dig)
button_continue.click()
time.sleep(3)

perfil_user = driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[1]/span')

perfil_user.click()
time.sleep(3)

nome_user = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/dl/div[1]/dd')
nome_user2 = nome_user.text
print(f"Seu nome é: {nome_user2}")
time.sleep(1)

matricula_user = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/dl/div[2]/dd')
matricula_user2 = matricula_user.text

print(f"Sua matricula é: {matricula_user2}")
time.sleep(1)

email_user = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/dl/div[4]/dd')
email_user2 = email_user.text

print(f"Seu email é: {email_user2}")
time.sleep(1)

cpf_user = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/dl/div[6]/dd')
cpf_user2 = cpf_user.text

print(f"Seu CPF é: {cpf_user2}")
time.sleep(1)

curso_user = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/dl/div[9]/dd')
curso_user2 = curso_user.text

print(f"Seu curso é: {curso_user2}")
