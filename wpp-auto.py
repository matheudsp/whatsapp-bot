#Importar bibliotecas ----------------------------------
from selenium import webdriver
import time
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Whatsapp Login ----------------------------------
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abrir o site   
time.sleep(25) #espera pra escanear o qr-code

#Definir ------------------------------------
contatos = ['Quick Notes'] 
mensagem1 = 'Fala '
mensagem2 = ' , segue minha playlist no spotify! https://open.spotify.com/playlist/1K04fOBfMaGxt47Xp6KvEB'
midia = "C:/workspace/wpp-auto/images/rock-spotify.jpeg"

#WppWeb> Buscar ctt/grupo > Enviar ----------------------------------
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem1,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(mensagem1) + str(contato) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)

def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()
    time.sleep(5)    

for contato in contatos:
    
    buscar_contato(contato)
    enviar_midia(midia) 
    enviar_mensagem(mensagem1,mensagem2)      

