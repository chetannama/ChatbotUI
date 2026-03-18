from fastapi import FastAPI
from agent.main_agent import build_agent
from pydantic import BaseModel #Define model
from fastapi.middleware.cors import CORSMiddleware
#Initialize API
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Initilize Agent
agent = None

@app.on_event("startup")
def startup():
    global agent
    try:
        agent = build_agent()
        print("Agent initialized")
    except Exception as e:
        print("Agent failed:", e)

messages=[]

'''
BaseModel in Pydantic to define structured data models with validation, parsing, and serialization.
### Why it is used:
# BaseModel helps you:
#  Validate data automatically and Ensures fields have the correct type.
#  Parse input data and Converts raw input like strings, dicts, or JSON into Python objects
'''
#This is model
class Query(BaseModel):
    question:str

#Creates API endpoints
'''
@app.post(\"/chat\") is a decorator in frameworks like FastAPI.
### Why we use it\nIt tells the framework:
# - app = your FastAPI application\
#  .post(\"/chat\") = this function should handle HTTP POST requests sent to the /chat URL
'''
@app.post("/chat")
def Chat(query: Query,session_id:str):

    response_text = ""

    config = {"configurable": {"thread_id": session_id}}

    #add user message
    messages.append({
        "role": "user",
        "content": query.question
    })

    for step in agent.stream(
        {"messages": messages},
        config=config,
        stream_mode="values"
    ):
        #"messages" is a key and [-1] used after that denote that message is a list
        # and it means find the last element of list that key should be "message" in dictionary step 
        response = step["messages"][-1]
        response_text = response.content

    return response_text