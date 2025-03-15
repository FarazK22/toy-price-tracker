from fastapi import APIRouter
from backend.scraper_service import scrape_toys

router = APIRouter()

@router.get("/scrape")
async def scrape():
	result = scrape_toys()
	return {"message": "Scraping completed", "data": result}
