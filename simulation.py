import random
import math

def simulacao(n,k,p,rodadas=10000):

    sucesso = 0

    for _ in range(rodadas):

        ativos = 0

        for _ in range(n):
            if random.random() <= p:
                ativos += 1

        if ativos >= k:
            sucesso += 1

    return sucesso/rodadas


def formula(n,k,p):

    total = 0
    for i in range(k,n+1):
        total += math.comb(n,i)*(p**i)*((1-p)**(n-i))

    return total


n = 5
k = 3
p = 0.9

print("Formula:",formula(n,k,p))
print("Simulação:",simulacao(n,k,p))
