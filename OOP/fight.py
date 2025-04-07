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
    def __init__(self, nome):
        super().__init__(nome)
        self.vida_extra = 10
        self.vida = self.vida + self.vida_extra