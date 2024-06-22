# Desafio 2: Elabore um algoritmo que receba o nome do estudante, a primeira e a segunda nota da avaliação. Ao final
# exiba o nome, a primeira nota, a segunda nota e a média do estudante.

nome = input('Digite o nome do estudante: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print ('A média do(a) estudante {} é {}'.format(nome, media))