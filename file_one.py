
import os.path

import requests
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options


def download():
    print("informe a URL de Download")
    url = input()
    print("informe o nome do arquivo")
    nome = input()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    print("Aguardando retorno da página...")
    driver.get(url)
    WebDriverWait(driver, timeout=10).until(
        lambda x: x.find_element(By.TAG_NAME, "video"))
    print("Vídeo Encontrado!")
    page_source = driver.page_source
    xml_soup = BeautifulSoup(page_source, 'html.parser')
    video = xml_soup.find('video')
    link = video.get('src')
    print(link)
    fim = requests.get(link).content
    home_directory = os.path.expanduser('~')
    f = open(f'{home_directory}/{nome}.mp4', 'wb')
    print("Salvando arquivo...")
    f.write(fim)
    print(f'Arquivo {nome} salvo com sucesso no local {home_directory}')
