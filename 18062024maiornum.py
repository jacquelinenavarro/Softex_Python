# Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1:.0f} é maior que o número {num2:.0f}.")

else:
    print(f"O número {num2:.0f} é maior que o número {num1:.0f}.")