class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"{self.nome} - {self.idade}"


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        

# Como criar objeto Pessoa e Estudante (Instância)

pessoa1 = Pessoa('Mauro', 21)  
print(pessoa1.apresentar())
estudante = Estudante('Francis', 25, 'ADS')
print(estudante.apresentar())
estudante2 = Estudante('Jacqueline', 40, 'LC')
print(estudante2.apresentar())