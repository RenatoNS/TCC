#%% Importar bibliotecas

import pandas as pd
from bs4 import BeautifulSoup as soup
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

#%% Defibir as funcoes

def extrair_btg(url):
    driver.get(url)
    
    time.sleep(5)
    
    element = driver.find_element_by_xpath('/html/body/app-root/div/app-product-catalog/div/app-product-catalog-fixed-income/app-tabs-default/div/div[2]/div/section/div/div[2]/div[1]')
    html_content = element.get_attribute('outerHTML')
    
    htmlSoup = soup(html_content, 'html.parser')
    table = htmlSoup.find(name='table')
    
    df_full = pd.read_html(str(table))[0]
    
    df = df_full.drop(df_full.columns[9], axis = 1)
    
    dfCDB = df.loc[df['Produto'].str.startswith('CDB')]
    
    dfLCI = df.loc[df['Produto'].str.startswith('LCI')]
    
    dfLCA = df.loc[df['Produto'].str.startswith('LCA')]
    
    
    df.to_csv('CDB_LCA_LCI_completo.csv', sep = ':', encoding = 'ansi', index = False)
    
    dfCDB.to_csv('CDB.csv', sep = ':', encoding = 'ansi', index = False)
    
    dfLCA.to_csv('LCA.csv', sep = ':', encoding = 'ansi', index = False)
    
    dfLCI.to_csv('LCI.csv', sep = ':', encoding = 'ansi', index = False)



def extrair_tesouro(url):
    driver.get(url)
    
    time.sleep(5)
    
    element_tesouro = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div/div/div[1]/div/div[9]')
    html_content_tesouro = element_tesouro.get_attribute('outerHTML')
    
    htmlSoup_tesouro = soup(html_content_tesouro, 'html.parser')
    table_tesouro = htmlSoup_tesouro.find(name='table')
    
    df_full_tesouro = pd.read_html(str(table_tesouro))[0]
    
    df_tesouro = df_full_tesouro.drop(df_full_tesouro.columns[5], axis = 1)
    
    df_tesouro.to_csv('tesouro.csv', sep = ';', encoding = 'ansi', index = False)


#%% Definir diretorio sincronizado com a nuvem

os.chdir(r'C:\dados')
# os.getcwd()

#%% Variaveis globais

geckodriver_path = r'C:\carga_de_dados\geckodriver.exe'

option = Options()
option.headless = True

driver = webdriver.Firefox(executable_path = geckodriver_path, options = option)

url_btg = 'https://www.btgpactualdigital.com/renda-fixa/produtos'
url_tesouro = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'

#%% Execucao do web scraping

extrair_btg(url_btg)
extrair_tesouro(url_tesouro)

#%% Fechar conexao

driver.quit()
