#Aula 21 de agosto de 2026

# meunome = "Arthur"

# for i in meunome:
#     print(i)

# for i in range (1,10,2):
#     print(i)

# range (inicio,final,gap = intervalo)

#WHILE:

# somador = int(input("Registro: "))
# controle = 0

# while controle <= 30:
#     controle=controle+somador
#     somador = int(input("Registro: "))

# print("Oficina lotada")

#FOR
# for i in range(5):
#     try:
#  # i representa o número atual da repetição (0, 1, 2...)
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
 
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
 
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")
#         num = float(input("Digite um número: "))

# acertou = 0
# while acertou < 5:
#     print(f"Número {acertou + 1} de 5:") 
#     num = float(input("Digite um número: ")) 
        
#     dobro = num * 2 
#     triplo = num * 3 
#     quádruplo = num * 4 
        
#     print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     acertou+=1 

# Desafios:

# 1.Cálculo de Média Escolar para Vários Alunos

# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, 
# agora para 10 estudantes

# for i in range (10):
#     try:
#         nota_n_1 = float(input("Digite a primeira nota da avaliação normal: "))
#         nota_n_2 = float(input("Digite a segunda nota da avaliação normal: "))
#         media = (nota_n_1 + nota_n_2)/2
    
#         if media >= 6.0:
#             print("Aprovado")
#         elif media > 3:
#             print ("Recupercao")
#         else:
#             print("Reprovado")
#     except ValueError:
#          print("Erro emissão de valor")

# 2. Cadastro de Candidatos

# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.

# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.

# for i in range (10):
#     try:
#         idade = float(input("Digite a sua idade: "))
#         if idade > 18:
#             telefone = float(input("Digite um numero de contato: "))
#             email = int(input("Digite um e-mail de contato: "))
#         else:
#             print("Idade menor de 18 anos, não pode particpar da pesquisa")
#     except ValueError:
#          print("Erro")

# 3. Tentativa de Login e Senha
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio

# usuario = "arthur"
# senha = "senac"
# contador = 1
# limite = 4
# tentativa = contador + 1 
# while contador < limite:

#     try:

#         login_1 = input("Digite o seu login: ")
#         senha_2= input("Digite a sua senha: ")

#         if login_1 == usuario and senha == senha_2:
#             print("login realizado com sucesso")
#             break
#         else:
#             print("Senha incorreta, tentativa",contador,"de 3")
#             contador = contador + 1
#             if contador == 4:
#                 print("Senha Bloqueada")
            
#     except ValueError:
#         print("Entrada invalida")

   