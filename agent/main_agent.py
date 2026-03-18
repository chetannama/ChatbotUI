from langchain.agents import create_agent
from agent.llm import get_llm
from Tools.calculator_tool import calculator
from Tools.excel_tool import analyze_excel
from Tools.search_tool import SerpAPI
#from Tools.sql_tool import get_sql_tool
from agent.prompt import get_system_prompt
from Tools.wiki_tool import get_wiki
from Tools.rag_tool import rag_search
from langgraph.checkpoint.memory import MemorySaver

def build_agent():

    #sql_tools = get_sql_tool()
    
    memory = MemorySaver()
    
    wiki = get_wiki()

    system_prompt = get_system_prompt()

    all_tools = [calculator,wiki,SerpAPI,analyze_excel,rag_search]
    #+sql_tools

    agent = create_agent(
    model=get_llm(),
    tools =all_tools,
    system_prompt=system_prompt,
    checkpointer=memory
)
    return agent


