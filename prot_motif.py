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

def find_motif(sequence, motif):
    motif_length = len(motif)
    return [i + 1 for i in range(len(sequence) - motif_length + 1) if sequence[i:i+motif_length] == motif]

def write_positions_to_file(sequences, motif, file_path):
    with open(file_path, 'w') as file:
        for seq_id, sequence in sequences.items():
            positions = find_motif(sequence, motif)
            file.write(f"Sequence ID: {seq_id}\nPositions: {', '.join(map(str, positions)) if positions else 'Not available'}\n\n")

input_file = input("Enter the input file: ").strip()
sequences = parse_fasta(input_file)
motif = input("Enter the motif sequence to search for: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"
write_positions_to_file(sequences, motif, output_file)
print(f"Positions of '{motif}' in all sequences have been written to '{output_file}'.")
