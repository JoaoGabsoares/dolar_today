from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from rich.progress import track
from rich import print

def inicio():
    print('-'*30,'\n', '[bold]Bem-Vindo[/]','\n','-'*30, '\n')
    print('[bold]Iniciando busca...[/]' '\n')

def loading():
    #adiciona uma barra de carregamento

    for tarefa in track(range(30), '[orange]Processando...[/]'):
        sleep(0.2)
    print('[bold][green]Processado com sucesso![/][/]')

def nao_abrir_janela():
    chrome_options = Options() 
    chrome_options.add_argument("--headless") #para não abrir janela do navegador
    return chrome_options

def buscar_webdrive():
    chrome_options = nao_abrir_janela()
    s = Service('/home/joao/Área de trabalho/Curso/arquivos_programacao/projetos/projeto_dolar/chromedriver') # nesse contexto vai ao path do webdriver
    browser = webdriver.Chrome(service=s, options=chrome_options) #adiciona parâmetros necessários ao webdriver
    return browser
    
def abrir_url():
    browser = buscar_webdrive() 

    #vai à url designada
    browser.get('https://www.google.com/search?q=dolar+hoje&oq=dolar+hoje&aqs=chrome..69i57j0i433i512l2j0i512l3j0i433i512j0i512j0i433i512.2222j1j7&sourceid=chrome&ie=UTF-8')
    sleep(2)
    return browser

def buscar_classe():
    browser = abrir_url()
    buscar_class = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]') #busca o xpath
    print(f'[bold][cyan] $1 Dólar setá custando: R${buscar_class.text}[/][/] :money__mouth_face:') #retorna a busca transformando em texto
    return buscar_classe

inicio()
loading()
nao_abrir_janela()
buscar_webdrive()
abrir_url()
buscar_classe()