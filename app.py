import streamlit as st
from itinerary_generator import generate_itinerary

st.set_page_config(page_title="AI Travel Guide", page_icon="✈️")

st.title("🌍 AI Travel Guide")
st.subheader("Plan your trip in seconds")

destination = st.text_input("📍 Enter Destination", placeholder="Example: Mysore")

days = st.number_input("🗓 Number of Days", min_value=1, max_value=15, step=1)

nights = st.number_input("🌙 Number of Nights", min_value=1, max_value=15, step=1)

interests = st.text_input("🎯 Interests", placeholder="food, nature, history")

if st.button("Generate Itinerary 🚀"):
    if destination and interests:
        result = generate_itinerary(destination, days, nights, interests)
        st.success("Itinerary Generated Successfully!")
        st.text(result)
    else:
        st.warning("Please fill all fields.")