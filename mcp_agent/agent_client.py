import os
from smolagents import OpenAIServerModel, CodeAgent, MCPClient

# ---------- MCP Client ----------
mcp_client = MCPClient(
    {
        "url": "http://localhost:7860/gradio_api/mcp/sse",
        "transport": "sse",
    }
)

tools = mcp_client.get_tools()

# ---------- Ollama Model ----------
# Connects to Ollama's local OpenAI-compatible endpoint
model = OpenAIServerModel(
    # qwen2.5-coder is highly recommended for CodeAgents, but you can use llama3.2
    model_id="qwen2.5-coder", 
    api_base="http://localhost:11434/v1",
    api_key="ollama", # Required by the client structure, but ignored by Ollama
)

# ---------- Agent ----------
agent = CodeAgent(
    tools=[*tools],
    model=model,
    max_steps=3,
    instructions="""
You are an AI assistant analyzing product reviews.

You have access to tools:
- summarize_tool → for summaries
- sentiment_tool → for sentiment

Rules:
- Use tools when relevant
- Do NOT always call both
- Choose based on user intent
- Be concise
"""
)

# ---------- Chat Loop ----------
print("\nAgent is ready! (Type 'exit' to quit)")
while True:
    query = input("\nAsk something: ")

    if query.lower() in ["exit", "quit"]:
        break
    
    try:
        response = agent.run(query)
        print("\nAgent Response:\n", response)
    except Exception as e:
        print(f"\nEncountered an error: {e}")

mcp_client.disconnect()