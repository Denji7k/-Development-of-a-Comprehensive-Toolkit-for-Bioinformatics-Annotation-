from collections import defaultdict

def read_fasta(file_path):
    """Read a FASTA file and return a list of sequences."""
    with open(file_path, 'r') as file:
        sequences = []
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def find_motifs(sequences, min_length=6, max_length=12):
    """Find fixed-length motifs shared across all sequences for lengths from min_length to max_length."""
    all_shared_motifs = defaultdict(set)
    
    for motif_length in range(min_length, max_length + 1):
        motif_count = defaultdict(int)
        for seq in sequences:
            seen_motifs = set()
            for i in range(len(seq) - motif_length + 1):
                motif = seq[i:i + motif_length]
                if motif not in seen_motifs:
                    motif_count[motif] += 1
                    seen_motifs.add(motif)
        
        # Filter motifs that are found in all sequences
        shared_motifs = {motif for motif, count in motif_count.items() if count == len(sequences)}
        if shared_motifs:
            all_shared_motifs[motif_length] = shared_motifs
    
    return all_shared_motifs

def main():
    input_file = input("Enter the input file: ").strip()
    sequences = read_fasta(input_file)

    if len(sequences) < 2:
        raise ValueError("Error: The FASTA file must contain at least two sequences.")
    
    min_length = 6  # Define the minimum motif length
    max_length = 12  # Define the maximum motif length
    all_common_motifs = find_motifs(sequences, min_length, max_length)
    
    output_file = input("Enter the output file (leave blank to use input file name): ").strip()
    if not output_file:
        output_file = f"{input_file}_common_motifs.txt"

    with open(output_file, 'w') as out_file:
        for length, motifs in sorted(all_common_motifs.items()):
            out_file.write(f"Motifs of length {length}:\n")
            for motif in sorted(motifs):
                out_file.write(motif + '\n')
            out_file.write('\n')

    print("Processing complete.")

if __name__ == "__main__":
    main()
