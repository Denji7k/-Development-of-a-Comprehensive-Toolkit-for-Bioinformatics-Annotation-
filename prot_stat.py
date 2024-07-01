def read_fasta(file_path):
    sequences = {}
    try:
        with open(file_path, 'r') as file:
            seq_id = ''
            sequence = ''
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if seq_id:
                        sequences[seq_id] = sequence
                    seq_id = line[1:]
                    sequence = ''
                else:
                    sequence += line
            if seq_id:
                sequences[seq_id] = sequence
    except IOError:
        print(f"Error: Unable to read from the file '{file_path}'")
        exit()
    return sequences

def calculate_amino_acid_frequencies(sequence):
    amino_acids = {}
    for amino_acid in sequence:
        amino_acids[amino_acid] = amino_acids.get(amino_acid, 0) + 1
    return amino_acids

def process_fasta(input_file, output_file):
    sequences = read_fasta(input_file)
    try:
        with open(output_file, 'w') as f:
            for seq_id, sequence in sequences.items():
                sequence = sequence.upper()
                length = len(sequence)
                frequencies = calculate_amino_acid_frequencies(sequence)
                f.write(f">{seq_id}\n")
                f.write(f"Length of sequence: {length}\n")
                f.write("Amino acid frequencies:\n")
                for amino_acid, count in frequencies.items():
                    f.write(f"{amino_acid}: {count}\n")
                f.write("\n")
        print(f"Output has been saved to '{output_file}'")
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'")

input_file = input("Enter the input FASTA file name: ")
output_file = input("Enter the output file name: ") or f"{input_file}_output.txt"


process_fasta(input_file, output_file)
