from Bio.Blast import NCBIWWW

def run_blast(query_sequence_file, blast_type, db, output_file):
    # Read query sequence from file
    try:
        with open(query_sequence_file, 'r') as f:
            query_sequence = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{query_sequence_file}' not found.")
        return

    # Perform BLAST search
    try:
        result_handle = NCBIWWW.qblast(blast_type, db, query_sequence, format_type="xml")
    except ValueError as e:
        print(f"Error performing BLAST search: {e}")
        return

    # Save BLAST results to output file
    with open(output_file, 'w') as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()
    print(f"BLAST search completed successfully. Results saved to '{output_file}'.")

# Get user input for the query sequence file, type of BLAST search, database, and output file
query_sequence_file = "blast_sequence.txt".strip()
blast_type = input("Enter the type of BLAST search (blastn, blastp, blastx, tblastn, tblastx): ").strip()
db = input("Enter the BLAST database (e.g., nt, nr, refseq_rna, refseq_protein, swissprot, pdbaa, env_nt, env_nr): ").strip()
output_file = "output.txt".strip()

# Run the BLAST search
run_blast(query_sequence_file, blast_type, db, output_file)
