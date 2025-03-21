import random 

palavras = ["Abacaxi", "Sol", "Dinossauro", "Biblioteca", "Computador", "Magia", "Horizonte", "Planeta", "Caverna", "Relâmpago", "Sorriso", "Aventuras", "Borboleta", "Dragão", "Montanha", "Oceano", "Estrela", "Telefone", "Chocolate", "Arco-íris"]
aleatorio =  random.choice(palavras)
aleatorio = list(aleatorio)
acertos = str(len(aleatorio)*'')
running = True
qnt_ac= 0 
while running:

    if qnt_ac >= 1:
        print(' '.join(acertos))
    print(len(aleatorio)*"_ ")
    escolha = input("escolha ae : ")
    for i in aleatorio:
        if escolha in aleatorio:
            if escolha in acertos:
                print("Essa letra já foi escolhida")
                break
            else:
                acertos.append(escolha)
                qnt_ac += 1
                break
        else:
            continue
