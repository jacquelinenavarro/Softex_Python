# Desafio Nível Inicial.
# Questão:
# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


import funcoes

num_eleitores = funcoes.obter_numero_eleitores()

while True:
    print("\n========= Menu ========")
    print("1. Votar")
    print("2. Mostrar resultados")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        votos = funcoes.contar_votos(num_eleitores)
    elif opcao == '2':
        funcoes.mostrar_resultados(votos)
    elif opcao == '3':
        print("Você saiu do sistema!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
