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

def translate_dna_to_protein(dna_sequence):
    # Codon table for DNA to Protein translation
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W'
    }
    
    protein_sequence = []
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        protein_sequence.append(codon_table.get(codon, '?'))  # Use '?' for unknown codons

    return ''.join(protein_sequence)

input_file = input("Enter the input FASTA file name: ").strip()
output_file = input("Enter the output file name: ").strip() or f"{input_file}_output.txt"

if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found.")
else:
    sequences = read_fasta(input_file)
    with open(output_file, 'w') as f:
        for seq_id, sequence in sequences.items():
            f.write(f">{seq_id}\n{translate_dna_to_protein(sequence)}\n")

    print(f"Converted sequences have been saved to '{output_file}'")
