def parse_fasta(file_path):
    """Parse the FASTA file into a dictionary of sequences."""
    sequences = {}
    current_key = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                sequences[current_key] += line
    return sequences

def find_motif(sequence, motif):
    """Find all positions of the motif in the sequence."""
    motif_length = len(motif)
    return [i + 1 for i in range(len(sequence) - motif_length + 1) if sequence[i:i+motif_length] == motif]

def write_positions_to_file(positions, file_path):
    """Write positions to a file."""
    with open(file_path, 'w') as file:
        file.write('\n'.join(map(str, positions)) + '\n')

# Prompt user for input FASTA file path
input_file_path = input("Enter the input file: ").strip()

# Read the FASTA file
sequences = parse_fasta(input_file_path)

# Prompt user for the motif sequence to search for
motif = input("Enter the motif sequence to search for: ").strip()

# Prompt user for output file path
output_file_path = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file_path}_output.txt"

# Find and write motif positions for each sequence
with open(output_file_path, 'w') as out_file:
    for seq_id, sequence in sequences.items():
        positions = find_motif(sequence, motif)
        if positions:
            out_file.write(f"Sequence ID: {seq_id}\nPositions: {', '.join(map(str, positions))}\n\n")

print(f"Positions of '{motif}' in all sequences have been written to '{output_file_path}'.")
