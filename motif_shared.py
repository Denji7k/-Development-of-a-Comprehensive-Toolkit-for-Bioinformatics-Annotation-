def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = []
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def find_longest_common_substring(s1, s2):
    substrings1 = {s1[i:j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1)}
    substrings2 = {s2[i:j] for i in range(len(s2)) for j in range(i + 1, len(s2) + 1)}
    common_substrings = substrings1 & substrings2
    return max(common_substrings, key=len, default='')

def main():
    input_file = input("Enter the input file: ").strip()
    sequences = read_fasta(input_file)

    if len(sequences) < 2:
        raise ValueError("Error: The FASTA file must contain at least two sequences.")

    shared_motif = sequences[0]
    for sequence in sequences[1:]:
        shared_motif = find_longest_common_substring(shared_motif, sequence)

    output_file = input("Enter the output file (leave blank to use input file name): ").strip()
    if not output_file:
        output_file = f"{input_file}_output.txt"

    with open(output_file, 'w') as output_file:
        output_file.write(shared_motif)

    print("Processing complete.")

if __name__ == "__main__":
    main()
