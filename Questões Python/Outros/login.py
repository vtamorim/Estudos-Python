import json
import os

class Nickname:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def load_table(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_table(file_path, table):
        with open(file_path, 'w') as file:
            json.dump(table, file, indent=4)

    @staticmethod
    def inserir(name, password, table, file_path):
        if name in table:
            return "Error: Nickname already exists."
        table[name] = password
        Nickname.save_table(file_path, table)
        return "Nickname inserted successfully."

    @staticmethod
    def delet(name, table, file_path):
        if name in table:
            del table[name]
            Nickname.save_table(file_path, table)
            return "Nickname deleted successfully."
        return "Error: Nickname not found."

    @staticmethod
    def search(name, table):
        return name in table

    @staticmethod
    def update(name, table, file_path):
        if name in table:
            new_name = input("New nickname: ")
            if new_name in table:
                return "Error: New nickname already exists."
            table[new_name] = table.pop(name)
            Nickname.save_table(file_path, table)
            return "Nickname updated successfully."
        return "Error: Nickname not found."

    @staticmethod
    def view_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(json.dumps(data, indent=4)) 
        else:
            print("Arquivo JSON não encontrado.")

def interaction(table, file_path):
    options = ['Insert', 'Delete', 'Search', 'Update', 'View JSON']
    for index, element in enumerate(options):
        print(f"[{index}] {element}")
    try:
        chosen = int(input("Choose an option: "))
        if chosen not in range(len(options)):
            print("Invalid option.")
            return table
    except ValueError:
        print("Invalid input. Please enter a number.")
        return table

    nick = input("Nickname: ")
    if chosen != 2:  
        password = input("Password: ")

    if chosen == 0:
        print(Nickname.inserir(nick, password, table, file_path))
    elif chosen == 1:
        print(Nickname.delet(nick, table, file_path))
    elif chosen == 2:
        exists = Nickname.search(nick, table)
        print("Nickname found." if exists else "Nickname not found.")
    elif chosen == 3:
        print(Nickname.update(nick, table, file_path))
    elif chosen == 4: 
        Nickname.view_json(file_path)

    return table


def main():
    file_path = 'table.json'
    table = Nickname.load_table(file_path)

    while True:
        interaction(table, file_path)


if __name__ == '__main__':
    main()
