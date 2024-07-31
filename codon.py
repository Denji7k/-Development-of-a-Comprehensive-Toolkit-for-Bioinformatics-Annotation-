import matplotlib.pyplot as plt
import mplcursors

def read_fasta(file_path):
    sequences = []
    header = ''
    sequence = ''
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append((header, sequence))
                header = line[1:]  # Remove '>'
                sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append((header, sequence))
    
    return sequences

def calculate_content(sequence, bases):
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    count = sum(sequence.count(base) for base in bases)
    return round(float(count) / len(sequence) * 100, 2)

def get_bases(sequence):
    return 'AU' if 'U' in sequence else 'AT'

def is_valid_sequence(sequence):
    return all(base in 'ACGTU' for base in sequence)

def nucleotide_percentages(sequence):
    total = len(sequence)
    return {base: round(sequence.count(base) / total * 100, 2) for base in 'ACGTU'}

def plot_gc_content_distribution(gc_contents, gc_details, output_file):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot of GC content values
    scatter = ax.scatter(range(1, len(gc_contents) + 1), gc_contents, c='royalblue', s=50, edgecolor='black')

    # Adding hover annotations using mplcursors
    mplcursors.cursor(scatter, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(gc_details[sel.index])
    )
    
    ax.set_title('GC Content Distribution')
    ax.set_xlabel('Sequence Index')
    ax.set_ylabel('GC Content (%)')
    ax.grid(True)

    plt.savefig(output_file)
    plt.show()

# Simplified execution
input_file = input('Enter the Fasta File:')
output_file = f"{input_file}_gc_content_details.txt"
plot_file = f"{input_file}_gc_content_distribution.png"

sequences = read_fasta(input_file)

gc_contents = []
gc_details = []
results = []

for index, (header, sequence) in enumerate(sequences, start=1):
    if not is_valid_sequence(sequence):
        results.append(f"{header} contains invalid characters and will be skipped.\n")
        continue
    
    gc_content = calculate_content(sequence, 'GC')
    base_type = get_bases(sequence)
    nucleotide_percents = nucleotide_percentages(sequence)
    
    gc_contents.append(gc_content)
    gc_details.append(f"{header}\nGC content: {gc_content:.2f}%\nNucleotide percentages: {nucleotide_percents}")

    if base_type == 'AU':
        au_content = calculate_content(sequence, 'AU')
        results.append(f"{header}\nGC content: {gc_content:.2f}%, AU content: {au_content:.2f}%\nNucleotide percentages: {nucleotide_percents}\n")
    else:
        at_content = calculate_content(sequence, 'AT')
        results.append(f"{header}\nGC content: {gc_content:.2f}%, AT content: {at_content:.2f}%\nNucleotide percentages: {nucleotide_percents}\n")

with open(output_file, 'w') as file:
    file.writelines(results)

plot_gc_content_distribution(gc_contents, gc_details, plot_file)
print(f"The GC, AT, and AU content for each sequence has been written to {output_file}")
print(f"GC content distribution plot has been saved to {plot_file}")
