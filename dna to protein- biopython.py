from Bio.Seq import Seq

# Read the DNA sequence from the file
file_path = "dna_sequence.txt"
with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

# Create a Seq object from the DNA sequence
dna_seq = Seq(dna_sequence)

# Open output file for writing
output_file_path = "output.txt"
with open(output_file_path, 'w') as output_file:
    # Nucleotide sequences and (reverse) complements
    complementary_seq = dna_seq.complement()
    output_file.write(f"COMPLEMENTARY SEQ: {complementary_seq}\n")

    reverse_complementary_seq = dna_seq.reverse_complement()
    output_file.write(f"REVERSE COMPLEMENTARY SEQ: {reverse_complementary_seq}\n")

    reversed_seq = dna_seq[::-1]
    output_file.write(f"REVERSED SEQ: {reversed_seq}\n")

    # Transcription (DNA to RNA)
    rna_seq = dna_seq.transcribe()
    output_file.write(f"TRANSCRIPTION: {rna_seq}\n")

    # Translation (RNA to Protein)
    protein_seq = rna_seq.translate()
    output_file.write(f"TRANSLATION: {protein_seq}\n")

print(f"Output has been written to {output_file_path}")
