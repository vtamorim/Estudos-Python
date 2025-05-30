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

def append_json(filepath, data):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lista = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []
    lista.append(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

class UI:
    def __init__(self):
        self.__codition_person = True
        self.__codition_work = True
        self.__codition_res = True
        self.__codition_city = True
        self.__codition_geral = True

    def ui_person(self):
        while self.__codition_person:
            entrada = input("Quer ler '-' ")
            if entrada == "s":
                with open("OOP/Arquivos json/pessoas.json","r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)


                for jombson in dados:
                    print(jombson["nome"])
            nome = input("Seu Nome: ")
            idade = int(input("Idade: "))
            ocupacao = input("Ocupação : ")
            genero = input("Gênero: ")
            dados_person = {
                "nome" : nome,
                "idade" : idade,
                "ocupacao" : ocupacao,
                "genero" : genero
            }
            append_json("OOP/Arquivos json/pessoas.json", dados_person)
            metodos_person = ["Nome","Idade","Ocupação","Gênero"]
            for i, metodo in enumerate(metodos_person):
                print(f"[{i}] {metodo}")
            escolha = input("Escolha um campo para exibir: ")
            pessoa = Pessoa(nome, idade, ocupacao, genero, "Sem CPF registrado")
            match escolha:
                case "Nome"|"0":
                    print(pessoa.get_nome())
                case "Idade"|"1":
                    print(pessoa.get_idade())
                case "Ocupação"|"2":
                    print(pessoa.get_ocupacao())
                case "Gênero"|"3":
                    print(pessoa.get_genero())

            sair = input("Quer sair do cadastro de pessoa? S/N: ").strip().upper()
            if sair == "S":
                self.__codition_person = False

    def ui_work(self):
        while self.__codition_work:
            work_name = input("Nome da Empresa que Trabalha: ")
            work_type = input("Tipo de Trabalho: ")
            work_empresa = input(f"Endereço do {work_name}: ")
            dados_work = {
                "nome" : work_name,
                "tipo" : work_type,
                "endereço" : work_empresa
            }
            append_json("OOP/Arquivos json/trabalhos.json", dados_work)
            metodos_work = ["Nome","Tipo","Endereço"]
            for i, metodo in enumerate(metodos_work):
                print(f"[{i}] {metodo}")
            escolha = input("Escolha um campo para exibir: ")
            work = Empresa(work_name, work_type, work_empresa, "Sem Funcionários", "Sem Vagas")
            match escolha:
                case "Nome"|"0":
                    print(work.get_nome())
                case "Tipo"|"1":
                    print(work.get_tipo())
                case "Endereço"|"2":
                    print(work.get_endereco())

            sair = input("Quer sair do cadastro de empresa? S/N: ").strip().upper()
            if sair == "S":
                self.__codition_work = False

    def ui_home(self):
        while self.__codition_res:
            res_endereco = input("Endereço da Residência: ")
            res_type = input("Tipo de Residência: ")
            res_morador = input("Morador dessa Residência: ")
            dados_residencia = {
                "endereco" : res_endereco,
                "type" : res_type,
                "morador" : res_morador
            }
            append_json("OOP/Arquivos json/residencias.json", dados_residencia)
            metodos_home = ["Morador","Tipo","Endereço"]
            for i, metodo in enumerate(metodos_home):
                print(f"[{i}] {metodo}")
            escolha = input("Escolha um campo para exibir: ")
            home = Residencia(res_endereco, res_morador, res_type)
            match escolha:
                case "Morador"|"0":
                    print(home.get_morador())
                case "Tipo"|"1":
                    print(home.get_tipo())
                case "Endereço"|"2":
                    print(home.get_endereco())

            sair = input("Quer sair do cadastro de residência? S/N: ").strip().upper()
            if sair == "S":
                self.__codition_res = False

    def ui_city(self):
        while self.__codition_city:
            city_name = input("Nome da Cidade: ")
            city_pop = int(input("População da Cidade: "))
            city_pref = input("Prefeito da Cidade: ")
            dados_city =  {
                "nome" : city_name,
                "populacao" : city_pop,
                "prefeito" : city_pref
            }
            append_json("OOP/Arquivos json/cidade.json", dados_city)
            metodos_city = ["Nome","População","Prefeito"]
            for i, metodo in enumerate(metodos_city):
                print(f"[{i}] {metodo}")
            escolha = input("Escolha um campo para exibir: ")
            city = Cidade(city_name, city_pop, city_pref)
            match escolha:
                case "Nome"|"0":
                    print(city.get_nome())
                case "População"|"1":
                    print(city.get_populacao())
                case "Prefeito"|"2":
                    print(city.get_prefeitura())

            sair = input("Quer sair do cadastro de cidade? S/N: ").strip().upper()
            if sair == "S":
                self.__codition_city = False

    def ui_geral(self):
        serv_cad = ["Cidade","Pessoa","Residencia","Empresa"]
        while self.__codition_geral:
            for i, serv in enumerate(serv_cad):
                print(f"[{i}] {serv}")
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "Cidade"|"0":
                    self.ui_city()
                case "Residencia"|"2":
                    self.ui_home()
                case "Pessoa"|"1":
                    self.ui_person()
                case "Empresa"|"3":
                    self.ui_work()
            sair = input("Quer sair do sistema geral? S/N: ").strip().upper()
            if sair == "S":
                self.__codition_geral = False
            else:
                continue 
initt = UI()
initt.ui_geral()