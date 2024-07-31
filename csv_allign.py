import csv
from collections import defaultdict

# Prompt the user for input and output file paths
input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

# Create a defaultdict to store grouped IDs
grouped_ids = defaultdict(list)

# Read the input CSV file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:  # Ensure the row is not empty
            if len(row) < 2:
                print(f"Warning: Skipping row {row} as it does not have enough columns.")
                continue
            id, letter = row[0], row[1]  # Assuming CSV structure is ID, Letter
            grouped_ids[letter].append(id)

# Write the grouped IDs to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for letter, ids in grouped_ids.items():
        csvwriter.writerow([letter] + ids)

# Print a confirmation message
print(f'Grouped IDs have been written to {output_file}')
