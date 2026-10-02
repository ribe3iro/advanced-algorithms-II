import random

MAX_L = 26
MAX_S = 351
T = 500

def solve(queries):
    answers = []

    for L, S in queries:
        dp = [[0] * (S + 1) for _ in range(L + 1)]
        dp[0][0] = 1

        for c in range(1, 27):
            for length in range(min(c, L), 0, -1):
                for total in range(S, c - 1, -1):
                    dp[length][total] += dp[length - 1][total - c]

        answers.append(dp[L][S])

    return answers


def generate_tests(seed=123):
    random.seed(seed)

    tests = []

    # # Casos pequenos e fáceis de verificar
    # tests.extend([
    #     (1, 1),
    #     (1, 2),
    #     (1, 26),
    #     (2, 3),
    #     (2, 4),
    #     (2, 27),
    #     (3, 6),
    #     (3, 7),
    #     (3, 10),
    #     (3, 78),
    #     (26, 351),
    # ])

    # # Casos impossíveis por soma mínima/máxima.
    # for L in range(1, 27):
    #     min_sum = L * (L + 1) // 2
    #     max_sum = L * (53 - L) // 2

    #     if min_sum > 1:
    #         tests.append((L, min_sum - 1))

    #     if max_sum < MAX_S:
    #         tests.append((L, max_sum + 1))

    # # Casos nos limites possíveis de soma.
    # for L in range(1, 27):
    #     min_sum = L * (L + 1) // 2
    #     max_sum = L * (53 - L) // 2

    #     tests.append((L, min_sum))
    #     tests.append((L, max_sum))

    # Casos aleatórios válidos.
    while len(tests) < T:
        L = random.randint(1, MAX_L)
        S = random.randint(1, MAX_S)

        tests.append((L, S))

    random.shuffle(tests)

    return tests[:T]


queries = generate_tests()
answers = solve(queries)

with open("input.txt", "w") as f:
    f.write(f"{len(queries)}\n")

    for L, S in queries:
        f.write(f"{L} {S}\n")

with open("output.txt", "w") as f:
    for answer in answers:
        f.write(f"{answer}\n")
