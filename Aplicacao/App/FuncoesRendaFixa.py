#%% Importar bibliotecas

import gdown
import pandas as pd
import os
import datetime
from datetime import date
import numpy as np


#%% Funcoes

def download_opcoesRF():
    id_CDB = '1GXUlUhjOhNjMFDO6x4eB0FiXotdenXqC'
    id_LCA = '1k4UGTGLx_t-4B-hYnqmsIWlI4BujZTFq'
    id_LCI = '1TOfiu5xWrazGSEoqvbhtl56bhU2NfSF3'
    id_tesouro = '1P7O8G6wnhgAtxtT1he9cn6_8QUpHabMw'
    id_completo = '1dewy6nZVPNsYBomfMykpwtUFFzc7GzLI'
    
    ids_drive = [id_CDB, id_LCA, id_LCI, id_tesouro, id_completo]
    ids_drive_nomes = ['CDB_Clean.csv', 'LCA_Clean.csv', 'LCI_Clean.csv', 
                       'tesouro_Clean.csv', 'completo_Clean.csv']

    for idurl, nome in zip(ids_drive, ids_drive_nomes):
        url = f'https://drive.google.com/uc?id={idurl}'
        output = nome
        gdown.download(url, output, quiet = True)
    return



def ir_regressivo(dataInic, dataFinal):
    dataInic = pd.to_datetime(dataInic, dayfirst = True)
    dataFinal = pd.to_datetime(dataFinal, dayfirst = True)
    dias = (dataFinal - dataInic).days
    if(dias <= 180):
        ir = 0.225
    elif(dias > 180 & dias <= 360):
        ir = 0.20
    elif(dias > 360 & dias <= 720):
        ir = 0.175
    elif(dias > 720):
        ir = 0.15
  
    return(ir)
    


def consulta_opcoes_CDB(dataF, valor):
    dfCDB_Clean = pd.read_csv('CDB_Clean.csv', sep = ';', encoding = 'ansi')
    dataF = pd.to_datetime(dataF, dayfirst = True)
    dfCDB_Clean['Vencimento'] = pd.to_datetime(dfCDB_Clean['Vencimento'], dayfirst = True)
    dfOpcoesCDB = dfCDB_Clean.loc[(dfCDB_Clean["Vencimento"] <= dataF) & 
                                  (dfCDB_Clean["AplicaçãoMínima"] <= valor)]
    dfOpcoesCDB['TaxaComIR'] = np.nan
    dfOpcoesCDB = dfOpcoesCDB.reset_index(drop = True)
    for i in range(dfOpcoesCDB['Produto'].count()):
        dfOpcoesCDB['TaxaComIR'][i] = (dfOpcoesCDB['TaxaPct'][i] * 
                   (1 - ir_regressivo(date.today(), dfOpcoesCDB['Vencimento'][i])))
    del dfOpcoesCDB['TaxaPct']
    dfOpcoesCDB['Vencimento'] = dfOpcoesCDB['Vencimento'].dt.strftime('%d/%m/%Y')
    dfOpcoesCDB = dfOpcoesCDB.sort_values('TaxaComIR', ascending = False)
    dfOpcoesCDB = dfOpcoesCDB.reset_index(drop = True)
    dfOpcoesCDB['TaxaComIR'] = dfOpcoesCDB['TaxaComIR'].round(2).astype(str) + '%' + ' ' + dfOpcoesCDB['Indexador'].astype(str)
    dfOpcoesCDB['TaxaComIR'] = dfOpcoesCDB['TaxaComIR'].str.replace('nan', "").astype(str)
    dfOpcoesCDB = dfOpcoesCDB.rename(columns={'Vencimento': 'Data de Resgate', 
                                              'Taxa': 'Rendimento Bruto', 
                                              'AplicaçãoMínima': 'Aplicação Mínima', 
                                              'TaxaComIR': 'Rendimento Líquido'})
    dfOpcoesCDB['Coberto pelo FGC?'] = 'Sim'
    dfOpcoesCDB['Risco'] = 'Baixo'
    dfOpcoesCDB['Canal de Atendimento'] = 'atendimento@btgpactualdigital.com'
    dfOpcoesCDB.to_csv('dfCDBop.csv', sep = ';', encoding = 'ansi', index = False)
    return


def consulta_opcoes_LCI(dataF, valor):
    dfLCI_Clean = pd.read_csv('LCI_Clean.csv', sep = ';', encoding = 'ansi')
    dataF = pd.to_datetime(dataF, dayfirst = True)
    dfLCI_Clean['Vencimento'] = pd.to_datetime(dfLCI_Clean['Vencimento'], dayfirst = True)
    dfOpcoesLCI = dfLCI_Clean.loc[(dfLCI_Clean["Vencimento"] <= dataF) & 
                                  (dfLCI_Clean["AplicaçãoMínima"] <= valor)]
    dfOpcoesLCI['Vencimento'] = dfOpcoesLCI['Vencimento'].dt.strftime('%d/%m/%Y')
    dfOpcoesLCI = dfOpcoesLCI.sort_values('TaxaPct', ascending = False)
    del dfOpcoesLCI['TaxaPct']
    dfOpcoesLCI = dfOpcoesLCI.reset_index(drop = True)
    dfOpcoesLCI = dfOpcoesLCI.rename(columns={'Vencimento': 'Data de Resgate',
                                              'Taxa': 'Rendimento Líquido', 
                                              'AplicaçãoMínima': 'Aplicação Mínima'})
    dfOpcoesLCI['Coberto pelo FGC?'] = 'Sim'
    dfOpcoesLCI['Risco'] = 'Baixo'
    dfOpcoesLCI['Canal de Atendimento'] = 'atendimento@btgpactualdigital.com'
    dfOpcoesLCI.to_csv('dfLCIop.csv', sep = ';', encoding = 'ansi', index = False)
    return
    

def consulta_opcoes_LCA(dataF, valor):
    dfLCA_Clean = pd.read_csv('LCA_Clean.csv', sep = ';', encoding = 'ansi')
    dataF = pd.to_datetime(dataF, dayfirst = True)
    dfLCA_Clean['Vencimento'] = pd.to_datetime(dfLCA_Clean['Vencimento'], dayfirst = True)
    dfOpcoesLCA = dfLCA_Clean.loc[(dfLCA_Clean["Vencimento"] <= dataF) & 
                                  (dfLCA_Clean["AplicaçãoMínima"] <= valor)]
    dfOpcoesLCA['Vencimento'] = dfOpcoesLCA['Vencimento'].dt.strftime('%d/%m/%Y')
    dfOpcoesLCA = dfOpcoesLCA.sort_values('TaxaPct', ascending = False)
    del dfOpcoesLCA['TaxaPct']
    dfOpcoesLCA = dfOpcoesLCA.reset_index(drop = True)
    dfOpcoesLCA = dfOpcoesLCA.rename(columns={'Vencimento': 'Data de Resgate',
                                              'Taxa': 'Rendimento Líquido', 
                                              'AplicaçãoMínima': 'Aplicação Mínima'})
    dfOpcoesLCA['Coberto pelo FGC?'] = 'Sim'
    dfOpcoesLCA['Risco'] = 'Baixo'
    dfOpcoesLCA['Canal de Atendimento'] = 'atendimento@btgpactualdigital.com'
    dfOpcoesLCA.to_csv('dfLCAop.csv', sep = ';', encoding = 'ansi', index = False)
    return
    

def consulta_opcoes_tesouro(dataF, valor):
    dftesouro_Clean = pd.read_csv('tesouro_Clean.csv', sep = ';', encoding = 'ansi')
    dataF = pd.to_datetime(dataF, dayfirst = True)
    dftesouro_Clean['Vencimento:'] = pd.to_datetime(dftesouro_Clean['Vencimento:'], dayfirst = True)
    dfOpcoesTesouro = dftesouro_Clean.loc[(dftesouro_Clean["Vencimento:"] <= dataF) & 
                                          (dftesouro_Clean["Investimento mínimo:"] <= valor)]
    dfOpcoesTesouro['TaxaComIR'] = np.nan
    dfOpcoesTesouro = dfOpcoesTesouro.reset_index(drop = True)
    for i in range(dfOpcoesTesouro['Título'].count()):
        dfOpcoesTesouro['TaxaComIR'][i] = (dfOpcoesTesouro['RentabilidadePct'][i] * 
                       (1 - ir_regressivo(date.today(), dfOpcoesTesouro['Vencimento:'][i])))
    del dfOpcoesTesouro['RentabilidadePct']
    dfOpcoesTesouro['Vencimento:'] = dfOpcoesTesouro['Vencimento:'].dt.strftime('%d/%m/%Y')
    dfOpcoesTesouro = dfOpcoesTesouro.sort_values('TaxaComIR', ascending = False)
    dfOpcoesTesouro = dfOpcoesTesouro.reset_index(drop = True)
    dfOpcoesTesouro['TaxaComIR'] = dfOpcoesTesouro['TaxaComIR'].round(2).astype(str) + '%' + ' ' + dfOpcoesTesouro['Indexador'].astype(str)
    dfOpcoesTesouro['TaxaComIR'] = dfOpcoesTesouro['TaxaComIR'].str.replace('nan', "").astype(str)
    dfOpcoesTesouro = dfOpcoesTesouro.rename(columns={'Renatbilidade anual:': 'Rendimento Anual Bruto',
                                                      'Investimento mínimo:': 'Investimento mínimo', 
                                                      'Preço Unitário:': 'Preço Unitário', 
                                                      'Vencimento:': 'Vencimento', 'TaxaComIR': 'Rendimento Líquido'})
    dfOpcoesTesouro['Coberto pelo FGC?'] = 'Não'
    dfOpcoesTesouro['Risco'] = 'Baixo'
    dfOpcoesTesouro['Canal de Atendimento'] = 'https://www.tesourodireto.com.br/central-de-atendimento/entre-em-contato.htm'
    dfOpcoesTesouro.to_csv('dfTesouroOp.csv', sep = ';', encoding = 'ansi', index = False)
    return



def criar_resultado_RF_excel():
    try:
        dfCDBop = pd.read_csv('dfCDBop.csv', sep = ';', encoding = 'ansi')        
    except:
        pass        
    try:
        dfLCIop = pd.read_csv('dfLCIop.csv', sep = ';', encoding = 'ansi')        
    except:
        pass
    try:
        dfLCAop = pd.read_csv('dfLCAop.csv', sep = ';', encoding = 'ansi')        
    except:
        pass
    try:
        dfTesouroOp = pd.read_csv('dfTesouroOp.csv', sep = ';', encoding = 'ansi')        
    except:
        pass
    
    writer = pd.ExcelWriter('Opcoes_Adequadas_Renda_Fixa.xlsx', engine='xlsxwriter')
    
    try:
        dfCDBop.to_excel(writer, sheet_name='CDB', index = False)
    except:
        pass
    
    try:
        dfLCIop.to_excel(writer, sheet_name='LCI', index = False)
    except:
        pass
        
    try:
        dfLCAop.to_excel(writer, sheet_name='LCA', index = False)
    except:
        pass
        
    try:
        dfTesouroOp.to_excel(writer, sheet_name='Tesouro', index = False)
    except:
        pass

    writer.save()
    
    try:
        os.remove('dfCDBop.csv')
    except:
        pass

    try:
        os.remove('dfLCIop.csv')
    except:
        pass
    try:
        os.remove('dfLCAop.csv')
    except:
        pass

    try:
        os.remove('dfTesouroOp.csv')
    except:
        pass
    
    os.remove('CDB_Clean.csv')
    os.remove('LCI_Clean.csv')
    os.remove('LCA_Clean.csv')
    os.remove('tesouro_Clean.csv')    
    os.remove('completo_Clean.csv')
    
    return
    

 