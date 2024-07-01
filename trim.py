def parse_fasta(fasta_data: str) -> dict:
    """Parse FASTA data into a dictionary of sequences."""
    sequences = {}
    current_key = None

    for line in fasta_data.splitlines():
        line = line.strip()
        if line.startswith('>'):
            current_key = line[1:]
            sequences[current_key] = ''
        else:
            sequences[current_key] += line.replace(' ', '')

    return sequences

# Get input and output file paths from user
input_file = input("Enter the input FASTA file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

# Read FASTA data from input file
with open(input_file, 'r') as f:
    fasta_data = f.read()

# Parse the FASTA data
sequences_dict = parse_fasta(fasta_data)

# Write the cleaned sequences to the output file
with open(output_file, 'w') as f:
    for key, sequence in sequences_dict.items():
        f.write(f">{key}\n{sequence}\n")

print(f"Processed sequences saved in '{output_file}'.")
