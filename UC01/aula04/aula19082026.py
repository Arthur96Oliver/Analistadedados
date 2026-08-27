#Aula de 19 de agosto de 2026
#git init
#git clone
#git push-u = Atualizar a maquina para o diretorio (site)
#git pull = Atualizar o diretorio (site) para maquina

#Passo a passo para salvar git: 1) git add . 2) git commit -m "texto" 3)git push


#Exericio (If/Elif/Else)

# nome = input("Informe seu nome: ")
# if nome == "Arthur":
#     resposta = "Arthur presente!"
# elif nome == "Phellipe":
#     resposta = "Phellpe presente!"

#Exercicio (Match/case)

# mes= input("informe o mês de nascimento: ")

# if mes == 1:
#     signo = "Aquario"
# elif mes == 2:
#     signo = "Peixe"
# else:
#     signo = "Aries"

# print(f"Seu signo é {signo}")

"""Versão do professor (if/elif/else)"""

# mes = int(input("Informe o mês de seu nascimento:"))

# if mes==1:
#     signo="Aquário"
# elif mes==2:
#     signo="Peixes"
# elif mes==3:
#     signo="Áries"
# elif mes==4:
#     signo="Touro"
# elif mes==5:
#     signo="Gêmeos"
# elif mes==6:
#     signo="Câncer"
# elif mes==7:
#     signo="Leão"
# elif mes==8:
#     signo="Virgem"
# elif mes==9:
#     signo="Libra"
# elif mes==10:
#     signo="Escorpião"
# elif mes==11:
#     signo="Sagitário"
# else:
#     signo="Capricórnio"

# print(f"Seu signo é {signo}.")

'''Versao match/case/case_'''

# mes= int(input("informe o mês de nascimento: "))

# match mes:
#     case 1:
#         signo="Aquario"
#     case 2:
#             signo="Peixe"
#     case 3:
#             signo="Leão"
#     case _:
#         signo="Numero de mês invalido"

# print(f"O seu signo é {signo}")


#1. Cálculo de Lâmpadas:

# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
#Dados de entrada: a potência da  lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. 
# Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3m² existe um bocal para uma lâmpada. 

# potencia = int(input("informe a potencia: "))

# if potencia >3:
#     print("Potencia acima do permitido, potencia sugerida 3 watts")
# elif potencia <3:
#      print("Potencia abaixo do permitido, potencia sugerida 3 watts")

# if potencia == 3:
#      largura = int(input("Informe a largura: "))
#      comprimento = int(input("Informe o comprimento: "))
#      metro_2 = largura*comprimento
#      lampada=(metro_2)/3
#      print(f"A quantidade necessaria de lampada é {lampada}")



#  2. Quantidade de Caixas de Azulejos:

# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,  largura e altura), calcular e escrever a quantidade 
# de caixas de azulejos para se colocar em  todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m² 


# azulejos = float(input("informe a dimensão da caixa: "))

# if azulejos > 1.5:
#     print("Dimensão acima do permitido, dimensão sugerida 1.5 m²")
# elif azulejos <1.5:
#      print("Dimensão abaixo do permitido, dimensão sugerida 1.5 m²")

# if azulejos == 1.5:
#     comprimento = int(input("Qual é o comprimento: "))
#     largura = int(input("Qual é a largura: "))
#     altura = int(input("Qual é altura: "))
#     caixa = (largura*altura)/1.5
#     print(f"Serão necessaria {caixa} caixas para colocar em todas as paredes")

#  3. Rendimento do Taxista:

# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o  preço do combustível é de R$ 6,15, 
# escreva um programa para ler: a marcação do # odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a  média do consumo em km/L e o lucro (líquido) do dia.

# COMBUSTIVEL = 6.15
# odometro_i = float(input("Qual é a marcação do odômetro no início do dia: "))
# odometro_f = float(input("Qual é a marcação do odômetro no fim do dia: "))
# litro = int(input("Consumo de litro gasto: "))
# v_recebido = float(input("Valor recebido no final do dia: "))

# if odometro_i >= odometro_f:
#     print("Valor do odometro maior ou igual a odomentro final")
# elif litro == 0:
#     print("Valor do consumo de litro invalido, valor tem que ser maior que 0")
# else:
#     odometro_r = odometro_f - odometro_i
#     litro_g = odometro_r/litro
#     valor_gasto = COMBUSTIVEL*litro_g
#     Lucro_liquido = valor_gasto - v_recebido
#     print(f"A media de cosumo foi {litro_g:.2f} e o lucro do dia foi {Lucro_liquido:.2f}")


# 4. Código de Origem do Produto:

# Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela abaixo:

# C_produto = float(input("Inserir o código do produto:"))

# match C_produto:
#     case 1:
#         print("Seu produto é procêdencia: Sul")
#     case 2:
#         print("Seu produto é procêdencia: Norte")
#     case 3:
#         print("Seu produto é procêdencia: Leste")
#     case 4:
#         print("Seu produto é procêdencia: Oeste")
#     case 5 | 6:
#         print("Seu produto é procêdencia: Nordeste")
#     case 7 | 8 | 9:
#          print("Seu produto é procêdencia: Sudeste")
#     case 10:
#          print("Seu produto é procêdencia: Centro-Oeste")
#     case 11:
#          print("Seu produto é procêdencia: Noroeste")
#     case _:
#          print("Seu produto é procêdencia: Importada")
        




# Observação: caso o código não seja nenhum dos especificados, o produto deve ser # encarado como “Importado”.

# 5. Média do Aluno com Optativa:

# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação  optativa dos estudantes de uma turma. 
# Caso o estudante não tenha feito a optativa, deve  ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e  mensagens que indiquem se o estudante foi aprovado,
#  reprovado ou se está em recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0

# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o resultado final.

nota_n_1 = float(input("Digite a primeira nota da avaliação normal: "))
nota_n_2 = float(input("Digite a segunda nota da avaliação normal:"))
f_prova_op = (input("Fez a prova optativa (sim/nao): "))
media = (nota_n_1 + nota_n_2)/2
if f_prova_op == "sim":
    nota_op = float(input("informe a nota da prova optativa: "))
elif f_prova_op == "nao":
    nota_op = -1

if nota_n_1 < nota_op:
    media = (nota_n_2 + nota_op)/2
elif nota_n_2 < nota_op:
    media = (nota_n_1 + nota_op)/2


if media >= 6.0:
    print("Aprovado")
elif media > 3:
    print ("Recupercao")
else:
    print("Reprovado")

# 6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo

# numero_1 = float(input("Inserir o valor: "))

# if numero_1 >= 0:
#     print("O valor escolhido é positivo")
# else:
#     print("O valor escolhido é negativo")