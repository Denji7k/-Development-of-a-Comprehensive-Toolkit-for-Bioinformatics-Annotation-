from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

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
    return mt.Tm_NN(Seq(primer))

def calculate_annealing_temp(tm):
    return tm - 5.0

def check_range(value, min_value, max_value, name):
    if not (min_value <= value <= max_value):
        raise ValueError(f"{name} ({value:.2f}°C) is out of the allowed range ({min_value:.2f}°C to {max_value:.2f}°C)")

def find_primers_and_tm(sequence):
    forward_primer = sequence[:20]
    reverse_primer = sequence[-20:]
    tm_forward = calculate_tm(forward_primer)
    tm_reverse = calculate_tm(reverse_primer)
    ta_forward = calculate_annealing_temp(tm_forward)
    ta_reverse = calculate_annealing_temp(tm_reverse)
    
    # Define allowed ranges
    tm_min, tm_max = 50.0, 65.0
    ta_min, ta_max = tm_min - 5.0, tm_max - 2.0  # Annealing temperature range is usually 2°C to 5°C below Tm
    
    # Check Tm and Ta ranges
    check_range(tm_forward, tm_min, tm_max, "Tm (Forward Primer)")
    check_range(ta_forward, ta_min, ta_max, "Annealing Temp (Forward Primer)")
    check_range(tm_reverse, tm_min, tm_max, "Tm (Reverse Primer)")
    check_range(ta_reverse, ta_min, ta_max, "Annealing Temp (Reverse Primer)")
    
    return forward_primer, tm_forward, ta_forward, reverse_primer, tm_reverse, ta_reverse

def write_results(output_file, sequences):
    with open(output_file, 'w') as f:
        for header, sequence in sequences.items():
            try:
                forward_primer, tm_forward, ta_forward, reverse_primer, tm_reverse, ta_reverse = find_primers_and_tm(sequence)
                f.write(f"{header}\n")
                f.write(f"Forward Primer: {forward_primer}\n")
                f.write(f"Tm (Forward Primer): {tm_forward:.2f}°C\n")
                f.write(f"Annealing Temp (Forward Primer): {ta_forward:.2f}°C\n")
                f.write(f"Reverse Primer: {reverse_primer}\n")
                f.write(f"Tm (Reverse Primer): {tm_reverse:.2f}°C\n")
                f.write(f"Annealing Temp (Reverse Primer): {ta_reverse:.2f}°C\n\n")
            except ValueError as e:
                f.write(f"{header}\n")
                f.write(f"Error: {e}\n\n")

input_file = input("Enter the input FASTA file name: ").strip()
output_file = input("Enter the output file name to store translated sequences: ").strip() or f"{input_file}_output.txt"

sequences = read_fasta(input_file)
write_results(output_file, sequences)

print(f"Results have been written to {output_file}.")
