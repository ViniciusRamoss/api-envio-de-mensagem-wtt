import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

contato = pd.read_excel(r'C:\Users\vinic\OneDrive\Área de Trabalho\DIO\api_whatsapp\Pasta1.xlsx')
print(contato)

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')
navegador.maximize_window()

while len(navegador.find_elements(By.ID,'side')) < 1:
    print("Aguardando o QR Code")
    time.sleep(1)

for i, mensagem in enumerate(contato['Mensagem']):
    pessoa = contato.loc[i, 'Nome']
    numero = contato.loc[i, 'Número']
    texto = urllib.parse.quote(f"{pessoa} estudo de caso de {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        print("Enviando mensagem")
        time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div/p/span').send_keys(Keys.ENTER)
    time.sleep(10)

