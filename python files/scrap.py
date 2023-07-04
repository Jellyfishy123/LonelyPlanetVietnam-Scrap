import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the <div> element with the specified class name
    div_element = soup.find("div", class_="readMore_content___5EuR")

    # Extract the content within the <div> element and split it into sentences
    content = div_element.get_text(strip=True)
    sentences = content.split(".")

    # Return the scraped sentences
    return sentences
city = "Tay Ninh"
# Input and output file paths
input_file = f"./{city}/links.txt"
output_file = f"./{city}/tay-ninh.txt"

# Open the input file and read the links
with open(input_file, "r") as file:
    links = file.readlines()

with open(output_file, "w", encoding="utf-8") as file:
    for link in links:
        link = link.strip()  # Remove leading/trailing whitespaces or newline characters
        sentences = scrape_content(link)
        for sentence in sentences:
            file.write(sentence.strip() + ".\n")

print("Scraping complete. Content saved to output file.")
