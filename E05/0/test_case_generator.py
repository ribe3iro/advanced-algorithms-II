import random

MAX_N = 10000
T = 500

def solve(queries):
    max_n = max(queries)

    dp = [max_n + 1] * (max_n + 1)
    dp[0] = 0

    for n in range(1, max_n + 1):
        for i in range(1, int(n ** 0.5) + 1):
            dp[n] = min(dp[n], dp[n - i * i] + 1)

    return [dp[n] for n in queries]


def generate_tests():
    tests = []

    # # Casos pequenos
    # tests.extend(range(1, 21))

    # # Quadrados perfeitos
    # for i in range(1, 101):
    #     if i * i <= MAX_N:
    #         tests.append(i * i)

    # # Valores próximos de quadrados
    # for i in range(1, 101):
    #     square = i * i

    #     for delta in [-2, -1, 1, 2]:
    #         n = square + delta

    #         if 1 <= n <= MAX_N:
    #             tests.append(n)

    # Casos aleatórios
    while len(tests) < T:
        tests.append(random.randint(1, MAX_N))

    # # Mantém exatamente T casos
    random.shuffle(tests)
    return tests[:T]


queries = generate_tests()
answers = solve(queries)

with open("input.txt", "w") as f:
    f.write(f"{len(queries)}\n")

    for n in queries:
        f.write(f"{n}\n")

with open("output.txt", "w") as f:
    for answer in answers:
        f.write(f"{answer}\n")
