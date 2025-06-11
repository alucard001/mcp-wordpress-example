# MCP + Wordpress Example
How to use FastMCP as a gateway to Wordpress REST API

## Notes

This is for demo and testing purpose only.  And the code here is for my reference purpose.

## Current Setup
- Python=3.12
- [`uv`](https://github.com/astral-sh/uv) under Windows

## About `mcp-sample.json` / `mcp-sample-remote.json`

This file is a sample configuration for FastMCP. It defines the tools and prompts that are available to the MCP server.
It is used to initialize the MCP server and I add it to my IDE as MCP server settings.

- `mcp-sample.json`: For local MCP server
- `mcp-sample-remote.json`: For remote MCP server

## Files

### `server.py`
This file defines the FastMCP server. It includes:
- An `mcp.tool` named `greet` that takes a `name` and returns a personalized greeting.
- An `mcp.prompt` named `personalized_greeting` that generates a greeting string, intended for use as context for an LLM.
- The main entry point to run the MCP server.

### `client.py`
This file demonstrates how to interact with the FastMCP server. It includes:
- An asynchronous function `test_call_tool` that uses the `fastmcp.Client` to:
  - Call the `greet` tool with a name.
  - Call the `personalized_greeting` prompt with a name.
- Prints the results from both the tool and the prompt calls.
