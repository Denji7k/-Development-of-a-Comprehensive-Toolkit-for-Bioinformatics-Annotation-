def read_fasta(file_path):
    sequences = {}
    key = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                key = line[1:]
                sequences[key] = ''
            elif key:
                sequences[key] += line
    return sequences


def parse_fasta(fasta_data):
    sequences = {}
    for key, value in fasta_data.iteritems():
        sequences[key] = value.strip()
    return sequences

def transcribe_translate(dna_sequence, introns):
    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, '')

    rna_sequence = dna_sequence.replace('T', 'U')

    protein_sequence = ''
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
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G" }

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == "STOP":
            break  # Stop translating at stop codon
        protein_sequence += amino_acid

    return protein_sequence

def get_protein_sequences(fasta_data):
    parsed_fa = parse_fasta(fasta_data)
    dna_sequences = list(parsed_fa.values())
    introns = dna_sequences[1:]

    protein_sequences = {}
    for key, dna_sequence in parsed_fa.items():
        protein_sequences[key] = transcribe_translate(dna_sequence, introns)

    return protein_sequences

file_path = 'fasta_sequence.txt'
dna_sequences = read_fasta(file_path)
protein_sequences = get_protein_sequences(dna_sequences)

for key, protein_sequence in protein_sequences.iteritems():
    print('{0}: {1}'.format(key, protein_sequence))



















