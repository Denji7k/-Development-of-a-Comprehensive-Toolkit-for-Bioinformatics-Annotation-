def translate_rna_to_protein(rna_sequence):
    codon_table = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
        "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
        "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }

    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == "STOP":
            break
        protein_sequence += amino_acid

    return protein_sequence

# Prompt user for input and output file paths
input_file = input("Enter the path to the input FASTA file: ")
output_file = input("Enter the path to the output file: ") or f"{input_file}_output.txt"

# Read the FASTA file
sequences = {}
with open(input_file, 'r') as file:
    key = None
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            key = line[1:]
            sequences[key] = ''
        elif key:
            sequences[key] += line

# Translate RNA to protein
protein_sequences = {key: translate_rna_to_protein(seq) for key, seq in sequences.items()}

# Write the protein sequences to the output file
with open(output_file, 'w') as file:
    for key, protein_sequence in protein_sequences.items():
        file.write(f'{key}: \n {protein_sequence}\n')

print(f"Protein sequences have been written to {output_file}.")
