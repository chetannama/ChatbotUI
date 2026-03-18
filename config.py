import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

if not isinstance(OPENAI_API_KEY, str):
    raise ValueError("OPENAI_API_KEY must be a string")

#DB_URI = "mssql+pyodbc://TripOrganiser:Chetan%40123@localhost/TripOrganiserBackend?driver=ODBC+Driver+17+for+SQL+Server"


# Paths
DATA_FOLDER = "data/"
GRAPH_FOLDER = "graphs/"
