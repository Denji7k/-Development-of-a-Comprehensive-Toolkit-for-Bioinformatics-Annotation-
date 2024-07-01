from collections import OrderedDict

def parse_fasta(file_path):
    sequences = OrderedDict()
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

def repeated_sequences(sequences, n):
    return [seq * n for seq in sequences]

def profile_matrix(parsed_fa):
    sequences = list(parsed_fa.values())
    matrix_size = len(sequences[0])  
    profile_matrix = {base: [0] * matrix_size for base in 'ATCG'}

    for seq in sequences:
        if len(seq) != matrix_size:
            raise ValueError("All sequences must have the same length")

    for seq in sequences:
        for i, base in enumerate(seq):
            if base in profile_matrix:
                profile_matrix[base][i] += 1

    return profile_matrix

def consensus_string(profile_matrix):
    consensus = ''
    for i in range(len(profile_matrix['A'])):
        counts = [profile_matrix[base][i] for base in 'ATCG']
        max_count = max(counts)
        max_bases = [base for base, count in zip('ATCG', counts) if count == max_count]
        consensus += max_bases[0]
    return consensus

fasta_file = 'fasta_sequence.txt'  
parsed_fa = parse_fasta(fasta_file)

sequences = list(parsed_fa.values())
matrix_size = 10
matrix = [sequences[i:i+matrix_size] for i in range(0, len(sequences), matrix_size)]

for row in matrix:
    for seq in row:
        print(" ".join(seq))

profile_matrix_result = profile_matrix(parsed_fa)
for base, counts in profile_matrix_result.items():
    print (base),
    print ("".join(map(str, counts)))

consensus = consensus_string(profile_matrix_result)
print("Consensus string:", consensus)
