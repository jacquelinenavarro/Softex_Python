# Projetos de Lógica de Programação com Python

# Projeto escolhido: 10 - Loja e Produtos

# Descrição: Uma loja vende vários produtos.
# Cada produto é vendido por uma única loja.
# Relação: Uma loja -> Muitos produtos.

caminho_arquivo_produtos = 'produtos.txt'
caminho_arquivo_funcionarios = 'funcionarios.txt'

def cadastrar_funcionario():
    cpf = input('CPF do funcionário: ')
    with open(caminho_arquivo_funcionarios, 'r') as f:
        if cpf in f.read():
            print('CPF já cadastrado.')
            return
    nome = input('Nome do funcionário: ')
    sobrenome = input('Sobrenome do funcionário: ')
    data_nascimento = input('Data de nascimento do funcionário (dd/mm/aaaa): ')
    with open(caminho_arquivo_funcionarios, 'a') as f:
        f.write(f'{cpf},{nome},{sobrenome},{data_nascimento}\n')


def listar_funcionarios():
    with open(caminho_arquivo_funcionarios, 'r') as f:
        print(f.read())

def deletar_funcionario():
    cpf_a_deletar = input('CPF do funcionário a ser deletado: ')
    with open(caminho_arquivo_funcionarios, 'r') as f:
        linhas = f.readlines()
    with open(caminho_arquivo_funcionarios, 'w') as f:
        for linha in linhas:
            if linha.split(',')[0] != cpf_a_deletar:
                f.write(linha)

def alterar_funcionario():
    cpf_a_alterar = input('CPF do funcionário a ser alterado: ')
    with open(caminho_arquivo_funcionarios, 'r') as f:
        linhas = f.readlines()
    with open(caminho_arquivo_funcionarios, 'w') as f:
        for linha in linhas:
            if linha.split(',')[0] == cpf_a_alterar:
                print('Digite os novos dados do funcionário')
                cpf = input('CPF do funcionário: ')
                nome = input('Nome do funcionário: ')
                sobrenome = input('Sobrenome do funcionário: ')
                data_nascimento = input('Data de nascimento do funcionário (dd/mm/aaaa): ')
                f.write(f'{cpf},{nome},{sobrenome},{data_nascimento}\n')
            else:
                f.write(linha)

def cadastrar_produto():
    codigo = input('Código do produto: ')
    with open(caminho_arquivo_produtos, 'r') as f:
        if codigo in f.read():
            print('Código do produto já cadastrado.')
            return
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade em estoque: '))
    with open(caminho_arquivo_produtos, 'a') as f:
        f.write(f'{codigo},{nome},{preco},{quantidade}\n')

def listar_produtos():
    with open(caminho_arquivo_produtos, 'r') as f:
        print(f.read())

def deletar_produto():
    codigo_a_deletar = input('Código do produto a ser deletado: ')
    with open(caminho_arquivo_produtos, 'r') as f:
        linhas = f.readlines()
    with open(caminho_arquivo_produtos, 'w') as f:
        for linha in linhas:
            if linha.split(',')[0] != codigo_a_deletar:
                f.write(linha)

def alterar_produto():
    codigo_a_alterar = input('Código do produto a ser alterado: ')
    with open(caminho_arquivo_produtos, 'r') as f:
        linhas = f.readlines()
    with open(caminho_arquivo_produtos, 'w') as f:
        for linha in linhas:
            if linha.split(',')[0] == codigo_a_alterar:
                print('Digite os novos dados do produto')
                codigo = input('Código do produto: ')
                nome = input('Nome do produto: ')
                preco = float(input('Preço do produto: '))
                quantidade = int(input('Quantidade em estoque: '))
                f.write(f'{codigo},{nome},{preco},{quantidade}\n')
            else:
                f.write(linha)

while True:
    op = input("Digite o módulo: (f)funcionário, (p)produto, (s)sair: ")

    if op == 's':
        break

    elif op == 'f':
        op_funcionario = input('c - Cadastrar funcionário; l - Listar funcionários; d - Deletar funcionário; a - Alterar funcionário: ')

        if op_funcionario == 'c':
            cadastrar_funcionario()
        elif op_funcionario == 'l':
            listar_funcionarios()
        elif op_funcionario == 'd':
            deletar_funcionario()
        elif op_funcionario == 'a':
            alterar_funcionario()

    elif op == 'p':
        op_produto = input('c - Cadastrar produto; l - Listar produtos; d - Deletar produto; a - Alterar produto: ')

        if op_produto == 'c':
            cadastrar_produto()
        elif op_produto == 'l':
            listar_produtos()
        elif op_produto == 'd':
            deletar_produto()
        elif op_produto == 'a':
            alterar_produto()
