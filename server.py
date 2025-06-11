from fastmcp import FastMCP

# Server
mcp = FastMCP(
    name="My MCP Server",
    instructions="""
        This is a sample/local MCP server.
    """)

@mcp.tool(tags={"tool", "tool_1"})
def greet(name: str) -> str:
    return f"[MCP] Hello, {name}!"

@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}

@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    # The {user_id} in the URI is extracted and passed to this function
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"

@mcp.prompt
def personalized_greeting(name: str) -> str:
    """Generates a personalized greeting for the user."""
    return f"Hello, {name}! Welcome to the FastMCP example."

if __name__ == "__main__":
    mcp.run()