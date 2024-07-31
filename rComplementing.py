def read_fasta(file_path):
    sequences = {}
    try:
        with open(file_path, 'r') as file:
            seq_id = None
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    seq_id = line[1:]
                    sequences[seq_id] = ''
                elif seq_id:  # Check if seq_id is set to avoid appending to non-existent keys
                    sequences[seq_id] += line
    except IOError:
        print(f"Error: Unable to read from the file '{file_path}'")
        exit()
    return sequences

def complement(seq):
    return seq.translate(str.maketrans('ATCG', 'TAGC'))

def write_complementary_fasta(sequences, output_file):
    try:
        with open(output_file, 'w') as f:
            for seq_id, seq in sequences.items():
                f.write(f">{seq_id}\n{complement(seq)}\n")
        print(f"Complementary strands have been saved to '{output_file}'")
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'")

input_file = input("Enter the input FASTA file name: ").strip()
output_file = input("Enter the output file name: ").strip() or f"{input_file}_output.txt"

sequences = read_fasta(input_file)
write_complementary_fasta(sequences, output_file)
