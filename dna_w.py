def calculate_molecular_weight(sequence, mol_type, is_circular):
    # Define weights for each nucleotide (monomer)
    weights = {'A': 313.2, 'T': 304.2, 'G': 329.2, 'C': 289.2}  # DNA monomers
    weights_rna = {'A': 329.2, 'U': 306.2, 'G': 345.2, 'C': 305.2}  # RNA monomers
    
    # Define weight for phosphate groups
    phosphates = {'ssdna': 79.0, 'dsdna': 158.0}
    
    # Define average weight per base pair for dsDNA
    average_base_pair_weight = 618.0

    # Calculate weight based on molecule type
    if mol_type == 'ssdna':
        weight = sum(weights.get(base, 0) for base in sequence)
    elif mol_type == 'dsdna':
        num_base_pairs = len(sequence) // 2
        weight = num_base_pairs * average_base_pair_weight
    elif mol_type == 'ssrna':
        weight = sum(weights_rna.get(base, 0) for base in sequence)
    else:
        raise ValueError("Invalid molecule type. Please enter 'ssDNA', 'dsDNA', or 'ssRNA'.")

    # Add weight for phosphates
    if mol_type in phosphates:
        weight += phosphates.get(mol_type, 0) * (len(sequence) // (2 if mol_type == 'dsdna' else 1))

    # Add extra weight if the DNA is circular
    if is_circular and mol_type == 'ssdna':
        weight += phosphates.get('ssdna', 0)  # Circular ssDNA has additional phosphate weight

    return weight

try:
    input_file_path = input("Enter the input file: ").strip()
    output_file_path = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file_path}_output.txt"

    mol_type = input("Enter molecule type (ssDNA, dsDNA, ssRNA): ").strip().lower()
    is_circular = input("Are the sequences circular? (yes/no): ").strip().lower() == 'yes'

    if mol_type not in ['ssdna', 'dsdna', 'ssrna']:
        raise ValueError("Invalid molecule type. Please enter 'ssDNA', 'dsDNA', or 'ssRNA'.")

    sequences = {}
    current_key = None

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                sequences[current_key] = ''
            else:
                sequences[current_key] += line

    sequence_weights = {}

    for seq_id, sequence in sequences.items():
        seq_upper = sequence.upper()
        if mol_type == 'dsdna' and len(seq_upper) % 2 != 0:
            print(f"Skipping sequence {seq_id}: Invalid length for dsDNA.")
            continue

        weight = calculate_molecular_weight(seq_upper, mol_type, is_circular)
        sequence_weights[seq_id] = weight

    with open(output_file_path, 'w') as f:
        for seq_id, weight in sequence_weights.items():
            f.write(f"Molecular weight of {seq_id}: {weight:.2f} g/mol\n")

    print(f"Molecular weights have been written to {output_file_path}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
