import streamlit as st
import requests

st.set_page_config(page_title="Travel Itinerary Generator", layout="centered")
st.title("Personalized Travel Itinerary Generator")

st.header("Enter Your Trip Details.")
destination = st.text_input("Destination (e.g., Paris)", placeholder="Enter a city")
budget = st.number_input("Budget ($)", min_value=0.0, step=50.0, value=1000.0)
duration = st.number_input("Trip Duration (days)", min_value=1, step=1, value=3)

if st.button("Generate Itinerary"):
    if destination.strip() == "":
        st.error("Please enter a valid destination.")
    else:
        # Send request to FastAPI
        payload = {
            "destination": destination,
            "budget": budget,
            "duration": duration
        }
        try:
            response = requests.post("http://localhost:8001/generate_itinerary", json=payload)
            response.raise_for_status()  # Check for HTTP errors
            result = response.json()
            st.success(result["message"])
            st.write("**Itinerary**:")
            st.markdown(result["itinerary"])
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")