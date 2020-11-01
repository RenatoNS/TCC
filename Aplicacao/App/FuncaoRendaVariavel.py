#%% Importar Bibliotecas

import gdown
import pandas as pd
import os


def download_opcoesRV():
    try:
        url = 'https://drive.google.com/uc?id=1qwx-7R3fT4n2488xpg9m24uSy0dcQVFD'
        gdown.download(url, 'carteiraRV.csv', quiet = True)
        carteiraRV = pd.read_csv('carteiraRV.csv', sep = ';', encoding = 'ansi')
        writer = pd.ExcelWriter('Opcoes_Adequadas_Renda_Variavel.xlsx', engine='xlsxwriter')
        carteiraRV.to_excel(writer, sheet_name='Carteira Renda Variavel', index = False)
        writer.save()
        os.remove('carteiraRV.csv')
    except:
        pass

