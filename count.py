def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence.upper())
                sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence.upper())
    return sequences

def calculate_percentages(sequence, chars):
    counts = {char: sequence.count(char) for char in chars}
    total_length = len(sequence)
    percentages = {char: (count / total_length * 100) for char, count in counts.items()}
    return counts, percentages

def write_content(file, sequences):
    for index, sequence in enumerate(sequences, start=1):
        if 'U' in sequence:  # RNA sequence
            chars = 'ACGU'
            counts, percentages = calculate_percentages(sequence, chars)
            file.write(f"Sequence {index} RNA Nucleotide Counts and Percentages:\n")
        elif set(sequence).issubset('ACGT'):  # DNA sequence
            chars = 'ACGT'
            counts, percentages = calculate_percentages(sequence, chars)
            file.write(f"Sequence {index} DNA Nucleotide Counts and Percentages:\n")
        elif set(sequence).issubset('ACDEFGHIKLMNPQRSTVWY'):  # Protein sequence
            chars = 'ACDEFGHIKLMNPQRSTVWY'
            counts, percentages = calculate_percentages(sequence, chars)
            file.write(f"Sequence {index} Protein Amino Acid Counts and Percentages:\n")
        else:
            file.write(f"Sequence {index} contains unknown characters.\n")
            continue
        
        for char, count in counts.items():
            file.write(f"{char}: {count} ({percentages[char]:.2f}%)\n")
        file.write("\n")

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

sequences = read_fasta(input_file)

with open(output_file, 'w') as file:
    write_content(file, sequences)

print(f"The content for each sequence has been written to {output_file}")
