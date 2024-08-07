class Usuario():
    # Construtor
    def __init__(self):
        self.__numeroUsuario = ""
        
    # Método para alterar o comportamento da classe ou objeto
    def get_numeroUsuario(self):
        return self.__numeroUsuario
    
    # Método para recuperar o comportamento da classe
    def set_numeroUsuario(self, v_numeroUsuario):
        self.__numeroUsuario = v_numeroUsuario
    
# Instância
usuario1 = Usuario()
usuario1.set_numeroUsuario('001')
print(usuario1.get_numeroUsuario())

usuario2 = Usuario()
usuario2.set_numeroUsuario('002')
print(usuario2.get_numeroUsuario())

usuario3 = Usuario()
usuario3.set_numeroUsuario('003')
print(usuario3.get_numeroUsuario())


#Classe secundaria ou subclasse:
class Administrador(Usuario):
    def __init__(self):
        return "Administrador"


administrador = Usuario("Andre")
administrador.set_numeroUsuario('002')
administrador.set_numeroUsuario('Softex')
print(administrador.get_numeroUsuario)