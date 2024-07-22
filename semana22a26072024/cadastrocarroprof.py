def criar_carro(marca, modelo, ano, cor):
    return {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor       
        
    }

def ligar_motor():
    print(f"Motor do carro ligado. ")

def desligar_motor():
    print('O motor do carro está desligado. ' )

def obter_informacoes(carro):
    return f"Carro: {carro['marca']} {carro: ['modelo']}, Ano: {carro['ano']}, cor: {carro['cor']}"

carro1 = criar_carro ("Toyota", "Corolla", 2023, "Prata")

ligar_motor()
print(obter_informacoes(carro1))

desligar_motor()