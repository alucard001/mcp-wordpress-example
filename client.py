import asyncio
from fastmcp import Client

client = Client("server.py")

async def test_call_tool(name: str):
    async with client:
        # Call the 'greet' tool
        tool_result = await client.call_tool("greet", {"name": name})
        print(f"Tool Result: {tool_result}")

        # Call the 'personalized_greeting' prompt
        """
        So, the mcp.prompt itself doesn't directly interact with an LLM. Instead,
        it's designed to generate structured text or data that can be fed into an
        LLM as part of a larger prompt or context. It acts as a way to programmatically
        construct parts of the input that you would then send to an LLM for processing.
        This allows you to create dynamic and reusable prompt components within
        your MCP server.
        """
        prompt_result = await client.call_prompt("personalized_greeting", {"name": name})
        print(f"Prompt Result: {prompt_result}")

asyncio.run(test_call_tool("John"))