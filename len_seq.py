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

def calculate_sequence_length(sequence):
    return len(sequence)

# Get input and output file paths from the user
input_file_path = input("Enter the input file: ").strip()
output_file_path = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file_path}_output.txt"


parsed_fa = parse_fasta(input_file_path)

# Write result for each sequence into a new file
with open(output_file_path, 'w') as output_file:
    for key, value in parsed_fa.items():
        seq_length = calculate_sequence_length(value)
        output_file.write(f"{key}: The length of the sequence is: {seq_length}\n")

print(f"The length of each sequence has been written to {output_file_path}")
