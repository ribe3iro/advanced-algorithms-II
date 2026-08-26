import argparse
import random
import subprocess

SOLVER_PATH = "./main"

EVENTS = {
    'DMG': (0, 1000),
    'POISON': (0, 1),
    'HEAL': (0, 1000),
    'BLESS': (0, 10)
}

def run_solver(input_data):
    try:
        result = subprocess.run(
            [SOLVER_PATH],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=0.01
        )
    except subprocess.TimeoutExpired:
        return None, "TIME LIMIT"

    if result.returncode != 0:
        return None, f"RUNTIME ERROR (code {result.returncode})"

    return result.stdout, None

def generate_in_n_out(num_cases):
    in_content = ""
    out_content = ""
    in_content += f"{num_cases}\n"  # T
    t = 0
    while t < num_cases:
        E = random.randint(1, 50)
        case_content = f"{E}\n"
        for e in range(E):
            event, interval = random.choice(list(EVENTS.items()))
            case_content += f"{event}\n"
            case_content += f"{round(random.uniform(*interval), 3)}\n"
        output, error = run_solver(f"1\n{case_content}")
        if output:
            t += 1
            in_content += case_content
            out_content += f"{output}"
    return in_content, out_content
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_prefix", nargs='+', required=True)

    args = parser.parse_args()

    for file_prefix in args.file_prefix:
        with open(f'{file_prefix}.in', 'r') as file:
            in_content = file.readlines()
        with open(f'{file_prefix}.out', 'r') as file:
            out_content = file.readlines()

        for out_line in out_content:
            out = float(line)
            T = int(in_content[0])

            num_line = 1
            for t in range(T):
                E = int(in_content[num_line])
                for e in range(E):
                    in_content[e]
        



if __name__ == '__main__':
    main()
