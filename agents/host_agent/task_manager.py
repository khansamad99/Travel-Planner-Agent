from common.a2a_client import call_agent

FLIGHT_URL = "http://localhost:8001/run"
HOTEL_URL = "http://localhost:8002/run"
ACTIVITIES_URL = "http://localhost:8003/run"

async def run(payload):
    # 👀 Print what the host agent is sending
    print("🚀 Incoming payload:", payload)

    flights = await call_agent(FLIGHT_URL, payload)
    hotel = await call_agent(HOTEL_URL, payload)
    activities = await call_agent(ACTIVITIES_URL, payload)

    # 🧾 Log outputs
    print("📦 flights:", flights)
    print("📦 hotel:", hotel)
    print("📦 activities:", activities)

    # 🛡 Ensure all are dicts before access
    flights = flights if isinstance(flights, dict) else {}
    hotel = hotel if isinstance(hotel, dict) else {}
    activities = activities if isinstance(activities, dict) else {}

    return {
        "flights": flights.get("flights", "No flights returned."),
        "stay": hotel.get("stays", "No stay options returned."),
        "activities": activities.get("activities", "No activities found.")
    }