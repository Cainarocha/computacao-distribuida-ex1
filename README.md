# Exercícios 1.1 e 1.2 — Computação Distribuída

## Alunos

Nome: Cainã Rocha  
Matrícula: 2315038  

Nome: Davi Silveira  
Matrícula: 2310347 

Nome: Marcos André  
Matrícula: 2310371 

Nome: Pedro Vieira  
Matrícula: 2315708 

Universidade de Fortaleza — UNIFOR

---

## Exercício 1.1

## Conceito de Disponibilidade

Disponibilidade é a proporção do tempo em que um sistema permanece em funcionamento:

Disponibilidade = tempo em operação / (tempo em operação + tempo fora de operação)

Em sistemas distribuídos, a disponibilidade pode ser aumentada através da redundância, utilizando múltiplos servidores para o mesmo serviço. Assim, mesmo que alguns falhem, o sistema continua operando.

---

## Derivação da Fórmula
Queremos calcular a disponibilidade de um serviço replicado em múltiplos servidores.
O sistema funciona se pelo menos k servidores estiverem disponíveis.
Essa fórmula vem da distribuição binomial onde a disponibilidade é dada por.

$$A(n,k,p) = \sum_{i=k}^{n} \binom{n}{i} p^i (1-p)^{n-i}$$

### Definição dos Parâmetros:

* **$n$**: Número de servidores.
* **$k$**: Mínimo de servidores ativos.
* **$p$**: Probabilidade de um servidor estar disponível.
* **$i$**: Variável de iteração representando o número de servidores ativos em cada cenário.
* **$\binom{n}{i}$**: Coeficiente binomial ($\frac{n!}{i!(n-i)!}$), que representa as combinações possíveis de servidores ativos.

Casos extremos:

* $k = 1$

* $A = 1 - (1-p)^n$

* $k = n$

* $A = p^n$

---

## Exercício 1.2

Foram utilizados dois métodos:

1. Cálculo analítico utilizando a fórmula binomial
2. Simulação estocástica com números aleatórios

Na simulação:

- cada servidor gera um número $n$, onde $n \in (0, 1)$
- se $n \leq p$ → servidor disponível
- contamos quantos servidores estão ativos
- se pelo menos $k$ estiverem ativos → serviço disponível

A frequência experimental converge para o valor teórico da fórmula.

---

## Visualização

O script [analysis.py](analysis.py) gera um gráfico da disponibilidade em função de p para diferentes valores de k.
Os gráficos mostram a relação entre a probabilidade p de um servidor estar disponível e a disponibilidade total do sistema para diferentes valores de k.

| ![Gráfico de disponibilidade](disp_teorica.png) | ![Gráfico de disponibilidade](disp_simulacao.png) |