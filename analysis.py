import math
import numpy as np
import matplotlib.pyplot as plt

def disponibilidade(n,k,p):
    total = 0
    for i in range(k,n+1):
        total += math.comb(n,i) * (p**i) * ((1-p)**(n-i))
    return total

p_vals = np.linspace(0,1,100)

n = 5
k_vals = [1,3,5]

for k in k_vals:
    y = [disponibilidade(n,k,p) for p in p_vals]
    plt.plot(p_vals,y,label=f"k={k}")

plt.xlabel("p (probabilidade servidor ativo)")
plt.ylabel("Disponibilidade")
plt.legend()

plt.show()
