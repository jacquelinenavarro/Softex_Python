# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
# Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link
# (em minutos).

tamanho = float(input("Digite o tamanho do arquivo, em MB: "))
velocidade = float(input("Digite a velocidade da conexão, em Mbps: "))
tempo = (tamanho * 8) / velocidade # O operador '/' realiza a divisão real entre dois valores.
minutos = tempo // 60    # '//' Retorna apenas a parte inteira do resultado da divisão.
segundos = tempo % 60  # '%' é uma maneira conveniente de obter a parte dos segundos após a divisão por 60.
print(f"{minutos:.0f} Minutos e {segundos:.0f} Segundos")

