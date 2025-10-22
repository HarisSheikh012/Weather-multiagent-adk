from google.adk.agents import Agent
from .tool import say_hello

greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Handles simple greetings using the 'say_hello' tool.",
    instruction="""
        You are the Greeting Agent. 
        Your ONLY task is to provide a friendly greeting. 
        Use the 'say_hello' tool to generate the greeting.
        If the user provides their name, pass it to the tool. 
        Do not engage in any other conversation or tasks.
    """,
    tools=[say_hello],
)
