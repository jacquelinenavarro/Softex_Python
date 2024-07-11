# O arquivo README.md, desta pasta, contém as informações deste projeto.

# Caminho do arquivo para armazenar as tarefas
arquivo_tarefas = 'tarefas.txt'

# Lista para armazenar as tarefas
tarefas = []


# Função para carregar as tarefas do arquivo
def carregar_tarefas():
    try:
        with open(arquivo_tarefas, 'r') as f:
            for linha in f:
                # Remove espaços em branco das extremidades e divide a linha no caractere '|'
                descricao, data_prevista = linha.strip().split('|')
                # Adiciona um dicionário com a descrição e data prevista à lista de tarefas
                tarefas.append({'descricao': descricao, 'data_prevista': data_prevista})
    except FileNotFoundError:
        # Se o arquivo não existir, cria um arquivo vazio
        open(arquivo_tarefas, 'w').close()


# Função para salvar as tarefas no arquivo
def salvar_tarefas():
    with open(arquivo_tarefas, 'w') as f:
        for tarefa in tarefas:
            # Escreve cada tarefa no arquivo com a descrição e data prevista separadas por '|'
            f.write(f"{tarefa['descricao']}|{tarefa['data_prevista']}\n")


# Função para cadastrar uma tarefa
def cadastrar_tarefa():
    descricao = input('Descrição da tarefa: ')
    data_prevista = input('Data prevista para concluir a tarefa (dd/mm/aaaa): ')
    # Adiciona a nova tarefa à lista de tarefas
    tarefas.append({'descricao': descricao, 'data_prevista': data_prevista})
    salvar_tarefas()
    print('Tarefa cadastrada com sucesso!')


# Função para listar tarefas
def listar_tarefas():
    if tarefas:
        print('\nLista de Tarefas:')
        # Enumera as tarefas, começando a contagem em 1
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['descricao']} (Data prevista: {tarefa['data_prevista']})")
    else:
        print('Nenhuma tarefa cadastrada.')


# Função para alterar uma tarefa
def alterar_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            # Tenta converter a entrada do usuário para um número inteiro
            indice = int(input('\nNúmero da tarefa a ser alterada: ')) - 1
            # Verifica se o índice está dentro do intervalo da lista de tarefas
            if 0 <= indice < len(tarefas):
                descricao = input('Nova descrição da tarefa: ')
                data_prevista = input('Nova data prevista para concluir a tarefa (dd/mm/aaaa): ')
                tarefas[indice] = {'descricao': descricao, 'data_prevista': data_prevista}
                salvar_tarefas()
                print('Tarefa alterada com sucesso!')
            else:
                print('Número de tarefa inválido.')
        except ValueError:
            # Captura erros de valor, caso a entrada não seja um número válido
            print('Entrada inválida. Por favor, insira um número.')


# Função para excluir uma tarefa
def excluir_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            # Tenta converter a entrada do usuário para um número inteiro
            indice = int(input('\nNúmero da tarefa a ser excluída: ')) - 1
            # Verifica se o índice está dentro do intervalo da lista de tarefas
            if 0 <= indice < len(tarefas):
                # Remove a tarefa da lista de tarefas
                tarefas.pop(indice)
                salvar_tarefas()
                print('Tarefa excluída com sucesso!')
            else:
                print('Número de tarefa inválido.')
        except ValueError:
            # Captura erros de valor, caso a entrada não seja um número válido
            print('Entrada inválida. Por favor, insira um número.')


# Carregar as tarefas ao iniciar o programa
carregar_tarefas()

# Loop principal do programa
while True:
    print("\n========= Menu ========")
    print("1. Cadastrar uma tarefa")
    print("2. Alterar uma tarefa")
    print("3. Excluir uma tarefa")
    print("4. Listar tarefas")
    print("5. Sair do sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_tarefa()
    elif opcao == '2':
        alterar_tarefa()
    elif opcao == '3':
        excluir_tarefa()
    elif opcao == '4':
        listar_tarefas()
    elif opcao == '5':
        print("Você saiu do sistema! ")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
