P1 = int(input())
P2 = int(input())
P3 = int(input())
P4 = int(input())
P5 = int(input())
PI = [P1,P2,P3,P4,P5]
for i in PI:
    if not 1 <= i <= 100:
        raise ValueError("ERRO")
maior = max(PI)
quantidade_trofeu = PI.count(maior)

restantes = [x for x in PI if x != maior]

if restantes:
    segundo_maior = max(restantes)
    quantidade_placa = restantes.count(segundo_maior)
else:
    quantidade_placa = 0
print(quantidade_trofeu , " " , quantidade_placa)