class Cidade:
    def __init__(self, nome, populacao, prefeitura):
        self.__nome = nome
        self.__populacao = populacao
        self.__prefeitura = prefeitura
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_prefeitura(self):
        return self.__prefeitura

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

class Residencia:
    def __init__(self, endereco, morador, tipo):
        self.__endereco = endereco
        self.__morador = morador
        self.__tipo = tipo
    def get_endereco(self):
        return self.__endereco
    def get_morador(self):
        return self.__morador
    def get_tipo(self):
        return self.__tipo
    
class Empresa:
    def __init__(self, nome, tipo, endereco, funcionarios, vagas):
        self.__nome = nome
        self.__tipo = tipo
        self.__endereco = endereco
        self.__funcionarios = funcionarios
        self.vagas = vagas
    def get_nome(self):
        return self.__nome
    def get_endereco(self):
        return self.__endereco
    def get_funcionario(self):
        return self.__funcionarios
    def get_tipo(self):
        return self.__tipo
    def get_vagas(self):
        return self.vagas


        