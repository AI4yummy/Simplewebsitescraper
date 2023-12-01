from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# Find all h4 tags with the specified class
listing = soup.find_all(class_='caption')

texts = []
# Extract text from each element
for listing in listings:
    text = listing.get_text()
    texts.append(text)
    print(f"Extracted Text: {text}")

if not texts:
    print("No elements found.")

