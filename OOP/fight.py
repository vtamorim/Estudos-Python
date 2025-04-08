class Personagem():
    def __init__(self, nome):
        self.vida = 100
        self.nome = nome
        self.alive = True
        self.ataque = False
        self.defesa = False
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
    def cond_mana(self):

        if self.mana == 0:
            self.mana = 50
        if self.mana - self.requerer < 0:
            print("Sem mana suficiente para utilizar a magia")
        if self.mana - self.requerer > 0 :
            self.mana -= 10