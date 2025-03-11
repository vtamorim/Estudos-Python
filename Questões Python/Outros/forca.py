import random 

palavras = ["Abacaxi", "Sol", "Dinossauro", "Biblioteca", "Computador", "Magia", "Horizonte", "Planeta", "Caverna", "Relâmpago", "Sorriso", "Aventuras", "Borboleta", "Dragão", "Montanha", "Oceano", "Estrela", "Telefone", "Chocolate", "Arco-íris"]
aleatorio =  random.choice(palavras)
aleatorio = list(aleatorio)
acertos = []
running = True

while running:
    
    print(len(aleatorio)*"_ ")
    escolha = input("escolha ae : ")
    for i in aleatorio:
        if escolha in aleatorio:
            print("deu bom")
            acertos.append(escolha)
            break
        else:
            

            
        