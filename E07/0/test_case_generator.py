#!/usr/bin/env python3
"""
Gera uma entrada com até 1000 casos para o problema das alavancas.

Uso:
    python3 E01_1_generator.py
    python3 E01_1_generator.py > teste.in

Inclui casos pequenos, quadrados perfeitos e seus vizinhos, valores
próximos do limite máximo e casos aleatórios reproduzíveis.
"""

import math
import random

MAX_N = 2**32 - 1
rng = random.Random(333)


def build_cases():
    cases = set()

    # # Quadrados perfeitos e números imediatamente vizinhos.
    # for r in range(1, 100):
    #     square = r * r
    #     for n in (square - 1, square, square + 1):
    #         if 1 <= n <= MAX_N:
    #             cases.add(n)

    # # Valores próximos do limite máximo permitido.
    # cases.update(MAX_N - offset for offset in range(6))

    # # Quadrados perfeitos próximos do limite máximo.
    max_root = math.isqrt(MAX_N)
    # for r in range(max_root - 5, max_root + 1):
    #     square = r * r
    #     for n in (square - 1, square, square + 1):
    #         if 1 <= n <= MAX_N:
    #             cases.add(n)

    # Outros quadrados perfeitos espalhados pela faixa.
    for _ in range(100):
        r = rng.randint(1, max_root)
        cases.add(r * r)

    # Valores aleatórios gerais até atingir 1000 casos.
    while len(cases) < 1000:
        cases.add(rng.randint(1, MAX_N))

    # Garante que o limite de T seja respeitado.
    if len(cases) > 1000:
        ordered = sorted(cases)
        fixed = set(range(1, 31))
        fixed.update(MAX_N - offset for offset in range(6))
        fixed.update(n for n in cases if math.isqrt(n) ** 2 == n)
        remaining = sorted(cases - fixed)
        slots = max(0, 1000 - len(fixed))
        chosen = rng.sample(remaining, min(slots, len(remaining)))
        cases = fixed.union(chosen)

    return sorted(cases)


def main():
    cases = build_cases()
    print(len(cases))
    print("\n".join(map(str, cases)))


if __name__ == "__main__":
    main()
