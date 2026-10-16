#!/usr/bin/env python3
"""Gera casos de teste para o exercicio de caixas de esfirras.

Uso: python3 marbles_generator.py > entrada.txt
A entrada gerada contem T=1000 casos, incluindo casos construidos e aleatorios.
"""
import random

RNG = random.Random(999)
MAX_N = 2_000_000_000
MAX_VALUE = 1_999_999_999
NUM_CASES = 1000


def add_case(cases, N, c1, n1, c2, n2):
    if 1 <= N <= MAX_N and all(1 <= value <= MAX_VALUE for value in (c1, n1, c2, n2)):
        cases.append((N, c1, n1, c2, n2))


def build_cases():
    cases = []

    # # Exemplos e casos pequenos que permitem conferir as respostas manualmente.
    # add_case(cases, 43, 1, 3, 2, 4)       # Solucao otima: 13 1
    # add_case(cases, 40, 5, 9, 5, 12)      # Sem solucao
    # add_case(cases, 12, 2, 3, 3, 4)       # Duas formas de empacotar
    # add_case(cases, 12, 3, 3, 2, 4)       # Favorece a caixa 2
    # add_case(cases, 12, 2, 3, 4, 6)       # Mesmo total, caixas de tamanhos relacionados
    # add_case(cases, 7, 1, 4, 1, 6)        # Sem solucao
    # add_case(cases, 1, 1, 1, 2, 2)         # Apenas caixa 1
    # add_case(cases, 2, 10, 1, 1, 2)       # Apenas caixa 2, apesar de preco diferente
    # add_case(cases, 24, 5, 6, 7, 8)       # Solucoes com custos distintos
    # add_case(cases, 24, 7, 6, 5, 8)       # Troca a vantagem de custo
    # add_case(cases, 100, 5, 10, 5, 20)    # Capacidade divisivel
    # add_case(cases, 100, 5, 20, 5, 10)    # Ordem dos tipos invertida
    # add_case(cases, MAX_N, 1, 1, 1, 2)    # N grande, caixas pequenas
    # add_case(cases, MAX_N, MAX_VALUE, MAX_VALUE, 1, 1)
    # add_case(cases, MAX_N - 1, 1, MAX_VALUE, 1, MAX_VALUE - 1)
    # add_case(cases, MAX_N, 1_999_999_937, 1_999_999_937,
    #          1_999_999_938, 1_999_999_938)

    # # Casos com capacidade igual ou capacidade de um tipo multiplo da outra.
    # for _ in range(80):
    #     capacity = RNG.randint(1, 1000)
    #     multiple = RNG.randint(1, min(20, MAX_VALUE // capacity))
    #     N = capacity * RNG.randint(1, min(MAX_N // capacity, 1000))
    #     c1 = RNG.randint(1, 10000)
    #     c2 = RNG.randint(1, 10000)
    #     add_case(cases, N, c1, capacity, c2, capacity * multiple)
    #     if len(cases) >= NUM_CASES:
    #         return cases[:NUM_CASES]

    # Casos aleatorios misturados: alguns sempre viaveis por construcao,
    # outros com N independente das capacidades (podem nao ter solucao).
    while len(cases) < NUM_CASES:
        mode = RNG.randrange(5)
        c1 = RNG.randint(1, 2_000_000)
        c2 = RNG.randint(1, 2_000_000)

        if mode == 0:
            # Escolhe quantidades de caixas e calcula N: garante solucao.
            n1 = RNG.randint(1, 100_000)
            n2 = RNG.randint(1, 100_000)
            m1 = RNG.randint(0, min(100_000, MAX_N // n1))
            m2 = RNG.randint(0, min(100_000, MAX_N // n2))
            if m1 + m2 == 0:
                m1 = 1
            N = m1 * n1 + m2 * n2
            add_case(cases, N, c1, n1, c2, n2)

        elif mode == 1:
            # Capacidades pequenas e N arbitrario: mistura solucoes e falhas.
            n1 = RNG.randint(1, 1000)
            n2 = RNG.randint(1, 1000)
            N = RNG.randint(1, 100_000)
            add_case(cases, N, c1, n1, c2, n2)

        elif mode == 2:
            # Valores grandes, incluindo casos proximos aos limites.
            n1 = RNG.randint(1, MAX_VALUE)
            n2 = RNG.randint(1, MAX_VALUE)
            N = RNG.choice([MAX_N, MAX_N - 1, MAX_N - 2, RNG.randint(1, MAX_N)])
            add_case(cases, N, c1, n1, c2, n2)

        elif mode == 3:
            # N multiplo de ambas as capacidades: certamente viavel.
            n1 = RNG.randint(1, 100_000)
            n2 = RNG.randint(1, 100_000)
            N = n1 * n2 // __import__('math').gcd(n1, n2)
            N *= RNG.randint(1, max(1, min(1000, MAX_N // N)))
            if N <= MAX_N:
                add_case(cases, N, c1, n1, c2, n2)

        else:
            # Casos com uma caixa capaz de armazenar exatamente N.
            N = RNG.randint(1, MAX_N)
            n1 = N if N < 2_000_000_000 else MAX_VALUE
            n2 = RNG.randint(1, MAX_VALUE)
            add_case(cases, N, c1, n1, c2, n2)

    return cases[:NUM_CASES]


def main():
    cases = build_cases()
    print(len(cases))
    for N, c1, n1, c2, n2 in cases:
        print(N)
        print(c1, n1)
        print(c2, n2)


if __name__ == '__main__':
    main()
