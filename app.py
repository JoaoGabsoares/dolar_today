from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from rich.progress import track
from rich import print


#inicio
print('-'*10, '\n', 'Bem Vindos' ,'\n','-'*10, '\n')
print('[bold]Iniciado busca[/]' '\n')

#colocar um loading
for tarefa in track(range(10), '[blue]Processando...[/]'):
    sleep(1)

print('[bold][green]Processado com sucesso!! [/][/]')

#chamar opçõse e passar argumento --headless para não abrir uma janela
chrome_options = Options()
chrome_options.add_argument("--headless")

#buscando webdriver no path
s = Service('/home/joao/Área de trabalho/Curso/arquivos_programacao/projetos/projeto_dolar/chromedriver')
browser = webdriver.Chrome(service=s, options=chrome_options)
sleep(1)

#open url
browser.get('https://www.google.com/search?q=dolar+hoje&oq=dolar+hoje&aqs=chrome..69i57j0i433i512l2j0i512l3j0i433i512j0i512j0i433i512.2222j1j7&sourceid=chrome&ie=UTF-8')
sleep(3)

buscar_classe = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]')
#print('$1 Dólar está custando: ', buscar_classe.text)
print(f'[bold][cyan]$1 Dólar está custando:  R${buscar_classe.text}[/][/]')