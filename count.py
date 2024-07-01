from collections import OrderedDict

def parse_fasta(file_path):
    sequences = OrderedDict()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                sequences[current_key] += line
    return sequences

def calculate_content(sequence, bases):
    count = sum(sequence.count(base) for base in bases)
    return round(float(count) / len(sequence) * 100, 2)

# Get input and output file paths from the user
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"


parsed_fa = parse_fasta(input_file_path)

# Write results for each sequence into the output file
with open(output_file_path, 'w') as output_file:
    for key, value in parsed_fa.items():
        gc_content = calculate_content(value, 'GC')
        if 'U' in value:
            au_content = calculate_content(value, 'AU')
            output_file.write(f"{key}: (GC content: {gc_content:.2f}%, AU content: {au_content:.2f}%)\n")
        else:
            at_content = calculate_content(value, 'AT')
            output_file.write(f"{key}: (GC content: {gc_content:.2f}%, AT content: {at_content:.2f}%)\n")

print(f"The GC, AT, and AU content for each sequence has been written to {output_file_path}")
