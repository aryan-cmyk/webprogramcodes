input_file = input("Enter input filename: ")
output_file = input("Enter output filename: ")

with open(input_file, 'r') as file:
    lines = file.readlines()

cleaned_lines = []
for line in lines:
    cleaned_lines.append(line.strip())

cleaned_lines.sort()

with open(output_file, 'w') as file:
    for line in cleaned_lines:
        file.write(line + '\n')

print("Sorted content saved to", output_file)
