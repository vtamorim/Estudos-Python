import tkinter as tk
from tkinter import messagebox


class SistemaBancario:
    def __init__(self):
        self.saldo = 0

    def saque(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente!"
        else:
            self.saldo -= valor
            return "Saque realizado com sucesso!"
    def saldo(self):
        return self.saldo
    def deposito(self, valor):
        self.saldo += valor
        return "Depósito realizado com sucesso!"
    def transferencia(self, valor, conta_destino):
        if valor > self.saldo:
            return "Saldo insuficiente!"
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            return "Transferência realizada com sucesso!"



def saque():
    messagebox.showinfo("Saque", "Você escolheu a opção Saque!")
    root.withdraw()
    root2 = tk.Tk()
    root2.title("Saque")
    root2.geometry("300x250")
    tk.Label(root2, text="Digite o valor do saque:").pack(pady=10)
    valor = tk.Entry(root2)
    valor.pack(pady=5) 
    btn_saque = tk.Button(root2, text="Sacar", width=20, fg="white", bg="green")
    btn_saque.pack(pady=10)
    root2.mainloop()


def deposito():
    messagebox.showinfo("Depósito", "Você escolheu a opção Depósito!")

def transferencia():
    messagebox.showinfo("Transferência", "Você escolheu a opção Transferência!")
def sair():
    root.quit()

# Criando a janela principal
root = tk.Tk()
root.title("Menu Interativo")
root.geometry("300x250")

# Criando os botões
tk.Label(root, text="Sistema Bancário", font=("Arial", 12)).pack(pady=10)

btn1 = tk.Button(root, text="Saque", command=saque, width=20)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Depósito", command=deposito, width=20)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Transferência", command=transferencia, width=20)
btn3.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", command=sair, width=20, fg="white", bg="red")
btn_sair.pack(pady=10)

# Executando a janela
root.mainloop()
