def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as f:
        header = None
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences[header] = sequence.upper()
                header, sequence = line[1:], ''
            else:
                sequence += line
        if header:
            sequences[header] = sequence.upper()
    return sequences

def transcribe(dna_sequence):
    return dna_sequence.replace('T', 'U')

def translate(rna_sequence):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    
    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        protein_sequence += codon_table.get(rna_sequence[i:i+3], '?')
    return protein_sequence

def generate_six_frames(dna_sequences):
    all_frames = {}
    for header, dna_sequence in dna_sequences.items():
        rna_sequence = transcribe(dna_sequence)
        revcomp_rna = transcribe(dna_sequence[::-1].translate(str.maketrans('ATCG', 'UAGC')))
        
        frames = {}
        frames['Forward Frame 1'] = translate(rna_sequence)
        frames['Forward Frame 2'] = translate(rna_sequence[1:])
        frames['Forward Frame 3'] = translate(rna_sequence[2:])
        frames['Reverse Frame 1'] = translate(revcomp_rna)
        frames['Reverse Frame 2'] = translate(revcomp_rna[1:])
        frames['Reverse Frame 3'] = translate(revcomp_rna[2:])
        
        all_frames[header] = frames
    
    return all_frames

def write_output(output_file, sequences_with_frames):
    with open(output_file, 'w') as f:
        for header, frames in sequences_with_frames.items():
            f.write(f"Header: {header}\n")
            for frame_name, sequence in frames.items():
                f.write(f"{frame_name}:\n{sequence}\n\n")

if __name__ == "__main__":
    input_file = input("Enter the input FASTA file name: ")
    output_file = input("Enter the output file name to store translated sequences: ") or f"{input_file}_output.txt"

    sequences = read_fasta(input_file)
    sequences_with_frames = generate_six_frames(sequences)
    write_output(output_file, sequences_with_frames)
    
    print(f"Translation results have been written to {output_file}.")
