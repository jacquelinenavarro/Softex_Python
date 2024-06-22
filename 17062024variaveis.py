#Fazer um programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a nota de unidade 1: "))
nota2 = float(input("Digite a nota de unidade 2: "))
nota3 = float(input("Digite a nota de unidade 3: "))
nota4 = float(input("Digite a nota de unidade 4: "))
media = (nota1 + nota2 + nota3 + nota4)/4

print(f"A média das notas {nota1:.2f}, {nota2:.2f}, "
      f"{nota3:.2f} e {nota4:.2f} é {media}"
      
)