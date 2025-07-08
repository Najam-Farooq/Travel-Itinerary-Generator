import streamlit as st
import requests

st.set_page_config(page_title="Travel Itinerary Generator", layout="centered")
st.title("Personalized Travel Itinerary Generator")

st.header("Generate a New Itinerary")
destination = st.text_input("Destination (e.g., Paris)", placeholder="Enter a city")
budget = st.number_input("Budget ($)", min_value=0.0, step=50.0, value=1000.0)
duration = st.number_input("Trip Duration (days)", min_value=1, step=1, value=3)

if st.button("Generate Itinerary"):
    if destination.strip() == "":
        st.error("Please enter a valid destination.")
    else:
        payload = {
            "destination": destination,
            "budget": budget,
            "duration": duration
        }
        try:
            response = requests.post("http://localhost:8001/generate_itinerary", json=payload)
            print(response.json())
            response.raise_for_status()
            result = response.json()
            st.success(result["message"])
            st.write("**Itinerary**:")
            st.markdown(result["itinerary"])
            st.write(f"**Trip ID**: {result['thread_id']} (Save this to retrieve your itinerary later)")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")

st.header("Retrieve a Saved Itinerary")
thread_id = st.text_input("Enter Trip ID", placeholder="e.g., 629fce12-86d7-4a22-adf1-10adbeacfd2d")
if st.button("Retrieve Itinerary"):
    if thread_id.strip() == "":
        st.error("Please enter a valid Trip ID.")
    else:
        try:
            response = requests.post("http://localhost:8001/get_itinerary", json={"thread_id": thread_id})
            print(response.json())
            response.raise_for_status()
            result = response.json()
            st.success(result["message"])
            st.write("**Itinerary**:")
            st.markdown(result["itinerary"])
            st.write(f"**Details**: {result['destination']}, ${result['budget']}, {result['duration']} days")
        except requests.exceptions.RequestException as e:
            st.error(f"Error retrieving itinerary: {e}")