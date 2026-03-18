from agent.main_agent import build_agent

agent = build_agent()
#MAX_HISTORY = 10
#Conversation Memory
message = []
config = {
    "configurable": {
        "thread_id": "user_1"
    }
}
while True:
    question = input("user: ")

#add user message
    message.append({
        "role": "user",
        "content": question
    })

    #full conversation history
    for step in agent.stream(
        {"messages":message},
        config=config,
        stream_mode="values"
    ):
        response=step["messages"][-1]
        print("AI :",response.content)
        #response[-1].pretty_print()




    #message = message[-MAX_HISTORY:]


# question = """
# How many tables are in TripOrganiserBackend?
# Also read 'data/weather.csv' and generate humidity with vertical comparison graph only?
# How many leave an employee can take in a year as per company policy ?
# Calculate 2*5*5-3?
# """

# for step in agent.stream(
#     {"messages": [{"role": "user", "content": question}]},
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

#asyncio.run(main())