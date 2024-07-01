import math
import itertools

n = 2
factorial_n = math.factorial(n)
permutations = itertools.permutations(range(1, n + 1))

with open('output.txt', 'w') as output_file:
    output_file.write(f"{factorial_n}\n")
    for perm in permutations:
        output_file.write(' '.join(map(str, perm)) + "\n")


