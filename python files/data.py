import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.lonelyplanet.com/vietnam/hanoi/attractions/temple-of-literature/a/poi-sig/1113735/357880"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the <div> element with the specified class name
div_element = soup.find("div", class_="readMore_content___5EuR")

# Extract the content within the <div> element and split it into sentences
content = div_element.get_text(strip=True)
sentences = content.split(".")

# Save the sentences into a text file
with open("scraped_content.txt", "w") as file:
    for sentence in sentences:
        file.write(sentence.strip() + ".\n")





