#%% Importar bibliotecas

import gdown
import pandas as pd
import os

#%% Definir diretorio para salvar os dados

os.chdir(r'C:\Users\Renato\Desktop\TCC')
# os.getcwd()

#%% ids dos arquivos em nuvem

file_id="1n1F7TMFnPLK6u7l7eRp8u04m74iu1QMV"
url = f'https://drive.google.com/uc?id={file_id}'

output = 'teste.csv'
#%%

gdown.download(url, output, quiet=False) 

df = pd.read_csv('teste.csv')
print(df.head())

