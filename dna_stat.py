def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence.upper())
                    sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence.upper())
    return sequences

Nucleotides = ("A", "C", "G", "T")

def validate(dna_sequence):
    """Validates if a DNA sequence contains only valid nucleotides."""
    return all(nuc in Nucleotides for nuc in dna_sequence.upper())

def countfreq(dna_sequence):
    """Counts the frequency of each nucleotide in a DNA sequence."""
    frequency = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in dna_sequence.upper():
        if nucleotide in frequency:
            frequency[nucleotide] += 1
    return frequency

# Get input and output file paths from the user
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use default name): ").strip() or f"{input_file}_output.txt"

# Read DNA sequences from FASTA file
sequences = read_fasta(input_file)

# Write results to the output file
with open(output_file, 'w') as file:
    for seq_num, dna_sequence in enumerate(sequences, start=1):
        is_valid = validate(dna_sequence)
        frequency = countfreq(dna_sequence)
        
        file.write(f"Sequence {seq_num}:\n")
        file.write(f"Valid: {is_valid}\n")
        file.write(f"Length: {len(dna_sequence)}\n")
        file.write(f"Nucleotide frequency: {frequency}\n\n")

print("Processing complete.")
