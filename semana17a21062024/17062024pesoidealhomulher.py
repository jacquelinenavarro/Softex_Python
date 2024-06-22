# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("Digite seu sexo ('M' para masculino e 'F' para feminino): ")

h = float(input("Digite a sua altura (em metros): "))

if sexo.upper() == "F":
    peso_ideal = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {peso_ideal:.2f} kg")
elif sexo.upper() == "M":
    peso_ideal = (72.7 * h) - 58
    print(f"Seu peso ideal é {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")