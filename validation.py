def clean_sequence(seq):
    return ''.join(base for base in seq if base in 'ACGTU')

def identify_sequence_type(seq):
    if 'T' in seq: return 'DNA'
    if 'U' in seq: return 'RNA'
    return None

def read_fasta(filename):
    sequences = {}
    with open(filename) as f:
        header = None
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences[header] = sequence
                header, sequence = line[1:], ''
            else:
                sequence += line
        if header:
            sequences[header] = sequence
    return sequences

# Get file names from user
input_file = input("Enter input FASTA file name: ").strip()
output_file = input("Enter output file name (default: input_file_output.txt): ").strip() or f"{input_file}_output.txt"

# Read and process each sequence
sequences = read_fasta(input_file)
with open(output_file, 'w') as f:
    for header, seq in sequences.items():
        cleaned_seq = clean_sequence(seq)
        seq_type = identify_sequence_type(cleaned_seq)
        f.write(f"Header: {header}\n")
        f.write(f"Cleaned sequence: {cleaned_seq}\n")
        f.write(f"Identified sequence type: {seq_type}\n\n")

print(f"Results saved to '{output_file}'.")
