import random



class Personagem():
    def __init__(self, nome):
        self.vida = 100
        self.nome = nome
        self.alive = True
        self.ataque = False
        self.defesa = False
        self.ataques = []
        self.defesas = []
    def get_ataques(self):
        return ''.join(self.ataques)
    def get_defesas(self):
        return ''.join(self.defesas)
    def atacar(self,inimigo,golpe):
        if inimigo.alive:
            inimigo.vida -= golpe
            if inimigo.vida <=0:
                inimigo.vida = 0
                inimigo.alive = False
                print(f"{self.nome} Ganhou!")
            
    def defender(self,inimigo,golpe):
        if self.alive: 
            self.vida -= golpe
            if self.vida <=0:
                self.vida = 0
                self.alive = False
                print(f"{inimigo.nome} Ganhou!")



class Guerreiro(Personagem):
    potencializador = 1.5

    def __init__(self, nome):
        super().__init__(nome)
        self.vida_extra = 10
        self.vida = self.vida + self.vida_extra
        self.ataques =  ["Golpe Poderoso", "Ataque Giratório", "Corte Feroz"]
        self.defesas = ["Bloqueio de Escudo", "Postura Defensiva", "Contra-ataque"]
    def get_ataques(self):
        return '|\n|'.join(self.ataques)
    def get_defesas(self):
        return '|\n|'.join(self.defesas)

    def ataque_especial(self, inimigo, golpe):
        golpe = golpe * self.potencializador
        if inimigo.alive:
            inimigo.vida -= golpe
            if inimigo.vida <=0:
                inimigo.vida = 0
                inimigo.alive = False
                print(f"{self.nome} Ganhou!")
        if self.alive:
            self.vida -= 0.1 * self.vida    
            if self.vida <= 0:
                self.vida = 0 
                self.alive = False
        elif not self.alive:
            print("Infelizmente ele tentou :(  )")


class Mago(Personagem):
    def __init__(self, nome,requerer):
        super().__init__(nome)
        self.mana = 100
        self.podermul = 1.2
        self.requerer = requerer
        self.ataques = ["Bola de Fogo", "Meteoro das Trevas", "Queda do Trovão"]
        self.defesas = ["Escudo Mágico", "Barreira Arcana", "Reflexão Mágica"]
    def get_ataques(self):
        return '|\n|'.join(self.ataques)
    def get_defesas(self):
        return '|\n|'.join(self.defesas)
    def cond_mana(self):

        if self.mana == 0:
            self.mana = 50
        if self.mana - self.requerer < 0:
            print("Sem mana suficiente para utilizar a magia")
            return False
        if self.mana>= self.requerer:
            self.mana -= self.requerer
            return True

    def lancar_magia(self,golpe,inimigo):
        if self.cond_mana():
            golpe = golpe * self.podermul
            inimigo.vida -= golpe

            if inimigo.vida <= 0:
                   inimigo.vida = 0
                   inimigo.alive = False
                   return f"{self.nome} Ganhou!"
            return f"{self.nome} Aplicou um golpe no inimigo, que está com: {inimigo.vida} de vida"
        
class Arqueiro(Personagem):
    def __init__(self, nome, esquiva):
        super().__init__(nome)
        self.esquiva = False
        self.atack_duplo = False
        self.vida -= self.vida * 0.08
        self.ataques = ["Tiro Preciso", "Disparo Rápido", "Flecha Explosiva"]
        self.defesas = ["Esquiva Ágil", "Reflexo Rápido", "Fuga do Arco"]
    def get_ataques(self):
        return '|\n|'.join(self.ataques)
    def get_defesas(self):
        return '|\n|'.join(self.defesas)
    def esquivar(self):
        self.esquiva = random.randint(1,8) == 1
        return self.esquiva
    def duplo_atack(self):
        self.atack_duplo = random.randint(1,16) == 1
        return self.atack_duplo
    


class Necromante(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.roubar = False
        self.sacri = False
        self.ataques = ["Toque da Morte", "Ritual Sombrio", "Chama da Alma"]
        self.defesas = ["Escudo de Ossos", "Barreira Sombria", "Aura de Morte"]
    def get_ataques(self):
        return '|\n|'.join(self.ataques)
    def get_defesas(self):
        return '|\n|'.join(self.defesas)
    def energia_vital(self,alma):
        if alma == "roubar":
            self.roubar = True
        elif alma == "sacrificar":
            self.sacri= True
        else:
            return False
    def atack_vital(self,golpe,inimigo):
        if self.roubar and inimigo.alive:
            inimigo.vida -= golpe
            if inimigo.vida <= 0:
                inimigo.vida = 0
            self.vida += golpe//2.5
            if self.vida > 100:
                self.vida = 100


class GerenciadorDeTurnos:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo
        self.turno = 1

    def executar_turno(self):
        print(f"\n--- Turno {self.turno} ---")
        
        if self.jogador.alive:
            print(f"{self.jogador.nome} está atacando!")
            golpe = random.randint(10, 20)
            escolha_ataque = input(f"Escolha um ataque:\n|{self.jogador.get_ataques()}|\n").strip().lower()
            print(f"Você escolheu: {escolha_ataque}")
            try:
                golpe = self.jogador.ataques.index(escolha_ataque) + golpe
            except ValueError:
                print("Ataque inválido! Usando golpe padrão.")
                golpe = random.randint(10, 20)
            if self.jogador.duplo_atack():
                print(f"{self.jogador.nome} executou um ataque duplo!")
                golpe *= 2
            if self.jogador.esquivar():
                print(f"{self.jogador.nome} conseguiu esquivar do ataque!")
                return True
            if isinstance(self.jogador, Mago):
                mana_requerida = 20
                if self.jogador.cond_mana():
                    resultado = self.jogador.lancar_magia(golpe, self.inimigo)
                    print(resultado)
                    if not self.inimigo.alive:
                        return False
                else:
                    print("Mana insuficiente para lançar magia.")
                    return True
            elif isinstance(self.jogador, Necromante):
                alma = input("Você quer roubar ou sacrificar a energia vital do inimigo? (roubar/sacrificar): ").strip().lower()
                self.jogador.energia_vital(alma)
                if alma == "roubar":
                    self.jogador.atack_vital(golpe, self.inimigo)
                    print(f"{self.jogador.nome} roubou energia vital! Vida atual: {self.jogador.vida}")
                elif alma == "sacrificar":
                    self.jogador.atack_vital(golpe, self.inimigo)
                    print(f"{self.jogador.nome} sacrificou energia vital! Vida atual: {self.jogador.vida}")
            else:
                golpe += random.randint(0, 5)
            self.jogador.atacar(self.inimigo, golpe)
            print(f"{self.inimigo.nome} tem {self.inimigo.vida} de vida restante.")
            if not self.inimigo.alive:
                print(f"{self.jogador.nome} venceu!")
                return False

        if self.inimigo.alive:
            print(f"{self.inimigo.nome} está atacando!")
            golpe = random.randint(5, 15)
            self.inimigo.atacar(self.jogador, golpe)
            print(f"{self.jogador.nome} tem {self.jogador.vida} de vida restante.")
            if not self.jogador.alive:
                print(f"{self.inimigo.nome} venceu!")
                return False

        self.turno += 1
        return True

    def iniciar_jogo(self):
        while self.jogador.alive and self.inimigo.alive:
            if not self.executar_turno():
                break


if __name__ == "__main__":
    

    print("Bem-vindo ao jogo de luta!")

    escolha = input("Escolha seu personagem (Guerreiro, Mago, Arqueiro, Necromante): ").strip().lower()
    nome = input("Digite o nome do seu personagem: ").strip()
    personagem_classes = {
        "guerreiro": Guerreiro(nome),
        "mago": Mago(nome, 20),
        "arqueiro": Arqueiro(nome, 0),
        "necromante": Necromante(nome)
    }
    if escolha not in personagem_classes:
        print("Escolha inválida!")
        exit()
    else:
        jogador = personagem_classes[escolha]
        print(f"Você escolheu: {jogador.nome} ({escolha.capitalize()})")
        print(f"Vida inicial: {jogador.vida}")
        print(f"Mana inicial: {getattr(jogador, 'mana', 'N/A')}")
        GerenciadorDeTurnos(jogador, Guerreiro("Inimigo")).iniciar_jogo()
        print("Fim do jogo!")
