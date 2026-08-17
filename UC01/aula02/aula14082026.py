#Aula 02 de 14 de agosto de 2026
# logica condiconal 
# and = Só sera verdade se todos forem verdadeiro
# or = Só basta uma verdeira para ser verdade
# not = nega o valores logicos 
# if = se
# else= se não
# elif = se somente se
# input = inserir uma caixa para colocar a variavel


#exemplo 1 
# x=100
# y=99.9

# print("x é maior que y:", x > y)
# print("x é igual a y: ", x == y)

#exemplo 2 

# cnh = True
# bebida = False

# posso_dirigir= cnh and bebida
# print(posso_dirigir)

#exemplo 3 

# Trem = True
# onibus = False
# venho_para_aula = Trem or onibus
# print("Posso ir a aula hoje: ", venho_para_aula)

#Exemplo

locomocao = input("diga a sua locomocao: ")
choveu = True

if choveu and locomocao == "moto":
    resultado = "To todo molhado :("
elif not choveu and locomocao == "moto":
    resultado = "to seco"
else:
    resultado = "To seco:)"

print(resultado)
