
import numpy as np
import pandas as pd
import os
import time

os.chdir('../Sistema/Controle')


class Conexao:

    def verificar_vazio(self):
        return not(os.path.exists('../Controle/Clientes.csv'))


    def criar_login(self, login, senha):
        informacoes = [[login, senha]]
        frame = pd.DataFrame(informacoes, columns=["login", "senha"])
        frame.to_csv("Login_temp.csv", encoding='ansi')

    def pesquisar_login(self,login):
        frame = pd.read_csv('../Controle/Clientes.csv', encoding='ansi')
        a = list(frame['Login'])
        if(login in a):
            return True
        else:
            return False

    def criar_primeira_conta(self, respostas, respostas2):
        frame = pd.read_csv('../Controle/Login_temp.csv', encoding='ansi', index_col=0)
        login = list(frame["login"])
        senha = list(frame["senha"])
        respostas2.sort()
        if (respostas2[4] == 0):
            perfil = "Conservador"
        elif (respostas2[4] == 1):
            perfil = "Conservador"
        elif (respostas2[4] == 2):
            perfil = "Moderado"
        else:
            perfil = "Agressivo"
        respostas.append(login[0])
        respostas.append(senha[0])
        respostas.append(perfil)
        informacoes = [respostas]
        columns = ["Qual sua faixa etária",
                   "Qual percentual do seu patrimônio está investido? (Carros, casas, ações, etc)",
                   "Qual o objetivo dos seus investimentos?",
                   "Como você se sentiria caso verificasse perdas em seus investimentos?",
                   "Quais são as aplicações financeiras em que você tem experiência?",
                   "Possui algum conhecimento sobre o mercado financeiro?",
                   "Qual sua escolaridade ?",
                   "Você costuma operar financeiramente com que frequência?",
                   "Você espera precisar de renda extra no futuro?",
                   "Qual o tempo disponível que você tem para manter seu dinheiro aplicado?",
                   "Login",
                   "Senha",
                   "Perfil"]
        frame = pd.DataFrame(informacoes, columns=columns)
        frame["lidorf"]=0
        frame["lidorv"]=0
        frame["mes_criacao"]=time.strftime('%m')
        frame["ano_criacao"]=time.strftime('%y')
        frame.to_csv("Clientes.csv", sep=";", encoding='ansi')
        os.remove('../Controle/Login_temp.csv')

    def criar_conta(self, respostas, respostas2):
        framelogin = pd.read_csv('../Controle/Login_temp.csv', encoding='ansi')
        frameclientes = pd.read_csv('../Controle/Clientes.csv', encoding='ansi', sep=";", index_col=0)
        login = list(framelogin["login"])
        senha = list(framelogin["senha"])
        respostas2.sort()
        if (respostas2[4] == 0):
            perfil = "Conservador"
        elif (respostas2[4] == 1):
            perfil = "Conservador"
        elif (respostas2[4] == 2):
            perfil = "Moderado"
        else:
            perfil = "Agressivo"
        respostas.append(login[0])
        respostas.append(senha[0])
        respostas.append(perfil)
        respostas.append(0)
        respostas.append(0)
        respostas.append(time.strftime('%m'))
        respostas.append(time.strftime('%y'))
        informacoes = [respostas]
        columns = ["Qual sua faixa etária",
                   "Qual percentual do seu patrimônio está investido? (Carros, casas, ações, etc)",
                   "Qual o objetivo dos seus investimentos?",
                   "Como você se sentiria caso verificasse perdas em seus investimentos?",
                   "Quais são as aplicações financeiras em que você tem experiência?",
                   "Possui algum conhecimento sobre o mercado financeiro?",
                   "Qual sua escolaridade ?",
                   "Você costuma operar financeiramente com que frequência?",
                   "Você espera precisar de renda extra no futuro?",
                   "Qual o tempo disponível que você tem para manter seu dinheiro aplicado?",
                   "Login",
                   "Senha",
                   "Perfil",
                   "lidorf",
                   "lidorv",
                   "mes_criacao",
                   "ano_criacao"]
        frame = pd.DataFrame(informacoes, columns=columns)
        frame.to_csv("Clientes1.csv", sep=";", encoding='ansi')
        framelogin = pd.read_csv('../Controle/Clientes1.csv', encoding='ansi', sep=";", index_col=0)
        frames = pd.concat([frameclientes, framelogin], ignore_index=True)
        frames.to_csv("Clientes.csv", sep=";", encoding='ansi')

        os.remove('../Controle/Clientes1.csv')
        os.remove('../Controle/Login_temp.csv')