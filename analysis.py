import math
import numpy as np
import matplotlib.pyplot as plt
import random

# Função teórica
def disponibilidade(n, k, p):
    total = 0
    for i in range(k, n+1):
        total += math.comb(n, i) * (p**i) * ((1-p)**(n-i))
    return total

# Simulação
def simulacao(n, k, p, repeticoes=100000):
    sucesso = 0

    for _ in range(repeticoes):
        ativos = 0

        for _ in range(n):
            if random.random() <= p:
                ativos += 1

        if ativos >= k:
            sucesso += 1

    return sucesso / repeticoes

# Parâmetros
p_vals = np.linspace(0, 1, 50)
n = 5
k_vals = [1, 3, 5]

# Gráfico teórico
plt.figure(1)
for k in k_vals:
    y = [disponibilidade(n, k, p) for p in p_vals]
    plt.plot(p_vals, y, label=f"k={k}")

plt.xlabel("p")
plt.ylabel("Disponibilidade")
plt.title("Disponibilidade Teórica")
plt.legend()

# Gráfico simulado
plt.figure(2)
for k in k_vals:
    y = [simulacao(n, k, p) for p in p_vals]
    plt.plot(p_vals, y, label=f"k={k}")

plt.xlabel("p")
plt.ylabel("Disponibilidade")
plt.title("Disponibilidade por Simulação")
plt.legend()

plt.show()
