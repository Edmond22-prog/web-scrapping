import requests
from bs4 import BeautifulSoup


# Retrieve the page where we want to do Scrapping
jetanime = requests.get("https://wwv.jetanimes.com/episodes/")

# Formatting of the resulting content
soup = BeautifulSoup(jetanime.content, "html.parser")

# Take all the anime tags from the page
animes = soup.find_all("article", class_="item se episodes")

# Track of each tag
for anime in animes:
    # Retrieve data of a tag
    data = anime.find("div", class_="data")
    episode = data.find("a").get_text()
    publication = data.find("span").get_text()
    title = data.find("span", class_="serie").get_text()
    print(f"{episode}\n{publication}\n{title}\n")
