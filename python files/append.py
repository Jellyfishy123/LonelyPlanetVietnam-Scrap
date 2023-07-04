# Input and output file paths
keyword = "attractions"
input_file = f"links_{keyword}.txt"
output_file = f"links_{keyword}.txt"

# Open the input file and read the lines
with open(input_file, "r") as file:
    lines = file.readlines()

# Append the prefix to each line
modified_lines = [f"https://www.lonelyplanet.com/{line.strip()}\n" for line in lines]

# Write the modified lines to the output file
with open(output_file, "w") as file:
    file.writelines(modified_lines)

print("Prefix appended to each line. Result saved to output file.")
