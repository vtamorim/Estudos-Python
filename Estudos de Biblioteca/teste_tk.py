import tkinter as tk



window = tk.Tk()
window.title("Só testando '-' ")
window.geometry("1200x720")

def show_window():
    name = entrada.get()
    texto["text"] = f"Eae {name}"

entrada = tk.Entry(window)
entrada.pack(padx=20)

botao = tk.Button(window, text = "Cleberson tá ativo", command=show_window)
botao.pack()


texto = tk.Label(window, text="")
texto.pack(pady=10)

window.mainloop()

