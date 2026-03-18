# from langchain_community.utilities import SQLDatabase
# from langchain_community.agent_toolkits import SQLDatabaseToolkit
# from agent.llm import get_llm
# from config import DB_URI

# def get_sql_tool():
#     db = SQLDatabase.from_uri(str(DB_URI))
#     toolkit = SQLDatabaseToolkit(
#         llm=get_llm(),
#         db=db
#     )
#     return toolkit.get_tools()