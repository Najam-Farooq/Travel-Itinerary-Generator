from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Travel Itinerary Generator API")

# Define input data model
class TravelInput(BaseModel):
    destination: str
    budget: float
    duration: int

# Endpoint to generate itinerary (placeholder)
@app.post("/generate_itinerary")
async def generate_itinerary(travel_input: TravelInput):
    return {
        "message": f"Planning a {travel_input.duration}-day trip to {travel_input.destination} with a ${travel_input.budget} budget",
        "itinerary": "Placeholder itinerary: Visit main attractions and local restaurants."
    }