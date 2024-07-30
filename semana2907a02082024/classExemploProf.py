class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def imprimir(self):
        return f"Nome: {self.nome}, Preço: {self.preco}"

class Avalicao:

    def __init__(self, produto, nota , comentario):
        self.produto = produto
        self.nota = nota
        self.comentario = comentario

    def imprimirAvalicao(self):
        return f"Avaliação: Produto: {self.produto.nome} -  Nota: {self.nota} - Comentario: {self.comentario}"
    
produto1 = Produto("Queijo", 30)

avaliacao1 = Avalicao(produto1, 5, "Queijo mussarela muito bom!!")

print(produto1.imprimir())
print(avaliacao1.imprimirAvalicao())