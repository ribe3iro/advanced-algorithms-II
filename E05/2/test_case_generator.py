import random

MAX_T = 1000
MAX_N = 30
MAX_D = 100
MAX_V = 1000


def solve(t, treasures):
    """
    Resolve o problema e também conta quantas escolhas diferentes
    atingem o valor ótimo.

    O número de soluções é limitado a 2, pois só precisamos saber
    se a solução ótima é única.
    """
    n = len(treasures)

    # dp[i][e] = melhor valor usando os primeiros i tesouros
    dp = [[0] * (t + 1) for _ in range(n + 1)]

    # ways[i][e] = quantidade de maneiras de obter dp[i][e].
    # Mantemos no máximo 2.
    ways = [[0] * (t + 1) for _ in range(n + 1)]

    for e in range(t + 1):
        ways[0][e] = 1

    for i in range(1, n + 1):
        d, v = treasures[i - 1]
        cost = 3 * d

        for e in range(t + 1):
            skip_value = dp[i - 1][e]
            skip_ways = ways[i - 1][e]

            dp[i][e] = skip_value
            ways[i][e] = skip_ways

            if cost <= e:
                take_value = dp[i - 1][e - cost] + v
                take_ways = ways[i - 1][e - cost]

                if take_value > dp[i][e]:
                    dp[i][e] = take_value
                    ways[i][e] = take_ways
                elif take_value == dp[i][e]:
                    ways[i][e] = min(2, ways[i][e] + take_ways)

    # Reconstrução determinística.
    chosen = []
    e = t

    for i in range(n, 0, -1):
        d, v = treasures[i - 1]
        cost = 3 * d

        if cost <= e and dp[i][e] == dp[i - 1][e - cost] + v:
            # Em casos gerados por este script, a solução ótima é única.
            chosen.append(i - 1)
            e -= cost

    chosen.reverse()

    return dp[n][t], chosen, ways[n][t]


def generate_case():
    """
    Gera um caso com solução ótima única.

    Isso é útil para testes com comparação exata da saída:
    não haverá duas respostas diferentes igualmente ótimas.
    """
    while True:
        n = random.randint(1, MAX_N)
        t = random.randint(1, MAX_T)

        treasures = []

        for _ in range(n):
            d = random.randint(1, MAX_D)
            v = random.randint(1, MAX_V)
            treasures.append((d, v))

        value, chosen, number_of_optima = solve(t, treasures)

        if number_of_optima == 1:
            return t, treasures, value, chosen


def add_edge_cases():
    cases = []

    # # Nenhum tesouro cabe.
    # cases.append((
    #     10,
    #     [(4, 100), (5, 200), (10, 500)]
    # ))

    # # Todos os tesouros cabem.
    # cases.append((
    #     100,
    #     [(1, 10), (2, 20), (3, 30)]
    # ))

    # # Escolha entre um tesouro caro e vários baratos.
    # cases.append((
    #     30,
    #     [(10, 100), (5, 40), (5, 40), (5, 40)]
    # ))

    # Caso com n máximo.
    treasures = []
    for i in range(MAX_N):
        treasures.append((1 + (i % 20), 10 + i))
    cases.append((1000, treasures))

    return cases


def write_test(filename="input.txt", output_filename="output.txt"):
    # Use uma semente fixa para tornar o conjunto reproduzível.
    random.seed(42)

    cases = add_edge_cases()

    # Complete o conjunto com casos aleatórios.
    while len(cases) < 100:
        t, treasures, _, _ = generate_case()
        cases.append((t, treasures))

    # Para os casos aleatórios, algumas soluções podem ter empate.
    # Regeneramos todos os casos para garantir solução ótima única.
    cases_with_answers = []

    for t, treasures in cases:
        value, chosen, number_of_optima = solve(t, treasures)

        if number_of_optima != 1:
            t, treasures, value, chosen = generate_case()

        cases_with_answers.append((t, treasures, value, chosen))

    with open(filename, "w") as f:
        t, treasures, _, _ = cases_with_answers[0]

        # O exercício recebe APENAS UM caso por execução.
        f.write(f"{t} {len(treasures)}\n")

        for d, v in treasures:
            f.write(f"{d} {v}\n")

    with open(output_filename, "w") as f:
        _, treasures, value, chosen = cases_with_answers[0]

        f.write(f"{value}\n")
        f.write(f"{len(chosen)}\n")

        for i in chosen:
            d, v = treasures[i]
            f.write(f"{d} {v}\n")


if __name__ == "__main__":
    write_test()
