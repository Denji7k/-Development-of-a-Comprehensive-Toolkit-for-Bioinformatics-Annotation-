import re
import primer3

def reverse_complement(seq):
    return seq.translate(str.maketrans('ATGC', 'TACG'))[::-1]

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

def annealing_temperature(forward_tm, reverse_tm):
    # Average Tm of both primers
    return (forward_tm + reverse_tm) / 2

def design_primers(dna_sequence):
    # Predetermined parameters with relaxed ranges
    min_length = 13  # Original min_length - 5
    max_length = 30  # Original max_length + 5
    min_gc = 35       # Original min_gc - 5
    max_gc = 65       # Original max_gc + 5
    min_tm = 45       # Original min_tm - 5
    max_tm = 65       # Original max_tm + 5
    min_product_size = 80  # Original min_product_size - 10
    max_product_size = 1500 # Original max_product_size + 10
    
    # Use Primer3 for primer design
    primer_results = primer3.bindings.designPrimers(
        {
            'SEQUENCE_ID': '1',
            'SEQUENCE_TEMPLATE': dna_sequence
        },
        {
            'PRIMER_PRODUCT_SIZE_RANGE': [[min_product_size, max_product_size]],
            'PRIMER_MIN_SIZE': min_length,
            'PRIMER_MAX_SIZE': max_length,
            'PRIMER_MIN_TM': min_tm,
            'PRIMER_MAX_TM': max_tm
        }
    )
    
    forward_primer = primer_results['PRIMER_LEFT_0_SEQUENCE']
    reverse_primer = primer_results['PRIMER_RIGHT_0_SEQUENCE']
    
    # Reverse complement the reverse primer
    reverse_primer = reverse_complement(reverse_primer)
    
    # Calculate GC content and Tm for both primers
    forward_gc = gc_content(forward_primer)
    reverse_gc = gc_content(reverse_primer)
    forward_tm = melting_temperature(forward_primer)
    reverse_tm = melting_temperature(reverse_primer)
    
    # Calculate annealing temperature
    annealing_temp = annealing_temperature(forward_tm, reverse_tm)
    
    # Check if the primers fall within the specified GC, Tm, and annealing temperature ranges
    errors = []
    
    if not (min_gc <= forward_gc <= max_gc):
        errors.append(f"Forward primer GC content out of range: {forward_gc:.2f}% (should be between {min_gc}-{max_gc}%)")
    
    if not (min_gc <= reverse_gc <= max_gc):
        errors.append(f"Reverse primer GC content out of range: {reverse_gc:.2f}% (should be between {min_gc}-{max_gc}%)")
    
    if not (min_tm <= forward_tm <= max_tm):
        errors.append(f"Forward primer Tm out of range: {forward_tm:.2f}°C (should be between {min_tm}-{max_tm}°C)")
    
    if not (min_tm <= reverse_tm <= max_tm):
        errors.append(f"Reverse primer Tm out of range: {reverse_tm:.2f}°C (should be between {min_tm}-{max_tm}°C)")
    
    if not (min_length <= len(forward_primer) <= max_length):
        errors.append(f"Forward primer length out of range: {len(forward_primer)} (should be between {min_length}-{max_length})")
    
    if not (min_length <= len(reverse_primer) <= max_length):
        errors.append(f"Reverse primer length out of range: {len(reverse_primer)} (should be between {min_length}-{max_length})")
    
    if not (min_product_size <= len(dna_sequence) <= max_product_size):
        errors.append(f"Product size out of range: {len(dna_sequence)} (should be between {min_product_size}-{max_product_size})")
    
    if errors:
        return None, errors  # Primers are not suitable, return errors
    
    return (
        forward_primer, forward_gc, forward_tm,
        reverse_primer, reverse_gc, reverse_tm,
        annealing_temp
    ), errors

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
            result, errors = design_primers(sequence)
            if result:
                (
                    forward_primer, forward_gc, forward_tm,
                    reverse_primer, reverse_gc, reverse_tm,
                    annealing_temp
                ) = result
                outfile.write(f">{seq_id}\n"
                              f"Forward Primer: {forward_primer}\n"
                              f"Forward GC Content: {forward_gc:.2f}%\n"
                              f"Forward Tm: {forward_tm:.2f}°C\n"
                              f"Reverse Primer: {reverse_primer}\n"
                              f"Reverse GC Content: {reverse_gc:.2f}%\n"
                              f"Reverse Tm: {reverse_tm:.2f}°C\n"
                              f"Annealing Temperature: {annealing_temp:.2f}°C\n")
            else:
                outfile.write(f">{seq_id}\nNo suitable primers found based on the specified ranges.\n")
                for error in errors:
                    outfile.write(f"  Error: {error}\n")

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

process_fasta(input_file, output_file)
print(f"Primers and their properties have been written to '{output_file}'.")
