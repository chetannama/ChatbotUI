from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

def get_wiki():
    return WikipediaQueryRun(
        api_wrapper = WikipediaAPIWrapper(
            top_k_results=1,       # fetch only 1 page
            doc_content_chars_max=1000,
            timeout=10   # seconds,
        )
    )
