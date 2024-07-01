def parse_fasta(file_path):
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

def calculate_total_mass(sequence, mass_table):
    return sum(mass_table.get(aa, 0) for aa in sequence)

# Protein mass table (shortened for clarity)
protein_mass_table = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
}

# input FASTA file path
input_file_path = input("Enter the input file: ").strip()
output_file_path = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file_path}_output.txt"


# Parse the sequences from the input FASTA file
sequences = parse_fasta(input_file_path)

# Calculate total masses for each sequence
sequence_masses = {seq_id: calculate_total_mass(seq.upper(), protein_mass_table) for seq_id, seq in sequences.items()}

# Write total masses to the output file
with open(output_file_path, 'w') as output_file:
    for seq_id, mass in sequence_masses.items():
        output_file.write(f"{seq_id}: {mass}\n")

print(f"Total masses of protein sequences have been written to {output_file_path}")

