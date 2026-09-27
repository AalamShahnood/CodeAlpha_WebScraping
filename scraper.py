import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://quotes.toscrape.com"

quotes_data = []


for page in range(1, 11):

    url = f"{base_url}/page/{page}/"

    print("Scraping:", url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find(
            "span",
            class_="text"
        ).get_text(strip=True)

        author = quote.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        tags = quote.find_all(
            "a",
            class_="tag"
        )

        tag_list = [
            tag.get_text(strip=True)
            for tag in tags
        ]

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tag_list)
        })


df = pd.DataFrame(quotes_data)

df.to_csv(
    "quotes_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)


print("\nScraping completed!")
print("Total records:", len(df))
print("\nDataset preview:")
print(df.head())