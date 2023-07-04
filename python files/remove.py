import string

def remove_special_chars(text):
    special_chars = "�"  # Include � in the list of special characters
    cleaned_text = ''.join(char for char in text if char not in special_chars)
    return cleaned_text

# Input and output file paths
input_file = "scraped_content.txt"
output_file = "new_content.txt"

# Read the input file
with open(input_file, "r") as file:
    text = file.read()

# Remove special characters
cleaned_text = remove_special_chars(text)

# Write the cleaned text to the output file
with open(output_file, "w") as file:
    file.write(cleaned_text)

print("Special characters removed and cleaned text saved to output file.")
