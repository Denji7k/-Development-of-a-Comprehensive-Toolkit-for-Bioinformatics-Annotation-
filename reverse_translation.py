def read_fasta(file_path):
    sequences = {}
    current_key = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                if current_key:
                    sequences[current_key] += line
    return sequences

table = {
    "W": 1, "M": 1,
    "F": 2, "Y": 2, "C": 2, "H": 2, "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2,
    "I": 3,
    "P": 4, "T": 4, "V": 4, "A": 4, "G": 4,
    "L": 6, "S": 6, "R": 6
}

input_file = input("Enter the input file:").strip()
protein_sequences = read_fasta(input_file)

results = {}
for seq_id, protein_seq in protein_sequences.items():
    result = 1
    for amino_acid in protein_seq.upper():
        result = (result * table.get(amino_acid, 1)) % 1000000
    results[seq_id] = result

output_file = input("Enter the output file:").strip() or f"{input_file}_output.txt"

with open(output_file, 'w') as file:
    for seq_id, result in results.items():
        file.write(f"{seq_id}:\n {result}\n")

print("Output stored in 'fasta_sequence.txt_ouput.txt' ")
