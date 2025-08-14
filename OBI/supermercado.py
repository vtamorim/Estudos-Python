N = int(input())
quilos = 1000
lista = []

for _ in range(N):
    P, G = input().split()
    P = float(P)
    G = int(G)
    resposta = (P * quilos) / G
    lista.append(resposta)

print(f"{min(lista):.2f}")
