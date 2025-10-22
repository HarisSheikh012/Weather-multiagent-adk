from google.adk.agents import Agent
from .tool import get_weather
from .sub_agents.greetings.agent import greeting_agent
from .sub_agents.farewell.agent import farewell_agent
from .mcp_server.filesystem_server import filesystem_mcp_toolset


root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Weather Agent that also handles greetings, farewells, and file operations via MCP server.",
    instruction="""
        You are the main Weather Agent.
        - For weather questions, use the 'get_weather' tool.
        - For greetings like 'Hi' or 'Hello', delegate to 'greeting_agent'.
        - For farewells like 'Bye' or 'Goodbye', delegate to 'farewell_agent'.
        - For file operations like 'read', 'write', or 'list files', use the MCP tools.
        - Never delegate file-related requests to other agents.
    """,
    tools=[get_weather, filesystem_mcp_toolset],
    sub_agents=[greeting_agent, farewell_agent],
)
