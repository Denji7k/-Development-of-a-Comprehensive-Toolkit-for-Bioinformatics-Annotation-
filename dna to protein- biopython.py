from Bio.Seq import Seq

file_path = "dna_sequence.txt"
with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

dna_seq = Seq(dna_sequence)

output_file_path = "output.txt"
with open(output_file_path, 'w') as output_file:
    complementary_seq = dna_seq.complement()
    output_file.write(f"COMPLEMENTARY SEQ: {complementary_seq}\n")

    reverse_complementary_seq = dna_seq.reverse_complement()
    output_file.write(f"REVERSE COMPLEMENTARY SEQ: {reverse_complementary_seq}\n")

    reversed_seq = dna_seq[::-1]
    output_file.write(f"REVERSED SEQ: {reversed_seq}\n")

    rna_seq = dna_seq.transcribe()
    output_file.write(f"TRANSCRIPTION: {rna_seq}\n")

    protein_seq = rna_seq.translate()
    output_file.write(f"TRANSLATION: {protein_seq}\n")

print(f"Output has been written to {output_file_path}")
