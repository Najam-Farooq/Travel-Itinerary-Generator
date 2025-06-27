import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Travel Itinerary Generator", layout="centered")

# Main title
st.title("Personalized Travel Itinerary Generator")

# Input form
st.header("Enter Your Trip Details")
destination = st.text_input("Destination (e.g., Paris)", placeholder="Enter a city")
budget = st.number_input("Budget ($)", min_value=0.0, step=50.0, value=1000.0)
duration = st.number_input("Trip Duration (days)", min_value=1, step=1, value=3)

# Generate button
if st.button("Generate Itinerary"):
    if destination.strip() == "":
        st.error("Please enter a valid destination.")
    else:
        st.success(f"Planning a {duration}-day trip to {destination} with a ${budget} budget...")
        # Placeholder for itinerary (we’ll connect to backend later)
        st.write("Itinerary will appear here once backend is connected!")