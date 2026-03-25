import re
from bs4 import BeautifulSoup
import cloudscraper
import csv
import time

URL = "https://zelda.fandom.com/wiki/Link"
OUTPUT_FILE = "Link_ZELDA_title.csv"

scraper = cloudscraper.create_scraper()

def fetch(url):
    try:
        time.sleep(1)  
        response = scraper.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("Request failed:", e)
        return None

def parse_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title_div = soup.find("div", {"data-source": "title"})
    if not title_div:
        print("No title section found")
        return ""
    value_div = title_div.find("div", class_="pi-data-value")
    if not value_div:
        print("No title value found")
        return ""
    return value_div.get_text(separator=", ", strip=True)

def clean_titles(raw_text):
    cleaned = re.sub(r"\[\s*,\s*\d+\s*,\s*\]", "", raw_text)

    parts = cleaned.split(",")

    titles = []
    for p in parts:
        p = p.strip()
        if p:
            titles.append(p)
    return titles

def save_to_csv(titles, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow(["Title"])  

        for t in titles:
            writer.writerow([t])  

if __name__ == "__main__":
    html = fetch(URL)
    if html:
        raw_title_text = parse_title(html)
        if raw_title_text:
            titles = clean_titles(raw_title_text)
            save_to_csv(titles, OUTPUT_FILE)
            print(f"Cleaned titles saved to {OUTPUT_FILE}")
        else:
            print("No title content extracted")
    else:
        print("Failed to fetch page")

