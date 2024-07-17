# Atividade 1:
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual número ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:
#  Tabuada de 5:
#  5 X 1 = 5
#  5 X 2 = 10
#  ...
#  5 X 10 = 50


# import funcoes

# n1 = float(input("Digite o número o qual deseja gerar a tabuada (entre 1 e 10): "))

# print(f'{n1} X {i} = ', funcoes.tabuada(n1))

import funcoes

n1 = int(input("Digite o número para gerar a tabuada (entre 1 e 10): "))

print(f'O resultado da tabuada de {n1} é:')
print(funcoes.tabuada(n1))
 
