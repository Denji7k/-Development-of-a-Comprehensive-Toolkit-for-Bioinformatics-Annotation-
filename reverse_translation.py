def read_fasta(file_path):
    """Reads protein sequence from a FASTA file and returns the sequence."""
    sequence = ''
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):  # Skip header lines starting with '>'
                sequence += line
    return sequence.upper()  # Return the concatenated sequence in uppercase

table = {
    "W": 1, "M": 1,
    "F": 2, "Y": 2, "C": 2, "H": 2, "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2,
    "I": 3,
    "P": 4, "T": 4, "V": 4, "A": 4, "G": 4,
    "L": 6, "S": 6, "R": 6
}

# Read protein sequence from FASTA file
# Read DNA sequences from FASTA file
sequence = input("Enter the input file:").strip()
protein_seq = read_fasta(sequence)

# Calculate the result based on the amino acids
result = 1
for amino_acid in protein_seq:
    result = (result * table.get(amino_acid, 1)) % 1000000

output_file =  input("Eneter the output file:").strip()or f"{sequence}_output.txt"
# Write the result into a new file
with open(output_file, 'w') as output_file:
    output_file.write(str(result))

print("Processing complete.")
