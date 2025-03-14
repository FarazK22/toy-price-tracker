from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/prices")
def get_prices():
	return {"prices": [10, 20, 30]} # Dummy data

def scrape_prices(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	price = soup.find("span", class_="price").text
	return price

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)