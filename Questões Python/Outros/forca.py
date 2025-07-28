import random

palavras = [
    "computador", "programador", "python", "java", "interface",
    "algoritmo", "função", "variavel", "objeto", "classe",
    "teclado", "monitor", "internet", "sistema", "software",
    "hardware", "rede", "jogo", "código", "aplicativo"
]
aleatorio = random.choice(palavras)
mano = ["_"] * len(aleatorio)
print(" ".join(mano))
print("Dica: TI")

while "_" in mano:
    escolha = input("Escolha uma letra:  ")
    for idx, letra in enumerate(aleatorio):
        if letra == escolha or letra.upper() == escolha:
            mano[idx] = escolha
    print(" ".join(mano))

print("Parabéns, você acertou!")