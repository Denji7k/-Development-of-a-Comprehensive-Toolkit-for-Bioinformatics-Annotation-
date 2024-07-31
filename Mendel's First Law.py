def firstLaw(k, m, n):
    k, m, n = map(float, (k, m, n))
    
    N = (k + m + n)
    return (1 - (1 / N) * ((n * (n - 1) + n * m + m * (m - 1) / 4) / (N - 1)))

# Get k, m, n values from user input
k = float(input("Enter the value for k: "))
m = float(input("Enter the value for m: "))
n = float(input("Enter the value for n: "))

# Calculate result
result = firstLaw(k, m, n)

# Write the result to a file
with open("output.txt", 'w') as output_file:
    output_file.write(str(result))
    
print(f"Result has been written to 'output.txt'.")
