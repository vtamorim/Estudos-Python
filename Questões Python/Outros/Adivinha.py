import random
aleatorio= random.randint(1,100)
tentativas= 0


while True:
    palpite=int(input("Manda um número: "))
    tentativas +=1
    if palpite>100:
        print(ValueError)
    elif palpite<0:
        print(ValueError)
    elif palpite>aleatorio:
        print("O número é menor que esse")
    elif palpite<aleatorio:
        print("O número é maior que esse")
    else:
        print(f"Parabéns, você acertou com o número de {tentativas} tentativas")

