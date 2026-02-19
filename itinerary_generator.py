import random

def generate_itinerary(destination, days, nights, interests):

    activities = [
        "Visit famous tourist attractions",
        "Explore local markets",
        "Visit parks and gardens",
        "Try local food and restaurants",
        "Visit museums or historical places",
        "Enjoy evening sightseeing",
        "Shopping and leisure walk"
    ]

    travel_tips = [
        "Carry a water bottle and stay hydrated.",
        "Start sightseeing early to avoid crowds.",
        "Use local transport to save money.",
        "Keep some cash for small shops and markets."
    ]

    tip = random.choice(travel_tips)

    itinerary = f"""
AI TRAVEL GUIDE ✈️

Destination : {destination}
Duration    : {days} days / {nights} nights
Interests   : {interests}
"""

    for day in range(1, int(days) + 1):
        day_plan = random.sample(activities, 2)

        itinerary += f"""

Day {day}:
- {day_plan[0]}
- {day_plan[1]}
"""

    itinerary += f"""

Travel Tip:
{tip}
"""

    return itinerary
