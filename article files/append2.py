input_file = "scraped_links.txt"
output_file = "scraped_links.txt"

# Open the input file for reading
with open(input_file, "r") as file:
    links = file.readlines()

# Append "https://www.lonelyplanet.com" to each link
modified_links = [f"https://www.lonelyplanet.com{link.strip()}\n" for link in links]

# Open the output file for writing
with open(output_file, "w") as file:
    file.writelines(modified_links)

print("Links modified and saved to 'modified_links.txt'.")
