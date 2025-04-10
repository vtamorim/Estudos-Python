import random



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
    def energia_vital(self,alma):
        if alma == 0:
            self.roubar = True
        elif alma == 1:
            self.sacri= True
        else:
            return False
    def atack_vital(self,golpe,inimigo):
        if self.roubar:
            inimigo.vida -= golpe
            self.vida += golpe
