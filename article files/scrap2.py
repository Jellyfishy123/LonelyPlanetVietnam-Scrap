import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <p> elements on the page
    p_elements = soup.find_all("p")

    # Extract the text content from each <p> element
    sentences = [p.get_text(strip=True) for p in p_elements]

    # Return the scraped sentences
    return sentences

# Input and output file paths
input_file = "scraped_links.txt"
output_file = "articles.txt"

# Open the input file and read the links
with open(input_file, "r") as file:
    links = file.readlines()

# Loop through the links and scrape the content
with open(output_file, "w", encoding="utf-8") as file:
    for link in links:
        link = link.strip()  # Remove leading/trailing whitespaces or newline characters
        sentences = scrape_content(link)
        for sentence in sentences:
            file.write(sentence.strip() + ".\n")

print("Scraping complete. Content saved to output file.")

