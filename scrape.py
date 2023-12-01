from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# Find all h4 tags with the specified class
price_elements = soup.find_all(class_='float-end price card-title pull-right')
miners = soup.find_all(class_='caption')
tile = soup.find_all(class_='title')

texts = []
# Extract text from each element
for miner in miners:
    text = miner.get_text()
    texts.append(text)
    print(f"Extracted Text: {text}")

if not texts:
    print("No elements found.")
