# Sentiment + Summarization: FastAPI vs. MCP Agent
This project explores the architectural evolution from Deterministic Pipelines to Agentic Tool Orchestration. 
It compares a traditional REST API approach with a Model Context Protocol (MCP) implementation where an LLM acts as the central reasoning engine.

## Architectural Comparison
### 1.Traditional FastAPI (Deterministic)
In this model, the developer defines the workflow.

Control Flow: Linear and hardcoded.
Execution: Every request triggers the same sequence (Summarize → Sentiment Analysis).
Use Case: Best for high-reliability, low-latency, and predictable production environments where consistency is paramount.

### 2. MCP + Smolagents (Agentic)
In this model, the developer defines the capabilities and the LLM defines the workflow

Control Flow: Dynamic and intent-driven.
Execution: The LLM (Qwen2.5-coder) inspects the available MCP tools and decides which tool to call (or skip) based on the user's prompt.
Use Case: Best for complex, multi-step tasks where the "right" answer depends on context and nuance.

## Insight
In the MCP setup, the Agent doesn't just call a function. If the tool provides a raw or truncated result, the Agent's reasoning loop polishes that data into a user-friendly response, effectively upgrading the quality of the underlying code.

## Tech Stack
Frameworks: FastAPI, Streamlit, Gradio\
AI Orchestration: MCP (Model Context Protocol), smolagents\
Models: Ollama (Qwen2.5-coder)\
NLP: TextBlob, Python

##How to Run
1. Start the fastapi server\
uvicorn fastapi_app.main:app --reload --port 8000

2. Start the MCP/Gradio Server\
python -m mcp_server.server

3. Launch Streamlit
streamlit run ui/streamlit_app.py
