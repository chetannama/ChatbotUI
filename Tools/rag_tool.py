from langchain.tools import tool
from rag.retriever import retriever_doc

@tool
def rag_search(query:str) -> str:
    """
        Use this tool to answer questions about internal company knowledge.
    """
    context = retriever_doc(query)

    return context