import requests
from bs4 import BeautifulSoup

# Amazon search URL for Bearbrick 400% toys
scrape_url = "https://www.amazon.com/s?k=bearbrick+400%&ref=nb_sb_noss_2";

def scrape_bearbricks():
	print("Starting scraping bearbricks from Amazon")

	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
		"DNT": "1",  # Do Not Track
		"Connection": "keep-alive",
		"Upgrade-Insecure-Requests": "1",
		"Referer": "https://www.google.com/",
	}

	response = requests.get(scrape_url, headers=headers)

	if response.status_code != 200:
		print(f"Error: Failed to fetch data with status code {response.status_code}")
		return {"error": "Failed to fetch price data"}

	soup = BeautifulSoup(response.text, "html.parser")
	bearbricks = []

	items = soup.select(".s-result-item[data-asin]:not([data-asin=''])")

	for i, item in enumerate(items):
		title_element = item.select_one(".a-text-normal")
		price_element = item.select_one(".a-offscreen")
		rating_element = item.select_one(".a-icon-alt")
		reviews_element = item.select_one(".a-size-base.s-underline-text")
		
		# Extract ASIN and product URL
		asin = item.get("data-asin")	
		product_url = f"https://www.amazon.com/dp/{asin}"

		bearbrick = {
			"title": title_element.text.strip() if title_element else "No title",
			"price": price_element.text.strip() if price_element else "No price",
			"rating": rating_element.text.strip() if rating_element else "No rating",
			"reviews": reviews_element.text.strip() if reviews_element else "0",
			"asin": asin,
			"product_url": product_url,
		}

		print(f"Item {i+1} data: {bearbrick}")
		bearbricks.append(bearbrick)
	
	print(f"Scraping complete. Found {len(bearbricks)} bearbricks")
	return bearbricks

# Call the function when this script is run directly
if __name__ == "__main__":
	result = scrape_bearbricks()	
	print(f"Scraped {len(result)} bearbricks")
