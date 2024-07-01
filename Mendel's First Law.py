def firstLaw(k, m, n):
    k, m, n = map(float, (k, m, n))

    N = (k + m + n)
    return (1 - (1 / N) * ((n * (n - 1) + n * m + m * (m - 1) / 4) / (N - 1)))

# Read k,m,n values from file
with open("organism.txt", 'r') as file:
    k, m, n = map(int, file.readline().split())

# Calculate result
result = firstLaw(k, m, n)

with open("output.txt", 'w') as output_file:
    output_file.write(str(result))


