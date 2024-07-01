import math

def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as f:
        header = None
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences[header] = sequence
                header = line[1:]
                sequence = ''
            else:
                sequence += line
        if header:
            sequences[header] = sequence
    return sequences

def calculate_tm(primer):
    tm_values = {'AA': 2.0, 'TT': 2.0, 'AT': 2.0, 'TA': 2.0,
                 'CA': 4.0, 'TG': 4.0, 'GT': 4.0, 'AC': 4.0,
                 'CT': 4.0, 'AG': 4.0, 'GA': 4.0, 'TC': 4.0,
                 'CG': 4.0, 'GC': 4.0, 'GG': 4.0, 'CC': 4.0}
    
    return sum(tm_values.get(primer[i:i+2], 0) for i in range(len(primer) - 1))

def calculate_annealing_temp(tm):
    return tm - 5.0

def find_primers_and_tm(sequence):
    forward_primer = sequence[:20]
    reverse_primer = sequence[-20:]
    tm_forward = calculate_tm(forward_primer)
    tm_reverse = calculate_tm(reverse_primer)
    ta_forward = calculate_annealing_temp(tm_forward)
    ta_reverse = calculate_annealing_temp(tm_reverse)
    return forward_primer, tm_forward, ta_forward, reverse_primer, tm_reverse, ta_reverse

def write_results(output_file, sequences):
    with open(output_file, 'w') as f:
        for header, sequence in sequences.items():
            forward_primer, tm_forward, ta_forward, reverse_primer, tm_reverse, ta_reverse = find_primers_and_tm(sequence)
            f.write(f"{header}\n")
            f.write(f"Forward Primer: {forward_primer}\n")
            f.write(f"Tm (Forward Primer): {tm_forward:.2f}*C\n")
            f.write(f"Annealing Temp (Forward Primer): {ta_forward:.2f}*C\n")
            f.write(f"Reverse Primer: {reverse_primer}\n")
            f.write(f"Tm (Reverse Primer): {tm_reverse:.2f}*C\n")
            f.write(f"Annealing Temp (Reverse Primer): {ta_reverse:.2f}C\n\n")


input_file = input("Enter the input FASTA file name: ").strip()
output_file = input("Enter the output file name to store translated sequences: ").strip() or f"{input_file}_output.txt"


sequences = read_fasta(input_file)
write_results(output_file, sequences)

print(f"Results have been written to {output_file}.")
