try:
    # Define molecular weights for nucleotides and phosphates
    weights = {'A': 331.2, 'U': 307.2, 'G': 347.2, 'C': 307.2, 'T': 322.2}
    phosphates = {'ssrna': 18.02, 'ssdna': 79.0, 'dsdna': 158.0}

# input FASTA file path
    input_file_path = input("Enter the input file: ").strip()
    output_file_path = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file_path}_output.txt"


    # Prompt user to enter molecule type
    mol_type = input("Enter molecule type (ssRNA, ssDNA, dsDNA): ").strip().lower()

    # Validate molecule type input
    if mol_type not in ['ssrna', 'ssdna', 'dsdna']:
        raise ValueError("Invalid molecule type. Please enter 'ssRNA', 'ssDNA', or 'dsDNA'.")

    sequences = {}
    current_key = None

    # Parse sequences from the input FASTA file
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                sequences[current_key] += line

    sequence_weights = {}

    # Iterate over sequences and calculate weights
    for seq_id, sequence in sequences.items():
        seq_upper = sequence.upper()
        if (mol_type == 'ssrna' and 'U' not in seq_upper) or \
           (mol_type == 'ssdna' and 'T' not in seq_upper) or \
           (mol_type == 'dsdna' and ('T' not in seq_upper or 'U' in seq_upper)):
            print(f"Skipping sequence {seq_id}: Invalid sequence for {mol_type.upper()}.")
        else:
            # Calculate molecular weight
            weight = sum(weights.get(base, 0) for base in seq_upper) + phosphates[mol_type]
            weight = weight * 2 if mol_type == 'dsdna' else weight
            sequence_weights[seq_id] = weight

    # Write molecular weights to the output file
    with open(output_file_path, 'w') as f:
        for seq_id, weight in sequence_weights.items():
            f.write(f"Molecular weight of {seq_id}: {weight:.2f} g/mol\n")

    print(f"Molecular weights have been written to {output_file_path}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
