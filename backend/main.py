from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router

app = FastAPI(title="Toy Price Tracker API", description="API for tracking toy prices")

# Include API routes
app.include_router(router)

@app.get("/")
def home():
	return {"message": "Welcome to the Toy Price Tracker API"}

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
