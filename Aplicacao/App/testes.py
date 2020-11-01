import pandas as pd
import time

frame = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\Clientes.csv', encoding='ansi', sep=";")
index = 0
senha = list(frame["Senha"])
perfil = list(frame["Perfil"])
mes = list(frame["mes_criacao"])
ano = list(frame["ano_criacao"])

print(10 != 10 & 8 >= 8)

