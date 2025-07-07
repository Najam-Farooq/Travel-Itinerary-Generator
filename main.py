from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Travel Itinerary Generator API")

class TravelInput(BaseModel):
    destination: str = Field(..., min_length=1, description="City or destination")
    budget: float = Field(..., ge=0, description="Budget in USD")
    duration: int = Field(..., ge=1, description="Trip duration in days")

@app.post("/generate_itinerary")
async def generate_itinerary(travel_input: TravelInput):
    if not travel_input.destination.strip():
        raise HTTPException(status_code=400, detail="Destination cannot be empty")
    return {
        "message": f"Planning a {travel_input.duration}-day trip to {travel_input.destination} with a ${travel_input.budget} budget",
        "itinerary": "Placeholder itinerary: Visit main attractions and local restaurants."
    }