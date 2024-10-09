# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# abrir o navegador (chrome)
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(5)


# Passo 2: Fazer login
# selecionar o campo de email
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("johanngomig@gmail.com")
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("123456")
login_button = driver.find_element(By.XPATH,
    '//*[@id="pgtpy-botao"]'
)
login_button.click()
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("produtos.csv")
# print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    codigo_input = driver.find_element(By.NAME,"codigo")
    codigo_input.send_keys(str(tabela.loc[linha, "codigo"]))

    marca_input = driver.find_element(By.NAME,"marca")
    marca_input.send_keys(str(tabela.loc[linha, "marca"]))

    tipo_input = driver.find_element(By.NAME,"tipo")
    tipo_input.send_keys(str(tabela.loc[linha, "tipo"]))

    categoria_input = driver.find_element(By.NAME,"categoria")
    categoria_input.send_keys(str(tabela.loc[linha, "categoria"]))

    preco_input = driver.find_element(By.NAME,"preco_unitario")
    preco_input.send_keys(str(tabela.loc[linha, "preco_unitario"]))

    custo_input = driver.find_element(By.NAME,"custo")
    custo_input.send_keys(str(tabela.loc[linha, "custo"]))

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        obs_input = driver.find_element(By.NAME,"obs")
        obs_input.send_keys(str(obs))

    enviar_button = driver.find_element(By.XPATH,'//*[@id="pgtpy-botao"]')
    enviar_button.click()
    time.sleep(1)  # Pequena pausa entre cadastros

# Fechar o navegador após a execução
driver.quit()
