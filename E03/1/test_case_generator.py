import argparse
import random
import subprocess

SOLVER_PATH = "./main"

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
        return result.stdout, f"RUNTIME ERROR (code {result.returncode})"

    return result.stdout, None

def generate_in_n_out(num_cases):
    in_content = ""
    out_content = ""
    in_content += f"{num_cases}\n"  # T
    t = 0
    while t < num_cases:
        a = random.randint(0, int(1e10)-1)
        b = random.randint(1, int(1e18))
        case_content = f"{a} {b}\n"
        output, error = run_solver(f"1\n{case_content}")
        if not error:
            t += 1
            in_content += case_content
            out_content += f"{output}"
        elif error == "TIME LIMIT":
            print("Timeout!")
        else:
            print(error)
            print(output)
            exit()
    return in_content, out_content
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=500)
    parser.add_argument("--sets", type=int, default=1)
    parser.add_argument("--seed", type=int, default=False)

    args = parser.parse_args()

    if(args.seed is not False):
        random.seed(args.seed)

    for i in range(args.sets):
        in_content, out_content = generate_in_n_out(args.n)
        with open(f'{i}.in', 'w') as file:
            file.write(in_content)
        with open(f'{i}.out', 'w') as file:
            file.write(out_content)
        



if __name__ == '__main__':
    main()
