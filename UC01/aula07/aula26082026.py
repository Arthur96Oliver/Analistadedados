# Aula de 26 de agosto de 2026

def calculadora_v1(num1,num2,operador):
      
    # num1 = float(input("Digite o primeiro numero: "))
    # num2 = float(input("Digite o segundo numero: "))
    # operador = input("Digite a operação desejada 1. soma, 2. subtracao, 3. multiplicao, 4. Divisao: ")



    match operador:
        case "1":
            print(f"Resultado da soma {num1+num2}.")
        case "2":
                print(f"Resultado da subtração {num1-num2}.")
        case "3":
                print(f"Resultado da multiplicação {num1*num2}.")
        case "4":
                if num2 == 0:
                    print(f"Dividiu por zero")
                else:
                    print(f"Resultado da divisao {num1/num2}.")
        case _:
            print("Operador invalido")

calculadora_v1(1,2,"3")
