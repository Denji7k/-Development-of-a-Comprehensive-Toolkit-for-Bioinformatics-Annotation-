def read_fasta(file_path):
    """Reads sequences from a FASTA file."""
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

def length_check(seq1, seq2):
    """Checks if the lengths of two sequences are equal."""
    return len(seq1) == len(seq2)

def find_matching_segments(seq1, seq2):
    """Finds matching segments between two sequences."""
    return ''.join(a if a == b else '*' for a, b in zip(seq1, seq2))

def calculate_similarity_percentage(seq1, seq2):
    """Calculates the percentage similarity between two sequences."""
    matches = sum(a == b for a, b in zip(seq1, seq2))
    return (matches / len(seq1)) * 100

file1_path = input("Enter the path for the first FASTA file: ").strip()
file2_path = input("Enter the path for the second FASTA file: ").strip()
output_file = input("Enter the path for the output file (default: comparison_output.txt): ").strip()

if not output_file:
    output_file = 'comparison_output.txt'


sequences1 = read_fasta(file1_path)
sequences2 = read_fasta(file2_path)

if not sequences1 or not sequences2:
    raise ValueError("Both FASTA files must contain at least one sequence.")

with open(output_file, 'w') as f:
    for i, seq1 in enumerate(sequences1, 1):
        for j, seq2 in enumerate(sequences2, 1):
            f.write(f"Comparing Sequence {i} from file1 with Sequence {j} from file2:\n")
            f.write(f"Length check: {length_check(seq1, seq2)}\n")
            f.write(f"Matching segments: {find_matching_segments(seq1, seq2)}\n")
            f.write(f"Similarity percentage: {calculate_similarity_percentage(seq1, seq2):.2f}%\n\n")

print(f"Processing complete. Results saved to '{output_file}'.")
