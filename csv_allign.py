import csv
from collections import defaultdict

input_file = input("Enter the input file: ").strip()
output_file = input("Enter the output file (leave blank to use input file name): ").strip() or f"{input_file}_output.txt"

grouped_ids = defaultdict(list)

with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:
            if len(row) < 2:
                print(f"Warning: Skipping row {row} as it does not have enough columns.")
                continue
            id, letter = row[0], row[1]
            grouped_ids[letter].append(id)

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for letter, ids in grouped_ids.items():
        csvwriter.writerow([letter] + ids)

print(f'Grouped IDs have been written to {output_file}')
