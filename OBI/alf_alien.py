K,N = list(map(int,input().split()))
condição = "N"
mano = 0
gabarito = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/#!")
Alf_K = input()
Alf_N = input()
if len(Alf_K) != K:
    raise ValueError
elif len(Alf_N) != N:
    raise ValueError                                                                                                                                                                                            
elif not 1<=K<=68:
    raise ValueError
elif not 1<=N<=1000:
    raise ValueError

for i in list(Alf_K):
    if i not in gabarito:
        raise ValueError
    elif Alf_K.count(i) > 1:
        raise ValueError
    else:
        continue
for i in list(Alf_N):
    if i not in Alf_K:
        print(condição)
        break
    else:
        mano += 1
        if mano == len(Alf_N):
            print("S")
    