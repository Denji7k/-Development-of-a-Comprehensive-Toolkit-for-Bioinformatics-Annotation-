def parse_fasta(file_path):
    sequences = {}
    current_key = None
    current_sequence = []
    sequence_count = 1
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_key is not None:
                    sequences[current_key] = ''.join(current_sequence)
                current_key = f"{line[1:]}_{sequence_count}"
                sequence_count += 1
                current_sequence = []
            else:
                current_sequence.append(line)
        if current_key is not None:
            sequences[current_key] = ''.join(current_sequence)
    
    return sequences

def find_motif_positions(sequence, motif_sequence):
    if len(motif_sequence) > len(sequence):
        return []
    return [i + 1 for i in range(len(sequence) - len(motif_sequence) + 1) if sequence[i:i+len(motif_sequence)] == motif_sequence]

# Get user inputs
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"
motif_sequence = input("Enter the motif sequence to search for: ").strip().upper()

# Check if motif_sequence is valid
if not motif_sequence:
    print("Error: Motif sequence cannot be empty.")
else:
    # Parse the FASTA file
    sequences = parse_fasta(input_file)
    
    if not sequences:
        print("Error: No sequences found or issue reading file.")
    else:
        # Find motif positions in each sequence
        sequence_positions = {seq_id: find_motif_positions(seq, motif_sequence) for seq_id, seq in sequences.items()}

        # Write results to the output file
        with open(output_file, 'w') as f:
            for seq_id, positions in sequence_positions.items():
                f.write(f"{seq_id}: {', '.join(map(str, positions))}\n")
        
        print(f"Positions of '{motif_sequence}' have been written to {output_file}")
