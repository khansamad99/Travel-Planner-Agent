# ADK-Powered Travel Planner

A multi-agent travel planning application built with the Google Agent Development Kit (ADK), FastAPI, and Streamlit. This project demonstrates how to orchestrate multiple specialized agents (flights, hotels, activities) to collaboratively plan a trip for a user.

## Features
- **Multi-agent architecture**: Separate agents for flights, hotels, and activities, coordinated by a host agent
- **Streamlit UI**: User-friendly web interface for entering trip details and viewing results
- **FastAPI microservices**: Each agent runs as an independent FastAPI service
- **Agent-to-agent (A2A) communication**: Agents communicate via HTTP APIs

## Project Structure
```
travel_planner.py         # Streamlit UI entry point
requirements.txt         # Python dependencies
README.md                # Project documentation
agents/
  host_agent/            # Orchestrator agent
  flight_agent/          # Flight planning agent
  hotel_agent/           # Hotel/stay planning agent
  activities_agent/      # Activities planning agent
common/                  # Shared utilities (A2A client/server)
schemas/                 # Data schemas
```

## Setup Instructions

### 1. Clone the repository
```sh
git clone <your-repo-url>
cd travel_planner
```

### 2. Create and activate a virtual environment (recommended)
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Start the agent services (in separate terminals or as background processes)
```sh
uvicorn agents.host_agent.__main__:app --port 8000 &
uvicorn agents.flight_agent.__main__:app --port 8001 &
uvicorn agents.hotel_agent.__main__:app --port 8002 &
uvicorn agents.activities_agent.__main__:app --port 8003 &
```

### 5. Run the Streamlit UI
```sh
streamlit run travel_planner.py
```

Open your browser to [http://localhost:8501](http://localhost:8501) to use the app.

## Usage
1. Enter your origin, destination, travel dates, and budget in the Streamlit UI.
2. Click "Plan My Trip ✨".
3. View suggested flights, stays, and activities, all coordinated by the host agent.

## Troubleshooting
- **ModuleNotFoundError**: Ensure all dependencies are installed and you are running from the project root.
- **Port already in use**: Kill any processes using ports 8000-8003 (`lsof -ti:8000,8001,8002,8003 | xargs kill -9`).
- **Agent errors**: Check each agent's terminal for error logs.

## Requirements
- Python 3.10+
- macOS, Linux, or Windows

## Credits
- Built with [Google ADK](https://github.com/google/adk-python), FastAPI, and Streamlit.

---
© 2025 Your Name or Organization. All rights reserved.
