def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence.upper())  # Convert to uppercase
                    sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence.upper())  # Append the last sequence
    return sequences

Nucleotides = ("A", "C", "G", "T")

def validate(dna_sequence):
    """Validates if a DNA sequence contains only valid nucleotides."""
    tmpdna = dna_sequence.upper()
    for i in tmpdna:
        if i not in Nucleotides:
            return False
    return tmpdna

def countfreq(dna_sequence):
    """Counts the frequency of each nucleotide in a DNA sequence."""
    tmpfreq = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in dna_sequence.upper():
        tmpfreq[i] += 1
    return tmpfreq

# Read DNA sequences from FASTA file
sequence = input("Enter the input file:")
sequences= read_fasta(sequence)

output_file = input("Entter the output file for the sequences to be stored:") or f"{sequence}_output.txt"

# Open output file to store results
with open(output_file, 'w') as output_file:
    for seq_num, dna_sequence in enumerate(sequences, start=1):
        # Validate sequence
        is_valid = validate(dna_sequence)
        
        # Count frequency
        frequency = countfreq(dna_sequence)
        
        # Write results to output file
        output_file.write(f"Sequence {seq_num}:\n")
        output_file.write(f"Valid: {is_valid}\n")
        output_file.write(f"Length: {len(dna_sequence)}\n")
        output_file.write(f"Nucleotide frequency: {frequency}\n\n")

print("Processing complete.")
