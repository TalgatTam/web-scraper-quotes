import requests
from bs4 import BeautifulSoup
import json

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote_block in soup.select(".quote"):
    text = quote_block.find("span", class_="text").get_text()
    author = quote_block.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in quote_block.select(".tags .tag")]

    quotes.append({
        "text": text,
        "author": author,
        "tags": tags
    })

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=4)

print("Quotes saved to quotes.json")
