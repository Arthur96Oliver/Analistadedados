#Aula 09 de agosto de 2026

import pandas as pd # alias 'pd'
import numpy as np  # alias 'np'
import openpyxl 

#LOC = buscar por coluna ou chaves 
#ILOC = buscar por indice
#Query = buscar por coluna

filmes = {
    'titulo':["Lagoa Azul", "Agente Secreto", "Gênio Indomavel","A freira", "Brinquedo Assasino", "Top Gun"],
    'categoria':["Romance","Acao","Drama", "Terror", "Comedia","Aventura"],
    'ano': ["1980","2025","1997","2022", "1995","1986"],
    'faturamento': [1,2,3,4,5,6]
}

indices = ["A","B","C","D", "E","F"]

tabela_filmes = pd.DataFrame(filmes, index=indices)
print (filmes)
print (type(filmes))
print(tabela_filmes)
print (type(tabela_filmes))

print (tabela_filmes.iloc[2])
print ('-'*20)
print(tabela_filmes.loc['B'])
print(tabela_filmes.loc['B':'E'])
print (tabela_filmes.iloc[1:3])
# print(tabela_filmes.query['titulo' != "Agente Secreto"])
# print ('-'*20)
consulta1 = tabela_filmes.query("faturamento == 5")
print(consulta1)