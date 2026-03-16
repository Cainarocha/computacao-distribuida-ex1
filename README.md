# Exercícios 1.1 e 1.2 — Computação Distribuída

## Exercício 1.1

Queremos calcular a disponibilidade de um serviço replicado em múltiplos servidores.

Parâmetros:

n = número de servidores  
k = mínimo de servidores ativos  
p = probabilidade de um servidor estar disponível  

O sistema funciona se pelo menos k servidores estiverem disponíveis.

A disponibilidade é dada por:

A(n,k,p) = Σ(i=k..n) C(n,i) p^i (1-p)^(n-i)

Essa fórmula vem da distribuição binomial.

Casos extremos:

k = 1

A = 1 - (1-p)^n

k = n

A = p^n

---

## Exercício 1.2

Foram utilizados dois métodos:

1. Cálculo analítico utilizando a fórmula binomial
2. Simulação estocástica com números aleatórios

Na simulação:

- cada servidor gera um número aleatório
- se o número ≤ p → servidor disponível
- contamos quantos servidores estão ativos
- se pelo menos k estiverem ativos → serviço disponível

A frequência experimental converge para o valor teórico da fórmula.

---

## Visualização

O script analysis.py gera gráficos da disponibilidade em função de p para diferentes valores de k.
