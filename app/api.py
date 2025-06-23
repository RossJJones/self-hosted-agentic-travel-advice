from fastapi import FastAPI
from crew import TripCrew
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    origin: str
    cities: str
    date_range: str
    interests: str

@app.post("/")
def run_travel_advice(request: RequestBody):
    crew = TripCrew(
        request.origin,
        request.cities,
        request.date_range,
        request.interests
    )
    result = crew.run()
    return result