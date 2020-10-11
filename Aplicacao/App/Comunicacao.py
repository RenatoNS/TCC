import numpy as np
import pandas as pd
import os

os.chdir(r'C:\TCC\Aplicacao\Arquivos CSV')


class Conexao:

    def verificar_vazio(self):
        return not(os.path.exists('C:\TCC\Aplicacao\Arquivos CSV\Clientes.csv'))

    def criar_login(self, login, senha):
        informacoes = [[login, senha]]
        frame = pd.DataFrame(informacoes, columns=["login", "senha"])
        frame.to_csv("Login_temp.csv", encoding='utf-8')

    def pesquisar_login(self,login):
        frame = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\Clientes.csv', encoding='#ISO-8859-1')
        a = list(frame['Login'])
        if(login in a):
            return True
        else:
            return False

    def criar_primeira_conta(self, respostas):
        frame = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\Login_temp.csv', encoding='#ISO-8859-1')
        login = list(frame["login"])
        senha = list(frame["senha"])
        respostas.append(login[0])
        respostas.append(senha[0])
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
                   "Senha"]
        frame = pd.DataFrame(informacoes, columns=columns)
        frame.to_csv("Clientes.csv", sep=";", encoding='ansi')

    def criar_conta(self, respostas):
        frame = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\Clientes.csv', encoding='#ISO-8859-1')
        frame = pd.read_csv('C:\TCC\Aplicacao\Arquivos CSV\Login_temp.csv', encoding='#ISO-8859-1')
        login = list(frame["login"])
        senha = list(frame["senha"])
        respostas.append(login[0])
        respostas.append(senha[0])
        informacoes = [respostas]


