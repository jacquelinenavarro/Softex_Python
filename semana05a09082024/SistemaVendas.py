#Privado

#Classe primária ou superclasse
class Usuario():
    #Construtor
    def __init__(self, numerousuario):
        self.__numeroUsuario = numerousuario

    #Método alterar o comportamento da classe ou objeto
    def get_numeroUsario(self):
        return self.__numeroUsuario
   
    #Método para recuperar o comportamento da classe
    def set_numeroUsuaio(self, numeroUsuario):
        self.__numeroUsuario = numeroUsuario
   
#Classe secundária ou subclasse
class Administrador(Usuario):

    def __init__(self, numeroUsuario, n):
        super().__init__(numeroUsuario)
        self.__nomeAdm = n
   
    def get_nomeAdministrador(self):
        return self.__nomeAdm
    #Atribuir
    def set_nomeAdministrador(self, n):
        self.__nomeAdm  = n


administrador = Administrador("002","Paulo")
#administrador.set_numeroUsuaio('002')
#administrador.set_nomeAdministrador('Softex')

print(administrador.get_numeroUsario())
print(administrador.get_nomeAdministrador())