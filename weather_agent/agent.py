from google.adk.agents import Agent
from .tool import get_weather
from .sub_agents.greetings.agent import greeting_agent
from .sub_agents.farewell.agent import farewell_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Main coordinator agent that handles weather, greetings, and farewells.",
    instruction="""
        You are the main Weather Agent coordinating a team.
        - For weather requests (e.g., 'What's the weather in Paris?'), use the 'get_weather' tool.
        - For greetings (e.g., 'Hi', 'Hello'), delegate to 'greeting_agent'.
        - For farewells (e.g., 'Bye', 'See you'), delegate to 'farewell_agent'.
        - For anything else, politely respond that you can only handle greetings, farewells, or weather.
    """,
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent],
)
