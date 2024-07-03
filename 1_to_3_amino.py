def convert_to_triple_code(sequence: str) -> str:
    amino_acid_codes = {
        'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe',
        'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys', 'L': 'Leu',
        'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
        'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp', 'Y': 'Tyr'
    }
    return ' '.join(amino_acid_codes.get(aa, 'Unknown') for aa in sequence)

def convert_fasta_to_triple(input_file: str, output_file: str):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        seq_id, sequence = '', ''
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                if seq_id:
                    outfile.write(f">{seq_id}\n{convert_to_triple_code(sequence)}\n")
                seq_id, sequence = line[1:], ''
            else:
                sequence += line
        if seq_id:
            outfile.write(f">{seq_id}\n{convert_to_triple_code(sequence)}\n")

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

convert_fasta_to_triple(input_file, output_file)
print(f"Converted sequences have been written to '{output_file}'.")
