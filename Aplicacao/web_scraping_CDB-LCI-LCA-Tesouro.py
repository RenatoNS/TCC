#%% Importar bibliotecas

import pandas as pd
from bs4 import BeautifulSoup as soup
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import numpy as np

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
    
    
    df.to_csv('CDB_LCA_LCI_completo_origin.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfCDB.to_csv('CDB_origin.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfLCA.to_csv('LCA_origin.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfLCI.to_csv('LCI_origin.csv', sep = ';', encoding = 'ansi', index = False)
    
    
    dfCDB['Vencimento'] = pd.to_datetime(dfCDB['Vencimento'], dayfirst = True)
    dfCDB = dfCDB.drop(['Prazo', 'Taxa EQ. CDB', 'Juros','Amortização', 'Horário'], axis =1)
    dfCDB['AplicaçãoMínima'] = dfCDB['AplicaçãoMínima'].str[:-2]
    dfCDB['AplicaçãoMínima'] = dfCDB['AplicaçãoMínima'].str.replace(r"[^0-9]", "").astype(float)
    dfCDB['TaxaPct'] = dfCDB['Taxa'].str.partition('%')[0]
    dfCDB['TaxaPct'] = dfCDB['TaxaPct'].str.replace(',', ".").astype(float)
    dfCDB['Indexador'] = dfCDB['Taxa'].str.partition('do ')[2]
    
    
    dfLCA['Vencimento'] = pd.to_datetime(dfLCA['Vencimento'], dayfirst = True)
    dfLCA = dfLCA.drop(['Prazo', 'Taxa EQ. CDB', 'Juros','Amortização', 'Horário'], axis =1)
    dfLCA['AplicaçãoMínima'] = dfLCA['AplicaçãoMínima'].str[:-2]
    dfLCA['AplicaçãoMínima'] = dfLCA['AplicaçãoMínima'].str.replace(r"[^0-9]", "").astype(float)
    dfLCA['TaxaPct'] = dfLCA['Taxa'].str.partition('%')[0]
    dfLCA['TaxaPct'] = dfLCA['TaxaPct'].str.replace(',', ".").astype(float)
    dfLCA['Indexador'] = dfLCA['Taxa'].str.partition('do ')[2]
    
    
    dfLCI['Vencimento'] = pd.to_datetime(dfLCI['Vencimento'], dayfirst = True)
    dfLCI = dfLCI.drop(['Prazo', 'Taxa EQ. CDB', 'Juros','Amortização', 'Horário'], axis =1)
    dfLCI['AplicaçãoMínima'] = dfLCI['AplicaçãoMínima'].str[:-2]
    dfLCI['AplicaçãoMínima'] = dfLCI['AplicaçãoMínima'].str.replace(r"[^0-9]", "").astype(float)
    dfLCI['TaxaPct'] = dfLCI['Taxa'].str.partition('%')[0]
    dfLCI['TaxaPct'] = dfLCI['TaxaPct'].str.replace(',', ".").astype(float)
    dfLCI['Indexador'] = dfLCI['Taxa'].str.partition('do ')[2]

    
    df['Vencimento'] = pd.to_datetime(df['Vencimento'], dayfirst = True)
    df = df.drop(['Prazo', 'Taxa EQ. CDB', 'Juros','Amortização', 'Horário'], axis =1)
    df['AplicaçãoMínima'] = df['AplicaçãoMínima'].str[:-2]
    df['AplicaçãoMínima'] = df['AplicaçãoMínima'].str.replace(r"[^0-9]", "").astype(float)
    df['TaxaPct'] = df['Taxa'].str.partition('%')[0]
    df['TaxaPct'] = df['TaxaPct'].str.replace(',', ".").astype(float)
    df['Indexador'] = df['Taxa'].str.partition('do ')[2]
    

    df.to_csv('CDB_LCA_LCI_completo_Clean.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfCDB.to_csv('CDB_Clean.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfLCA.to_csv('LCA_Clean.csv', sep = ';', encoding = 'ansi', index = False)
    
    dfLCI.to_csv('LCI_Clean.csv', sep = ';', encoding = 'ansi', index = False)

    
    



def extrair_tesouro(url):
    driver.get(url)
    
    time.sleep(5)
    
    element_tesouro = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div/div/div[1]/div/div[9]')
    html_content_tesouro = element_tesouro.get_attribute('outerHTML')
    
    htmlSoup_tesouro = soup(html_content_tesouro, 'html.parser')
    table_tesouro = htmlSoup_tesouro.find(name='table')
    
    df_full_tesouro = pd.read_html(str(table_tesouro))[0]
    
    df_tesouro = df_full_tesouro.drop(df_full_tesouro.columns[5], axis = 1)
    
    df_tesouro.to_csv('tesouro_origin.csv', sep = ';', encoding = 'ansi', index = False)
    
    
    df_tesouro['Vencimento:'] = pd.to_datetime(df_tesouro['Vencimento:'], dayfirst = True)
    df_tesouro['Preço Unitário:'] = df_tesouro['Preço Unitário:'].str[3:]
    df_tesouro['Preço Unitário:'] = df_tesouro['Preço Unitário:'].str.replace('.', "")
    df_tesouro['Preço Unitário:'] = df_tesouro['Preço Unitário:'].str.replace(',', ".").astype(float)
    df_tesouro['Investimento mínimo:'] = df_tesouro['Investimento mínimo:'].str[3:]
    df_tesouro['Investimento mínimo:'] = df_tesouro['Investimento mínimo:'].str.replace(',', ".").astype(float)
    df_tesouro['RentabilidadePct'] = np.nan
    for i in range(df_tesouro['Rentabilidade anual:'].count()):
        if '+' in df_tesouro['Rentabilidade anual:'][i]:
            df_tesouro['RentabilidadePct'][i] = df_tesouro['Rentabilidade anual:'][i].partition('+ ')[2]
        else:
            df_tesouro['RentabilidadePct'][i] = df_tesouro['Rentabilidade anual:'][i]
    df_tesouro['RentabilidadePct'] = df_tesouro['RentabilidadePct'].str.partition('%')[0]
    df_tesouro['RentabilidadePct'] = df_tesouro['RentabilidadePct'].str.replace(',', ".").astype(float)
    df_tesouro['Indexador'] = df_tesouro['Rentabilidade anual:'].str.partition(' +')[0]
    for i in range(df_tesouro['Indexador'].count()):
        if '%' in df_tesouro['Indexador'][i]:
            df_tesouro['Indexador'][i] = np.nan
        else:
            df_tesouro['Indexador'][i] = df_tesouro['Indexador'][i]

    df_tesouro.to_csv('tesouro_Clean.csv', sep = ';', encoding = 'ansi', index = False)


#%% Definir diretorio sincronizado com a nuvem

os.chdir(r'C:\dados')
# os.getcwd()

#%% Variaveis globais

geckodriver_path = r'C:\dados\geckodriver.exe'

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

