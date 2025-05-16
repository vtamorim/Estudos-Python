class Pessoa:
    def __init__(self,nome,idade,ocupacao,genero,cpf):
        self.__nome = nome
        self.__idade = idade
        self.__ocupacao = ocupacao
        self.__genero = genero
        self.__cpf = cpf
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_idade(self):
        return self.__idade
    
    def get_ocupacao(self):
        return self.__ocupacao
    
    def get_genero(self):
        return self.__genero



        