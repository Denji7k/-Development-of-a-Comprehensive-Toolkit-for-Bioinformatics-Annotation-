rna_codon = {
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
    "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

def translate_rna_to_protein(rna_str):
    protein_str = ''.join(rna_codon[rna_str[i:i+3]] for i in range(0, len(rna_str), 3) if rna_str[i:i+3] in rna_codon and rna_codon[rna_str[i:i+3]] != "*")
    return protein_str

def translate_fasta_to_rna(input_file, output_file):
    with open(input_file, 'r') as file:
        sequences = {}
        current_seq_id = ''
        current_sequence = ''

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_seq_id:
                    sequences[current_seq_id] = current_sequence.replace('T', 'U')
                current_seq_id = line[1:]
                current_sequence = ''
            else:
                current_sequence += line

        if current_seq_id:
            sequences[current_seq_id] = current_sequence.replace('T', 'U')

    with open(output_file, 'w') as protein_file:
        for seq_id, rna_seq in sequences.items():
            protein_seq = translate_rna_to_protein(rna_seq)
            protein_file.write(f">{seq_id}\n{protein_seq}\n")

# Input file names directly in the script
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"


translate_fasta_to_rna(input_file, output_file)
print(f"Protein sequences have been written to '{output_file}'.")
