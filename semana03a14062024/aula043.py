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

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))

# if num1 > num2 and num1 > num3:
#     print("O maior número é {}".format(num1))

# elif num2 > num1 and num2 > num3:
#     print("O maior número é {}".format(num2))

# elif num3 > num1 and num3 > num2:
#     print("O maior número é {}".format(num3))

# # 4.Crie um programa Python que solicite ao usuário uma temperatura em Fahrenheit e converta para Celsius.
# f = float(input("Digite a temperatura em Fahrenheit que deseja convertar para Celsius: "))

# C = (f-32)/1.8

# print(f"A temperatura em Celsius é {C:.2f}°C")


#5.Escreva um programa Python que determine se um número fornecido pelo usuário é positivo, negativo ou zero.


numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


