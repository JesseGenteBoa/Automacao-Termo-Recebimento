from selenium import webdriver                        
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep
from pyperclip import copy
from pyautogui import press, hotkey
import pandas as pd


def enviarEmails(caminho_arq):
    df = pd.read_excel(caminho_arq, dtype={3:str})
    lista_de_nomes = df.iloc[:, 0].tolist()
    lista_de_email = df.iloc[:, 2].tolist()
    

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=1')
    link = "https://app.clicksign.com/"
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options)
    driver.get(link)
    

    sleep(1)
    usuario = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div[2]/div/form/div[1]/fieldset/div/input')
    usuario.send_keys("caixa@eqsengenharia.com.br")
    senha = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div[2]/div/form/div[2]/div/fieldset/div/fieldset/div/input')
    senha.send_keys("Eqseng135@")
    logar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div[2]/div/form/button')
    logar.click()

    while True:
        try:
            acesso_eqs = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/main/section/div[4]/div[2]/ul/li[2]/a/div[1]')
            acesso_eqs.click()
            break
        except:
            sleep(0.5)


    for i, nome in enumerate(lista_de_nomes):
        
        sleep(2)
        while True:
            try:
                botao_add_doc = driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[1]/div[1]/div[1]/button')
                botao_add_doc.click()
                break
            except:
                try:
                    botao_add_doc = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[1]/div[1]/button')
                    botao_add_doc.click()
                    break
                except:
                    sleep(0.5)

        sleep(0.8)
        
        while True:
            try:
                botao_selec_arq = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[2]/div[2]/div[1]/div/button[1]')
                botao_selec_arq.click()
                break
            except:
                sleep(0.5)
        
        sleep(1)

        nome = nome.upper()
        nome = nome.strip()
        nome = str(nome)
        arquivo = "PDFs\\TERMO DE RECEBIMENTO - CARTÃO FLASH - " + nome + ".pdf"
        caminho_absoluto = str(Path(arquivo).resolve())
        copy(caminho_absoluto)
        sleep(0.4)
        hotkey("ctrl", "v", interval=0.1)
        sleep(0.4)
        press(["tab"]*2, interval=0.5)
        sleep(0.4)
        press("enter")
        sleep(3)

        while True:
            try:
                botao_avancar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/button')
                botao_avancar.click()
                break
            except:
                sleep(0.8)

        sleep(1)

        while True:
            try:
                botao_sign_agenda = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[1]/ul/li[2]/div/div/div/button')
                botao_sign_agenda.click()
                break
            except:
                sleep(0.8)

        sleep(1)

        while True:
            try:
                input_contato = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/section/div[1]/div[1]/fieldset/div/fieldset/div/input')
                email = lista_de_email[i]
                email = email.lower()
                email = email.strip()
                input_contato.send_keys(email)
                break
            except:
                sleep(0.8)

        sleep(5)

        try:
            checkbox = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/section/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/fieldset/div/label/div')
            checkbox.click()
        except:
            input_contato.clear()
            sleep(0.8)
            input_contato.send_keys(nome)
            sleep(4)
            checkbox = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/section/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/fieldset/div/label/div')
            checkbox.click()

        sleep(1)

        while True:
            try:
                botao_avancar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/footer/button[2]')
                botao_avancar.click()
                break
            except:
                sleep(0.8)

        sleep(1.5)

        while True:
            try:
                campo_sign = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/section/div/ul/li/div/div[1]/fieldset/div/div/div/div[1]/span')
                campo_sign.click()
                sleep(0.8)
                copy("Assinar para acusar recebimento")
                hotkey("ctrl", "v", interval=0.1)
                sleep(0.5)
                press("down", interval=0.3)
                press("enter", interval=0.3)
                break
            except:
                sleep(0.8)

        sleep(1.5)
        
        while True:
            try:
                botao_adicionar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/section[1]/div[1]/div/div/footer/button[2]')
                botao_adicionar.click()
                break
            except:
                sleep(0.8)

        sleep(3.5)

        while True:
            try:
                botao_avancar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/button[2]')
                botao_avancar.click()
                break
            except:
                sleep(0.8)

        sleep(3.5)

        while True:
            try:
                botao_avancar = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[1]/button[2]')
                botao_avancar.click()
                break
            except:
                sleep(0.8)

        sleep(1.5)

        while True:
            try:
                botao_enviar_doc = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[1]/div[4]/button[2]')
                botao_enviar_doc.click()
                break
            except:
                sleep(0.8)

        sleep(2)

        while True:
            try:
                voltar_ao_inicio = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/section/div[2]/button')
                sleep(2.5)
                voltar_ao_inicio.click()
                break
            except:
                sleep(0.8)

    sleep(3)
    driver.quit()
