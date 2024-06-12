# Estrutura de Controle If Else: ● Sintaxe básica do if e else.
# Par ou Ímpar
# num = int(input("Digite um número: "))
# if num % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# Python - Exercícios

#1.Escreva um algoritmo que solicite ao usuário dois números e exiba a soma deles.

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# soma = num1 + num2
# print("A soma dos dois números é {}".format(soma))

# 2. Crie um algoritmo que verifique se um número é par ou ímpar.
# num = int(input("Digite um número: "))
# if num % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# 3. Desenvolva um algoritmo que leia três números e exiba o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é {}".format(num1))

elif num2 > num1 and num2 > num3:
    print("O maior número é {}".format(num2))

elif num3 > num1 and num3 > num2:
    print("O maior número é {}".format(num3))

