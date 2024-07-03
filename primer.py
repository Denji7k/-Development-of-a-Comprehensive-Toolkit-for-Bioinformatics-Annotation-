import re

def complement(seq):
    return seq.translate(str.maketrans('ATGC', 'TACG'))

def reverse_complement(seq):
    return complement(seq)[::-1]

def gc_content(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    total_count = len(seq)
    return (g_count + c_count) / total_count * 100 if total_count > 0 else 0

def melting_temperature(seq):
    # Tm = 2 * (A + T) + 4 * (G + C)
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    return 2 * (a_count + t_count) + 4 * (g_count + c_count)

def design_primers(dna_sequence):
    dna_sequence = re.sub(r'[^ATGC]', '', dna_sequence.upper())
    forward_primer = dna_sequence[:20]
    reverse_primer = reverse_complement(dna_sequence[-20:])
    
    # Calculate GC content and Tm for both primers
    forward_gc = gc_content(forward_primer)
    reverse_gc = gc_content(reverse_primer)
    forward_tm = melting_temperature(forward_primer)
    reverse_tm = melting_temperature(reverse_primer)
    
    return (
        forward_primer, forward_gc, forward_tm,
        reverse_primer, reverse_gc, reverse_tm
    )

def process_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        sequences = {}
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                seq_id = line[1:]
                sequences[seq_id] = ''
            else:
                sequences[seq_id] += line
        
        for seq_id, sequence in sequences.items():
            (
                forward_primer, forward_gc, forward_tm,
                reverse_primer, reverse_gc, reverse_tm
            ) = design_primers(sequence)
            outfile.write(f">{seq_id}\n"
                          f"Forward Primer: {forward_primer}\n"
                          f"Forward GC Content: {forward_gc:.2f}%\n"
                          f"Forward Tm: {forward_tm:.2f}°C\n"
                          f"Reverse Primer: {reverse_primer}\n"
                          f"Reverse GC Content: {reverse_gc:.2f}%\n"
                          f"Reverse Tm: {reverse_tm:.2f}°C\n")

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"


process_fasta(input_file, output_file)
print(f"Primers and their properties have been written to '{output_file}'.")

output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"


process_fasta(input_file, output_file)
print(f"Primers and their properties have been written to '{output_file}'.")
