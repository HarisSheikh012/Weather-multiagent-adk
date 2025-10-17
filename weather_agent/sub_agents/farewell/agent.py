from google.adk.agents import Agent
from .tool import say_goodbye

farewell_agent = Agent(
    name="farewell_agent",
    model="gemini-2.0-flash",
    description="Handles simple farewells using the 'say_goodbye' tool.",
    instruction="""
        You are the Farewell Agent. 
        Your ONLY task is to provide a polite farewell. 
        Use the 'say_goodbye' tool when the user says 'bye', 'goodbye', or similar.
        Do not perform any other actions.
    """,
    tools=[say_goodbye],
)
