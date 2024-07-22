#Atividade: 22/07/2024
# O objetivo deste programa em Python é desenvolver um sistema simples para cadastrar carros, onde cada carro é identificado
# por sua marca, modelo, ano e cor. O sistema deve permitir realizar operações básicas com os carros, como ligar/desligar o motor,
# obter informações sobre o carro e outras funções específicas.

# Exemplo:
#   marca = ‘Fiat’
#   liga_carro():
#   print(‘O motor está ligado’)

# Lista para armazenar os carros cadastrados
carros = []

# Função para cadastrar um carro
def cadastrar_carro():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    cor = input("Digite a cor do carro: ")
    carro = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor,
        'motor_ligado': False
    }
    carros.append(carro)
    print(f"Carro {marca} {modelo} cadastrado com sucesso!")

# Função para listar os carros cadastrados
def listar_carros():
    if not carros:
        print("Nenhum carro cadastrado.")
    else:
        for i, carro in enumerate(carros, start=1):
            print(f"{i}. Marca: {carro['marca']}, Modelo: {carro['modelo']}, Ano: {carro['ano']}, Cor: {carro['cor']}")

# Função para ligar o carro
def ligar_carro(carro):
    if not carro['motor_ligado']:
        carro['motor_ligado'] = True
        print(f"O motor do {carro['marca']} {carro['modelo']} está ligado.")
    else:
        print(f"O motor do {carro['marca']} {carro['modelo']} já está ligado.")

# Função para desligar o carro
def desligar_carro(carro):
    if carro['motor_ligado']:
        carro['motor_ligado'] = False
        print(f"O motor do {carro['marca']} {carro['modelo']} está desligado.")
    else:
        print(f"O motor do {carro['marca']} {carro['modelo']} já está desligado.")

# Loop principal do programa
while True:
    print("\n========= Menu ========")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Ligar carro")
    print("4. Desligar carro")
    print("5. Sair do sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_carro()
    elif opcao == '2':
        listar_carros()
    elif opcao == '3':
        listar_carros()
        indice = int(input("Escolha o número do carro para ligar: ")) - 1
        if 0 <= indice < len(carros):
            ligar_carro(carros[indice])
        else:
            print("Carro inválido.")
    elif opcao == '4':
        listar_carros()
        indice = int(input("Escolha o número do carro para desligar: ")) - 1
        if 0 <= indice < len(carros):
            desligar_carro(carros[indice])
        else:
            print("Carro inválido.")
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
