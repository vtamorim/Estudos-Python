import random
import json
import math

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

class UI:
    def __init__(self):
        self.codition_person = True
        self.codition_work = True
    def ui_person(self):
        while self.codition_person:
            self.nome = input("Seu Nome: ")
            self.idade = int(input("Idade: "))
            self.ocupacao = input("Ocupação : ")
            self.genero = input("Gênero: ")
            dados_person = {
                "nome" : self.nome,
                "idade" : self.idade,
                "ocupacao" : self.ocupacao,
                "genero" : self.genero
            } 
            with open("OOP/Arquivos json/pessoas.json", "w" , encoding="utf-8") as arquivo:
                json.dump(dados_person,arquivo,ensure_ascii=False,indent=4)
    def ui_work(self):
        while self.codition_work:
            self.work_name = input("Nome da Empresa que Trabalha: ")
            self.work_type = input("Tipo de Trabalho: ")
            self.work_carg = input(f"Cargo/Ocupação no {self.work_name}: ")
            dados_work = {
                "nome" : self.work_name,
                "type" : self.work_type,
                "cargo" : self.work_carg
            }
            
            with open("OOP/Arquivos json/trabalhos.json", "w" , encoding="utf-8") as arquivo:
                json.dump(dados_work, arquivo,ensure_ascii=False, indent=4)
initt = UI()
initt.ui_work()