#Aula de 28 de agosto de 2026

# 1. DEFINIÇÃO  da função

# import time

# def dar_boas_vindas():
#     print("-"*40)
#     print("Bem vindo o nosso aplicativo!😁")
#     print("-"*40)

# # 2. CHAMADA da função

# print("Inicio do programa.")
# print("Por favor,aguarde...")
# time.sleep(2) #Simula uma pausa
# dar_boas_vindas()
# print("Meio de programa")

# Sorteio de numeros

# import random
# numero_random = random.randint(1,30)

# print(numero_random)

# def sorteiame():
#     """Algoritimo escolhe e retorna um numero inteiro aleatorio no intervalo 1 até 30"""
#     import random
#     numero_random = random.randint(1,30)
#     return numero_random

# sorteiame()
# resultado = sorteiame ()
# print(resultado)

# 2. Calculadora de IMC

def calculadora_ncm():
    contador = 1
    npessoa = 3

    while contador < npessoa:
        try:

            peso = float(input("Digite o seu peso: "))
            altura = float(input("Digite a sua altura: "))
            ncm = peso/(altura*altura)

            if ncm < 18.5:
                print("Abaixo do peso")
            elif ncm >= 18.5 and ncm <= 24.9:
                print("Peso normal")
            elif ncm >= 25.0 and ncm <= 29.9:
                print("Sobrepeso")
            else:
                print("Obesidade")
            contador = contador + 1
        except ValueError:
            print("Entrada invalida")
            contador = contador + 1
    return calculadora_ncm


