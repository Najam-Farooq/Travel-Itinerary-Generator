import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sys
sys.path.insert(0, r"C:\Users\user\Desktop\Ai project")
import database
from database import save_itinerary, get_itinerary

print(f"Imported get_itinerary: {get_itinerary}")
print(f"database.py path: {database.__file__}")

app = FastAPI(title="Travel Itinerary Generator API")

class TravelInput(BaseModel):
    destination: str = Field(..., min_length=1, description="City or destination")
    budget: float = Field(..., ge=0, description="Budget in USD")
    duration: int = Field(..., ge=1, description="Trip duration in days")

class ThreadInput(BaseModel):
    thread_id: str = Field(..., min_length=1, description="Trip ID")

@app.post("/generate_itinerary")
async def generate_itinerary(travel_input: TravelInput):
    if not travel_input.destination.strip():
        raise HTTPException(status_code=400, detail="Destination cannot be empty")
    itinerary = "Placeholder itinerary: Visit main attractions and local restaurants."
    thread_id = save_itinerary(
        travel_input.destination,
        travel_input.budget,
        travel_input.duration,
        itinerary
    )
    if not thread_id:
        raise HTTPException(status_code=500, detail="Failed to save itinerary")
    return {
        "message": f"Planning a {travel_input.duration}-day trip to {travel_input.destination} with a ${travel_input.budget} budget",
        "itinerary": itinerary,
        "thread_id": thread_id
    }

@app.post("/get_itinerary")
async def get_itinerary(thread_input: ThreadInput):
    itinerary = database.get_itinerary(thread_input.thread_id)  # Direct call
    print(f"itinerary type: {type(itinerary)}")
    print(f"itinerary value: {itinerary}")
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return {
        "message": f"Retrieved itinerary for {itinerary['destination']}",
        "itinerary": itinerary['itinerary'],
        "thread_id": itinerary['thread_id'],
        "destination": itinerary['destination'],
        "budget": itinerary['budget'],
        "duration": itinerary['duration']
    }