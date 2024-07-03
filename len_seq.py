from collections import OrderedDict

def parse_fasta(file_path):
    sequences = OrderedDict()
    current_key = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_key is not None:
                    sequences[current_key] = ''.join(sequences.get(current_key, ''))
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                if current_key is not None:
                    sequences[current_key] += line

        if current_key is not None:
            sequences[current_key] = ''.join(sequences.get(current_key, ''))

    return sequences

def calculate_sequence_length(sequence):
    return len(sequence)

# Get input and output file paths from the user
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

parsed_fa = parse_fasta(input_file)

# Write result for each sequence into a new file
with open(output_file, 'w') as file:
    for key, value in parsed_fa.items():
        seq_length = calculate_sequence_length(value)
        file.write(f"{key}: The length of the sequence is: {seq_length}\n")

print(f"The length of each sequence has been written to {output_file}")
