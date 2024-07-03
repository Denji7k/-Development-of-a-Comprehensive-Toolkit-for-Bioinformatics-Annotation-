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

Nucleotides = ("A", "C", "G", "T")

def validate(dna_sequence):
    tmpdna = dna_sequence.upper()
    for i in tmpdna:
        if i not in Nucleotides:
            return False
    return tmpdna

def countfreq(dna_sequence):
    tmpfreq = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in dna_sequence.upper():
        tmpfreq[i] += 1
    return tmpfreq

sequence = input("Enter the input file:").strip()
sequences = read_fasta(sequence)

output_file = input("Enter the output file for the sequences to be stored:").strip() or f"{sequence}_output.txt"

with open(output_file, 'w') as output_file:
    for seq_num, dna_sequence in enumerate(sequences, start=1):
        is_valid = validate(dna_sequence)
        frequency = countfreq(dna_sequence)
        output_file.write(f"Sequence {seq_num}:\n")
        output_file.write(f"Valid: {is_valid}\n")
        output_file.write(f"Length: {len(dna_sequence)}\n")
        output_file.write(f"Nucleotide frequency: {frequency}\n\n")

print("Processing complete.")
