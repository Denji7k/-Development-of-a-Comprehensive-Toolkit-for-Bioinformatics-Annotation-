import math
import itertools

n = int(input('Eneter the value:'))
factorial_n = math.factorial(n)
permutations = itertools.permutations(range(1, n + 1))

output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{"gene order"}_output.txt"
with open(output_file, 'w') as output_file:
    output_file.write(f"{factorial_n}\n")
    for perm in permutations:
        output_file.write(' '.join(map(str, perm)) + "\n")


