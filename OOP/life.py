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
        self.__codition_person = True
        self.__codition_work = True
        self.__codition_res = True
        self.__codition_city = True
        self.__codition_geral = True
    def ui_person(self):
        while self.__codition_person:
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
            self.metodos_person = ["Nome","Idade","Ocupação","Gênero"]
            for i in range(len(self.metodos_person)):
                print("[", i ,"]", self.metodos_person[i])            
            
            escolha = input()
            pessoa = Pessoa(self.nome,self.idade,self.ocupacao,self.genero,"Sem CPF registrado")
            match escolha:
                case "Nome"|"0":
                    pessoa.get_nome()
                case "Idade"|"1":
                    pessoa.get_idade()
                case "Ocupação"|"2":
                    pessoa.get_ocupacao()
                case "Gênero"|"3":
                    pessoa.get_genero

    def ui_work(self):
        while self.__codition_work:
            self.work_name = input("Nome da Empresa que Trabalha: ")
            self.work_type = input("Tipo de Trabalho: ")
            self.work_empresa = input(f"Endereço do {self.work_name}: ")
            dados_work = {
                "nome" : self.work_name,
                "tipo" : self.work_type,
                "endereço" : self.work_empresa
            }
            
            with open("OOP/Arquivos json/trabalhos.json", "w" , encoding="utf-8") as arquivo:
                json.dump(dados_work, arquivo,ensure_ascii=False, indent=4)
            self.metodos_work = ["Nome","Tipo","Endereço"]
            for i in range(len(self.metodos_work)):
                print("[", i ,"]", self.metodos_work[i])
            escolha = input()
            work = Empresa(self.work_name,self.work_type,self.work_empresa,"Sem Funcionários","Sem Vagas")
            match escolha:
                case "Nome"|"0":
                    work.get_nome()
                case "Tipo"|"1":
                    work.get_tipo()
                case "Endereço"|"2":
                    work.get_endereco()


    def ui_home(self):
        while self.__codition_res:
            self.res_endereco = input("Endereço da Residência: ")
            self.res_type = input("Tipo de Residência: ")
            self.res_morador = input("Morador dessa Residência: ")
            dados_residencia = {
                "endereco" : self.res_endereco,
                "type" : self.res_type,
                "morador" : self.res_morador

            }

            with open("OOP/Arquivos json/residencias.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_residencia, arquivo, ensure_ascii=False, indent=4)
                
            self.metodos_home = ["Morador","Tipo","Endereço"]
            for i in range(len(self.metodos_home)):
                print("[", i ,"]", self.metodos_home[i])            
            
            escolha = input()
            home = Residencia(self.res_endereco,self.res_morador,self.res_type,"Sem Funcionários","Sem Vagas")
            match escolha:
                case "Morador"|"0":
                    home.get_morador()
                case "Tipo"|"1":
                    home.get_tipo()
                case "Endereço"|"2":
                    home.get_endereco()
    def ui_city(self):
        while self.__codition_city:
            self.city_name = input("Nome da Cidade: ")
            self.city_pop = int(input("População da Cidade: "))
            self.city_pref = input("Prefeito da Cidade: ")
            dados_city =  {
                "nome" : self.city_name,
                "populacao" : self.city_pop,
                "prefeito" : self.city_pref
            }
            with open("OOP/Arquivos json/cidade.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_city, arquivo, ensure_ascii=False, indent=4)
            self.metodos_city = ["Nome","População","Prefeito"]
            for i in range(len(self.metodos_city)):
                print("[", i ,"]", self.metodos_city[i])            
            
            escolha = input()
            city = Cidade(self.city_name,self.city_pop,self.city_pref)
            match escolha:
                case "Nome"|"0":
                    city.get_nome()
                case "População"|"1":
                    city.get_populacao()
                case "Prefeito"|"2":
                    city.get_prefeitura()
    def ui_geral(self):
        self.serv_cad = ["Cidade","Pessoa","Residencia","Empresa"]
        while self.__codition_geral:
            for i in range(len(self.serv_cad)):
                print("[", i ,"]", self.serv_cad[i])
            escolha = input()
            init = UI()
            match escolha:
                case "Cidade"|"0":
                    init.ui_city()
                case "Residencia"|"2":
                    init.ui_home()
                case "Pessoa"|"1":
                    init.ui_person()
                case "Empresa"|"3":
                    init.ui_work()
            sair = input("Quer sair? S/N")
            if sair == "S":
                self.__codition_geral == False
            else:
                continue 
initt = UI()
initt.ui_geral()