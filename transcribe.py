def transcribe_dna_to_rna(input_file, output_file):
    sequences = []
    current_sequence = ''

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences.append((seq_id, current_sequence.replace('T', 'U')))
                seq_id = line[1:]
                current_sequence = ''
            else:
                current_sequence += line

        if current_sequence:
            sequences.append((seq_id, current_sequence.replace('T', 'U')))

    with open(output_file, 'w') as rna_file:
        for seq_id, rna_seq in sequences:
            rna_file.write(f">{seq_id}\n{rna_seq}\n")

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"


transcribe_dna_to_rna(input_file, output_file)
print(f"RNA sequences have been written to '{output_file}'.")
