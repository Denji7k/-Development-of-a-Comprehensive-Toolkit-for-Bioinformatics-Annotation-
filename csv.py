def read_csv(file_name):
    with open(file_name, 'r') as f:
        next(f)
        return [(int(line.split(',')[0]), line.split(',')[1].strip()) for line in f]

input_file1 = input("Enter the first CSV file name: ").strip()
input_file2 = input("Enter the second CSV file name: ").strip()

seq1 = read_csv(input_file1)
seq2 = read_csv(input_file2)

out1_file = 'out_1.txt'
out2_file1 = f'out_2_{input_file1}'
out2_file2 = f'out_2_{input_file2}'

with open(out1_file, 'w') as out1, \
     open(out2_file1, 'w') as out2_1, \
     open(out2_file2, 'w') as out2_2:
    for (pos1, res1), (pos2, res2) in zip(seq1, seq2):
        if res1 == res2:
            out1.write(f"{pos1},{res1}\n")
        else:
            out2_1.write(f"{pos1},{res1}\n")
            out2_2.write(f"{pos2},{res2}\n")

print("Processing complete.")
