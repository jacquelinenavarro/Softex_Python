#import funcoes

# n1 = 10
# n2 = 20
# print(funcoes.soma(n1,n2))
# print(funcoes.multiplicacao(n1,n2))

import funcoes

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

while True:
    print("\n========= Menu ========")
    print("1. Para somar")
    print("2. Para subtrair")
    print("3. Para multiplicar")
    print("4. Para dividir")
    print("5. Você saiu do sistema com sucesso!")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print(f'A soma entre os números {n1} e {n2} é ', funcoes.soma(n1, n2))
    elif opcao == '2':
        print(f'A subtração entre os números {n1} e {n2} é ', funcoes.subtracao(n1, n2))
    elif opcao == '3':
        print(f'A multiplicação entre os números {n1} e {n2} é ', funcoes.multiplicacao(n1, n2))
    elif opcao == '4':
        print(f'A divisão entre os números {n1} e {n2} é ', funcoes.divisao(n1, n2))
    elif opcao == '5':
        print("Você saiu do sistema!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")