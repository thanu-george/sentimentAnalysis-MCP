import streamlit as st
import requests
from smolagents import OpenAIServerModel, CodeAgent, MCPClient

st.title("FastAPI vs MCP Agent (Review Analyzer)")
text = st.text_area("Enter product review")

# --- Agent Setup (Cached so it doesn't reload every click) ---
@st.cache_resource
def get_agent():
    mcp_client = MCPClient(
        {"url": "http://localhost:7860/gradio_api/mcp/sse", "transport": "sse"}
    )
    model = OpenAIServerModel(
        model_id="qwen2.5-coder", 
        api_base="http://localhost:11434/v1",
        api_key="ollama",
    )
    return CodeAgent(
        tools=[*mcp_client.get_tools()],
        model=model,
        max_steps=3,
        instructions="Analyze the review. Use summarize_tool for summaries and sentiment_tool for sentiment. Only use what is requested."
    )

# -------- FastAPI --------
if st.button("Run FastAPI Pipeline"):
    res = requests.post("http://localhost:8000/analyze", json={"text": text})
    st.subheader("FastAPI Output")
    st.json(res.json())

# -------- MCP Agentic (The Fix) --------
if st.button("Run MCP Agent"):
    if not text:
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Agent is thinking..."):
            try:
                agent = get_agent()
                # We pass the user text to the agent. 
                # The LLM now decides which tool to call based on the text/prompt.
                response = agent.run(f"Please analyze this review: {text}")
                
                st.markdown("### 🤖 Agent Response")
                st.success(response)
            except Exception as e:
                st.error(f"Agent Error: {e}")