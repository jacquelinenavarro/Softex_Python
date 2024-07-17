
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
