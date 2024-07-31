def transcribe_dna_to_rna(input_file, output_file):
    sequences = []
    header = ''
    seq_id = ''

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    # Transcribe the sequence and add it to the list
                    sequences.append((seq_id, header.replace('T', 'U')))
                seq_id = line[1:]  # Extract sequence ID
                header = ''  # Reset header for the new sequence
            else:
                header += line  # Accumulate sequence lines

        # Process the last sequence
        if header:
            sequences.append((seq_id, header.replace('T', 'U')))

    with open(output_file, 'w') as rna_file:
        for seq_id, rna_seq in sequences:
            rna_file.write(f">{seq_id}\n{rna_seq}\n")

if __name__ == "__main__":
    input_file = input("Enter the input file: ").strip()
    output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

    transcribe_dna_to_rna(input_file, output_file)
    print(f"RNA sequences have been written to '{output_file}'.")
