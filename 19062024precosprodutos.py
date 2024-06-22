# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
# que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))

if produto1 < produto2 and produto1 < produto3:
    print("Compre o produto 1. Ele é o mais barato entre os três que você informou!")

elif produto2 < produto1 and produto2 < produto3:
    print("Compre o produto 2. Ele é o mais barato entre os três que você informou!")

else:
    print("Compre o produto 3. Ele é o mais barato entre os três que você informou!")
