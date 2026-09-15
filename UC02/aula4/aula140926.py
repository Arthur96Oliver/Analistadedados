"""Aula 14 de agosto de 2026"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dados = np.array([12,15,17,20,22,25,28,30,35,40])
# print(dados)

# q1 = np.percentile(dados,25)
# q2 = np.percentile(dados,50)
# q3 = np.percentile(dados,75)
# print(f"primeiro quartil(Q1):{q1}")
# print(f"segundo quartil(Q2,mediana):{q2}")
# print(f"terceiro quartil(Q3):{q3}")

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name="Transacoes")
# print(df_transacoes.head(7))
q1_preco = df_transacoes['preco'].quantile(0.25)
q2_preco = df_transacoes['preco'].quantile(0.50)
q1_preco = df_transacoes['preco'].quantile(0.75)

contagem_operacao = df_transacoes['operacao'].value_counts()
contagem_operacao.plot(kind='bar', title='Tipos de opreração')

plt.show()