import requests
from bs4 import BeautifulSoup

# Send a GET request to the articles page
url = "https://www.lonelyplanet.com/vietnam/articles"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article links on the page
article_links = soup.find_all("a", class_="card-link")

# Open the output file in write mode
with open("scraped_links.txt", "w") as file:
    # Write each link to the file
    for link in article_links:
        article_url = link["href"]
        file.write(article_url + "\n")

print("Scraping complete. Links saved to 'scraped_links.txt'.")


