import pandas as pd # alias 'pd'
import numpy as np  # alias 'np'
import openpyxl 
# # numeros_impares = [43,55,1,3,11,27,109]
# # numeros_seq = [2,3,4,5,6,6,7]
# # # print(type(numeros_impares))

# # serie_impares = pd.Series(numeros_impares)
# # print(serie_impares)
# # print(type(serie_impares))

# # print(serie_impares.sum())
# # print(serie_impares.mean())
# # print(serie_impares.min())
# # print(serie_impares.max())
# # print(len(serie_impares))
# # print(serie_impares.describe())
# # print(serie_impares[serie_impares>50])

# # serie2_impares = pd.Series(
# #     numeros_impares,
# #       index =['a','b','c','d','e','f','g'])
# # print(serie2_impares)

# # filmes = {
# #     'titulo':["Lagoa Azul", "Agente Secreto", "Gênio Indomavel"],
# #     'categoria':["Romance","Acao","Drama"],
# #     'ano': ["1980","2025","1997"]
# # }

# # tabela_filmes = pd.DataFrame(filmes)
# # print (filmes)
# # print (type(filmes))
# # print(tabela_filmes)
# # print (type(tabela_filmes))

# # print (serie_impares)


# # quadrado_serie_impares = serie_impares*serie_impares
# # print(quadrado_serie_impares)

# ###LEITURA ARQUIVOS XLSX

'''Revisar e tratar os dados e funções abaixos '''

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name="Transacoes")
df_ativos = pd.read_excel('base_invest.xlsx', sheet_name="Ativo")
df_participantes = pd.read_excel('base_invest.xlsx', sheet_name="Participante")
df_compra=df_transacoes[df_transacoes['operacao']=='compra']
df_venda=df_transacoes[df_transacoes['operacao']=='venda']

# print(df_transacoes)

# max_compra_preco = df_compra['preco'].max()
# min_compra_preco = df_compra['preco'].min()
# max_venda_preco = df_venda['preco'].max()
# min_venda_preco = df_venda['preco'].min()

# print(max_compra_preco)

# df_transacoes['valor_total'] = df_transacoes['quantidade']*df_transacoes['preco']
# # print(df_transacoes)

# valor_por_ativo =df_transacoes.groupby('id_ativo')['valor_total'].sum()

# id_ativo_maior_valor = valor_por_ativo.idxmax()
# print(id_ativo_maior_valor)

# cnpj_maior_valor = df_ativos[df_ativos['id_ativo']==id_ativo_maior_valor]['cnpj'].iloc[0]
# print (cnpj_maior_valor)


