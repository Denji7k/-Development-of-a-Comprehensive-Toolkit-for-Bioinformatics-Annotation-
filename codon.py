def detect_stop_and_start_codons(dna_sequence):
    """Detects all start and stop codons in a DNA sequence."""
    stop_codons = ['TAA', 'TAG', 'TGA']
    start_codon = 'ATG'

    # Find all positions of stop codons
    stop_codon_positions = [i + 1 for i in range(len(dna_sequence) - 2) if dna_sequence[i:i+3] in stop_codons]
    # Find all positions of start codons
    start_codon_positions = [i + 1 for i in range(len(dna_sequence) - 2) if dna_sequence[i:i+3] == start_codon]

    return stop_codon_positions, start_codon_positions

def read_fasta(file_path):
    """Reads sequences from a FASTA file."""
    sequences = []
    current_sequence = ''
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence.upper())
                current_sequence = ''
            else:
                current_sequence += line
        if current_sequence:
            sequences.append(current_sequence.upper())
    
    return sequences

# Get file paths from user
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

# Read sequences from the FASTA file
sequences = read_fasta(input_file)
if not sequences:
    raise ValueError("Error: No sequences found in the FASTA file.")

# Detect codons and write results to the output file
with open(output_file, 'w') as file:
    for i, sequence in enumerate(sequences, start=1):
        stop_positions, start_positions = detect_stop_and_start_codons(sequence)
        file.write(f"Sequence {i}:\n")
        file.write(f"Stop Codon Positions: {stop_positions}\n")
        file.write(f"Start Codon Positions: {start_positions}\n\n")

print("Processing complete.")
