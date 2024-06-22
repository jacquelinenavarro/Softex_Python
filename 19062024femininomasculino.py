# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra, escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe seu sexo, sendo [F] - Feminino e [M] - Masculino: ")

if sexo.upper () == "F":
    print("F - Feminino")

elif sexo.upper () == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido!")