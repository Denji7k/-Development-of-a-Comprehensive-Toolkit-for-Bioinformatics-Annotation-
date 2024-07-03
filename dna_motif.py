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

def find_motif_positions(sequence, motif_sequence):
    return [i + 1 for i in range(len(sequence) - len(motif_sequence) + 1) if sequence[i:i+len(motif_sequence)] == motif_sequence]

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

motif_sequence = input("Enter the motif sequence to search for: ").strip()

sequences = parse_fasta(input_file)

sequence_positions = {seq_id: find_motif_positions(seq, motif_sequence) for seq_id, seq in sequences.items()}

with open(output_file, 'w') as output_file:
    for seq_id, positions in sequence_positions.items():
        output_file.write(f"{seq_id}: {', '.join(map(str, positions))}\n")

print(f"Positions of '{motif_sequence}' in each sequence have been written to {output_file}")
