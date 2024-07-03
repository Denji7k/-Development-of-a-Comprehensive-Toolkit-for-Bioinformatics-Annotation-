def read_fasta(file_path):
    sequences = []
    Header = ''
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if Header:
                    sequences.append(Header.upper())
                Header = ''
            else:
                Header += line
        if Header:
            sequences.append(Header.upper())
    
    return sequences

def calculate_content(sequence, bases):
    count = sum(sequence.count(base) for base in bases)
    return round(float(count) / len(sequence) * 100, 2)

def get_bases(sequence):
    if 'U' in sequence:
        return 'AU'
    return 'AT'

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

sequences = read_fasta(input_file)

with open(output_file, 'w') as file:
    for index, sequence in enumerate(sequences, start=1):
        gc_content = calculate_content(sequence, 'GC')
        base_type = get_bases(sequence)
        if base_type == 'AU':
            au_content = calculate_content(sequence, 'AU')
            file.write(f"Sequence {index} \nGC content: {gc_content:.2f}%, AU content: {au_content:.2f}% \n")
        else:
            at_content = calculate_content(sequence, 'AT')
            file.write(f"Sequence {index} \nGC content: {gc_content:.2f}%, AT content: {at_content:.2f}% \n")

print(f"The GC, AT, and AU content for each sequence has been written to {output_file}")
