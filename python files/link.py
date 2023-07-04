import requests
from bs4 import BeautifulSoup

#attractions = ["attractions", "restaurants", "entertainment", "nightlife", "shopping", "hotels"]
#for i in attractions:
keyword = "attractions"
city = "tay-ninh"

base_url = f"https://www.lonelyplanet.com/vietnam/around-ho-chi-minh-city/{city}/{keyword}?page="
num_pages = 3  # Number of pages to scrape

# Open a text file for writing
with open(f"links_{keyword}.txt", "w") as file:
    for page in range(1, num_pages + 1):
        url = base_url + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href and f"/vietnam/around-ho-chi-minh-city/{city}/{keyword}/" in href:
                file.write(href + "\n")