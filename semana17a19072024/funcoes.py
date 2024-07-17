
def soma(parametro1, parametro2):
    soma = parametro1 + parametro2
    return soma

def subtracao(parametro1, parametro2):
    subtracao = parametro1 - parametro2
    return subtracao

def multiplicacao(parametro1, parametro2):
    multiplicacao = parametro1 * parametro2
    return multiplicacao

def divisao(parametro1, parametro2):
    divisao = parametro1 / parametro2
    return divisao

def tabuada(parametro1):
    for i in range(1, 11):
        tabuada = parametro1 * i
        print(f'{parametro1} X {i} = {tabuada}')

# ---------------------------------#

# Funções do Desafio Nível Inicial: Elição


def obter_numero_eleitores():
    return int(input("Digite o número total de eleitores: "))

def obter_voto():
    while True:
        voto = int(input("Digite o número do candidato (1, 2 ou 3): "))
        if voto in [1, 2, 3]:
            return voto
        else:
            print("Voto inválido. Tente novamente.")

def contar_votos(num_eleitores):
    votos = {1: 0, 2: 0, 3: 0}
    for i in range(num_eleitores):
        voto = obter_voto()
        votos[voto] += 1
    return votos

def mostrar_resultados(votos):
    for candidato, num_votos in votos.items():
        print(f"Candidato {candidato} recebeu {num_votos} votos.")
# ---------------------------------#

# Funções do Desafio Nível Avançado: Eleição

def mostrar_vencedor(votos):
    vencedor = max(votos, key=votos.get)
    print(f"O candidato vencedor é o {vencedor} com {votos[vencedor]} votos.")
