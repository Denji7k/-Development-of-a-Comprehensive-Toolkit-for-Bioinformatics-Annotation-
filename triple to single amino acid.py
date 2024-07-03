import os

def read_fasta(file_path):
    sequences = {}
    current_seq_id = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_seq_id = line[1:]
                sequences[current_seq_id] = ''
            else:
                sequences[current_seq_id] += line
    return sequences

def convert_to_triple_code(sequence: str) -> str:
    amino_acid_codes = {
        'Ala': 'A', 'Cys': 'C', 'Asp': 'D', 'Glu': 'E', 'Phe': 'F',
        'Gly': 'G', 'His': 'H', 'Ile': 'I', 'Lys': 'K', 'Leu': 'L',
        'Met': 'M', 'Asn': 'N', 'Pro': 'P', 'Gln': 'Q', 'Arg': 'R',
        'Ser': 'S', 'Thr': 'T', 'Val': 'V', 'Trp': 'W', 'Tyr': 'Y'
    }
    
    three_letter_sequence = []
    current_aa = ''
    
    i = 0
    while i < len(sequence):
        aa_found = False
        for aa in amino_acid_codes:
            if sequence[i:i+len(aa)] == aa:
                three_letter_sequence.append(amino_acid_codes[aa])
                i += len(aa)
                aa_found = True
                break
        if not aa_found:
            i += 1  # Move to the next character if no match is found
    
    return ''.join(three_letter_sequence)

input_file = input("Enter the input FASTA file name: ").strip()
output_file = input("Enter the output file name: ").strip() or f"{input_file}_output.txt"

if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found.")
else:
    sequences = read_fasta(input_file)
    with open(output_file, 'w') as f:
        for seq_id, sequence in sequences.items():
            f.write(f">{seq_id}\n{convert_to_triple_code(sequence)}\n")

    print(f"Converted sequences have been saved to '{output_file}'")
