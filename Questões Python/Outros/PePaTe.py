import random


def jogo():
        opçoes=["pedra","tesoura","papel"]
        jogador=input("Escolhe pedra, papel ou tesoura: ").lower()
        computador= random.choice(opçoes)
        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {computador}")

        while True:
            if jogador == "sair":
                print("Saindo")
                quit()
            elif jogador not in opçoes:
                print(ValueError)
                continue
            elif jogador==computador:
                print("Empate!!!")
                break
            elif jogador=="pedra" and computador=="tesoura"or  \
    jogador=="papel" and computador=="pedra" or \
    jogador=="tesoura" and computador=="papel":
                print("Você Ganhou!! Parabéns")
            
            else:
                print("Você perdeu!! Tente Novamente")
                break
        
jogo()