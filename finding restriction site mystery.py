def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in sequence[::-1])

def find_palindromes(sequence, min_length=4, max_length=12):
    palindromes = []
    for i in range(len(sequence)):
        for length in range(min_length, max_length + 1):
            if i + length > len(sequence):  # Avoid going beyond the sequence length
                break
            substring = sequence[i:i+length]
            rev_com = reverse_complement(substring)
            if rev_com == substring:
                palindromes.append((i+1, length))
    return palindromes

file_path = input("Enter the input file:")
sequence = read_fasta(file_path)
palindromes = find_palindromes(sequence)

output_path = input("Enter the output file:")
with open(output_path, 'w') as output_file:
    for start, length in palindromes:
        output_file.write(f"{start} {length}\n")

print(f"Output written to {output_path}")
