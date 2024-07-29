# Classe Produto:

class Produto:
    # Construtor da Classe
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Método da minha classe Produto:

    def relatorioProduto(self):
        print(f"Produto: {self.nome} - Preco: {self.preco}")

# Classe Avaliação:
class Avaliacao:
    def __init__(self, produto, nota, comentario):
        self.produto = produto
        self.nota = nota
        self.comentario = comentario
    

#Objetos: 
produto1 = Produto('Biscoito', 10)
produto1.relatorioProduto()
produto2 = Produto('Bolacha', 8)
produto2.relatorioProduto()

avaliacao1 = Avaliacao(produto1, 4, 'Muito ruim')


print(produto1.nome, produto1.preco)
print(avaliacao1.produto.nome, avaliacao1.nota, avaliacao1.comentario)





    
    