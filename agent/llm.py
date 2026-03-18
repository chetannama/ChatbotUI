from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY

load_dotenv()

#temperature=0 means it will not generate the bad output but less smart
#temperature=1 means it can generate the bad output but very smart or creative at the same time

def get_llm():
    # return ChatOpenAI(base_url="https://openrouter.ai/api/v1",
    #                 api_key=str(OPENAI_API_KEY),
    #                 temperature=0.6) model="gpt-4.1"

    return ChatOpenAI(model="gpt-4o-mini",
                    api_key=str(OPENAI_API_KEY),
                    temperature=0.6) 