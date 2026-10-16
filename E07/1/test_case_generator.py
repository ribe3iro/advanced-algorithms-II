#!/usr/bin/env python3

import random

RNG = random.Random(999)

NUM_CASES = 1000
MAX_DIGITS = 1000


def make_number(length, divisible_by_9):
    """Gera um numero com tamanho exato e sem zeros iniciais."""

    if length == 1:
        if divisible_by_9:
            return "9"
        return str(RNG.randint(1, 8))

    digits = [str(RNG.randint(1, 9))]

    for _ in range(length - 1):
        digits.append(str(RNG.randint(0, 9)))

    total = sum(int(digit) for digit in digits)
    last = int(digits[-1])

    if divisible_by_9:
        # Ajusta o ultimo digito para tornar a soma multipla de 9.
        digits[-1] = str((last - total % 9) % 9)

    elif total % 9 == 0:
        # Altera o ultimo digito para deixar de ser multiplo de 9.
        digits[-1] = str((last + 1) % 10)

        if sum(int(digit) for digit in digits) % 9 == 0:
            digits[-1] = str((last + 2) % 10)

    return "".join(digits)


def build_cases():
    cases = set()
    # {
        # Casos pequenos.
        # "1", "8", "9", "10", "18", "19",
        # "27", "28", "81", "99", "100",
        # "108", "111", "123", "126",
        # "999", "1000", "9999", "10000", "99999",

        # # Casos com muitos digitos repetidos.
        # "999999999",
        # "999999999999999999999",
        # "9999999999999999999999999999998",
    # }

    # Explora diferentes comprimentos, incluindo o limite de 1000.
    # lengths = [10, 50, 100, 250, 500, 999, 1000]

    # for length in lengths:
    # #     cases.add("9" * length)
    # #     cases.add("1" * length)
    # #     cases.add("8" + "0" * (length - 1))

    #     cases.add(make_number(length, True))
    #     cases.add(make_number(length, False))

    # Gera casos aleatorios de diferentes tamanhos.
    lengths = [
        10, 20, 50, 100, 250, 500, 999, 1000
    ]

    while len(cases) < NUM_CASES:
        length = RNG.choice(lengths)
        divisible = bool(RNG.getrandbits(1))

        number = make_number(length, divisible)
        cases.add(number)

    return sorted(cases, key=lambda n: (len(n), n))[:NUM_CASES]


def main():
    cases = build_cases()

    print(len(cases))

    for number in cases:
        print(number)


if __name__ == "__main__":
    main()
