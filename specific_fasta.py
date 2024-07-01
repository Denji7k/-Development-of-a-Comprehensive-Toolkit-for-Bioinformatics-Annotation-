def parse_fasta(fasta_data):
    """Parse FASTA data into a dictionary."""
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

def extract_region(sequences, start, end):
    """Extract a specific region from each sequence."""
    return {key: seq[start-1:end] for key, seq in sequences.items()}

# Get user inputs
input_file = input("Enter the input FASTA file: ").strip()
start, end = int(input("Enter start position: ")), int(input("Enter end position: "))

# Read and process FASTA file
with open(input_file) as f:
    sequences = parse_fasta(f.read())

# Extract region and write to output file
output_file = input("Enter output file name (default: <input_file>_output.txt): ").strip() or f"{input_file}_output.txt"
with open(output_file, 'w') as f:
    for key, seq in extract_region(sequences, start, end).items():
        f.write(f">{key}\n{seq}\n")

print(f"Extracted regions saved in '{output_file}'.")
