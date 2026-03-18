from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import tool
from config import SERPAPI_API_KEY

serp = SerpAPIWrapper(
    serpapi_api_key = str(SERPAPI_API_KEY)
    )

@tool("SerpAPI", description="Use this tool to search the web using Google SERP API")
def SerpAPI(query: str) -> str:
    return serp.run(query)
