import pandas as pd
import os

dfleitor = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\leitor_temp.csv', encoding='ansi',
                       sep=";")
print(dfleitor.iloc[0][2] == 1)