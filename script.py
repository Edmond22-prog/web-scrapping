import requests
from bs4 import BeautifulSoup
import time


def track(url: str, page = 1):
    # Retrieve the page where we want to do Scrapping
    retrieve = requests.get(url+str(page))
    # Formatting of the resulting content
    formatter = BeautifulSoup(retrieve.content, "html.parser")
    # Take all the anime tags from the page
    formatted_content = formatter.find_all("article", class_="item se episodes")
    # Track of each tag
    for content in formatted_content:
       # Retrieve data of a tag
        data = content.find("div", class_="data")
        episode = data.find("a").get_text()
        publication = data.find("span").get_text()
        title = data.find("span", class_="serie").get_text()
        print(f"{episode}\n{publication}\n{title}\n")
        time.sleep(2)

       
URL_PAGE = "https://wwv.jetanimes.com/episodes/page/"

track(URL_PAGE)
print("You are actually on page 1")
while True:
    choice = input("Do you want to go to another page ? (y|n) : ")
    if choice in ("y", "Y", "yes", "YES"):
        while True:
            page = input("At which page do you want to go ?\nResponse: ")
            try:
                page = int(page)
            except:
                print("Please enter a number !")
            else:
                if page <= 1:
                    track(URL_PAGE)
                    print("You are actually on page 1")
                elif page > 412:
                    track(URL_PAGE, 412)
                    print("You are actually on page 412")
                else:
                    track(URL_PAGE, page)
                    print(f"You are actually on page {page}")
            break
    else:
        print("Close !")
        break
    


        
    


