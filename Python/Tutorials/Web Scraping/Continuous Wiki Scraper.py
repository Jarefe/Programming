import requests
from bs4 import BeautifulSoup
import random
import time


def scrapeWikiArticle(url: str, num: int):
    time.sleep(0.1)
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    # Get all links on page
    all_links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(all_links)
    link_to_scrape = None

    for link in all_links:
        # Check if 'href' attribute exists before trying to access it
        if 'href' not in link.attrs:
            continue  # Skip links without the 'href' attribute

        # Search for wiki articles specifically
        if link['href'].find("/wiki/") == -1:
            continue

        # Check if the link is an absolute URL
        if link['href'].startswith("http"):
            link_to_scrape = link
        else:
            # Otherwise, concatenate with the base URL
            link_to_scrape = link
            break

    if link_to_scrape and num != 0:
        next_url = link_to_scrape['href']
        # If it's a relative URL, append the base URL
        if not next_url.startswith("http"):
            next_url = "https://en.wikipedia.org" + next_url
        scrapeWikiArticle(next_url, num - 1)


scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping", 50)