import operator as ne

def calculate_mutations(seq1, seq2):
    return sum(map(ne.ne, seq1, seq2))

def write_output(mutations, output_filename):
    with open(output_filename, 'w') as output_file:
        output_file.write(str(mutations))

def read_fasta_file(filename):
    sequences = []
    with open(filename, 'r') as f:
        seq_id, seq = None, []
        for line in f:
            line = line.rstrip()
            if line.startswith('>'):
                if seq_id:
                    sequences.append((''.join(seq_id), ''.join(seq)))
                seq_id, seq = line[1:], []
            else:
                seq.append(line)
        if seq_id:
            sequences.append((''.join(seq_id), ''.join(seq)))
    return sequences

input_files = input("Enter the input FASTA file path: ").strip()
input_files = input("Enter the other input FASTA file path: ").strip()
sequences = [read_fasta_file(file) for file in input_files]

for (seq_id1, seq1), (seq_id2, seq2) in zip(*sequences):
    mutations = calculate_mutations(seq1, seq2)
    output_filename = f'{seq_id1}_{seq_id2}_mutations.txt'
    write_output(mutations, output_filename)

print("Mutation calculations and outputs have been written to files.")
