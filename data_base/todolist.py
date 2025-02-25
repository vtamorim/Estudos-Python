import json

class Tdlist:
    def __init__(self):
        self.lista = []
        self.ToDo = ''

    def add(self):
        self.ToDo = input("Digite a tarefa: ")
        if self.ToDo in self.lista:
            print(f'Tarefa {self.ToDo} já existe')
        else:
            self.lista.append(self.ToDo)
            print(f'Tarefa {self.ToDo} adicionada com sucesso')

    def remover(self):
        remove_ToDo = input("Digite a tarefa que deseja remover: ")
        if remove_ToDo in self.lista:
            self.lista.remove(remove_ToDo)
            print(f'Tarefa {remove_ToDo} removida com sucesso')
        else:
            print(f'Tarefa {remove_ToDo} não existe')

    def exibir(self):
        print(f'Tarefas: {self.lista}')

    def edit(self):
        edit_ToDo = input("Digite a tarefa que deseja editar: ")
        if edit_ToDo in self.lista:
            new_ToDo = input("Digite a nova tarefa: ")
            self.lista.remove(edit_ToDo)
            self.lista.append(new_ToDo)
            print(f'Tarefa {edit_ToDo} editada com sucesso')
        else:
            print(f'Tarefa {edit_ToDo} não existe')

    def concluida(self):
        concluida_ToDo = input("Digite a tarefa que deseja marcar como concluída: ")
        if concluida_ToDo in self.lista:
            self.lista.remove(concluida_ToDo)
            print(f'Tarefa {concluida_ToDo} concluída com sucesso')
        else:
            print(f'Tarefa {concluida_ToDo} não existe')

    def filter(self, cate):
        filter_ToDo = input("Digite a categoria que deseja filtrar: ")
        if filter_ToDo in self.lista:
            print(f'Tarefas da categoria {cate}: {self.lista}')
        else:
            print(f'Tarefa {filter_ToDo} não existe')

    def save(self, lista, file):
        with open('todolist.json', 'w') as file:
            json.dump(lista, file)

    def vencimento(self):
        vencimento_ToDo = input("Digite a tarefa que deseja adicionar vencimento: ")
        if vencimento_ToDo in self.lista:
            vencimento = input("Digite a data de vencimento: ")
            print(f'Tarefa {vencimento_ToDo} adicionada com vencimento {vencimento}')
        else:
            print(f'Tarefa {vencimento_ToDo} não existe')

    def exit(self, verif):
        exit = input("Deseja sair? (s/n): ")
        if exit == 's':
            verif = False
        elif exit == 'n':
            verif = True
        if not verif:
            quit()
        else:
            return True

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

initt = Tdlist()
running = True
login = ''
users_data = load_users()

while True:
    print("Bem vindo ao ToDoList")
    if login == '':
        print("Já possui uma conta? (s/n)")
    cond = input("Digite sua escolha: ")
    if cond == 's':
        login = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        user_found = False
        for user in users_data["users"]:
            if user["login"] == login and user["password"] == password:
                print("Login realizado com sucesso")
                user_found = True
                break
        if user_found:
            break
        else:
            print("Usuário ou senha inválidos")
            quit("Tente Novamente")
    else:
        create_login = input("Crie seu nome de usuário: ")
        create_password = input("Crie sua senha: ")
        users_data["users"].append({"login": create_login, "password": create_password})
        save_users(users_data)
        print("Conta criada com sucesso")

while running:
    list_todolist = ['Adicionar', 'Remover', 'Exibir', 'Editar', 'Concluida', 'Filtrar', 'Salvar', 'Vencimento', 'Sair']
    for i in range(len(list_todolist)):
        print(f'[{i}] {list_todolist[i]}')
    escolha = int(input("Escolha uma opção: "))
    for j in range(9):
        if escolha == j:
            match j:
                case 0:
                    initt.add()
                case 1:
                    initt.remover()
                case 2:
                    initt.exibir()
                case 3:
                    initt.edit()
                case 4:
                    initt.concluida()
                case 5:
                    initt.filter()
                case 6:
                    initt.save()
                case 7:
                    initt.vencimento()
                case 8:
                    initt.exit()
                case _:
                    print("Opção inválida")












