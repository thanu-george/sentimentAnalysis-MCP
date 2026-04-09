##Sentiment + Summarization: FastAPI vs. MCP Agent
This project explores the architectural evolution from Deterministic Pipelines to Agentic Tool Orchestration. 
It compares a traditional REST API approach with a Model Context Protocol (MCP) implementation where an LLM acts as the central reasoning engine.

#1.Traditional FastAPI (Deterministic)
In this model, the developer defines the workflow.

Control Flow: Linear and hardcoded.
Execution: Every request triggers the same sequence (Summarize → Sentiment Analysis).
Use Case: Best for high-reliability, low-latency, and predictable production environments where consistency is paramount.

#2. MCP + Smolagents (Agentic)

In this model, the developer defines the capabilities and the LLM defines the workflow

Control Flow: Dynamic and intent-driven.
Execution: The LLM (Qwen2.5-coder) inspects the available MCP tools and decides which tool to call (or skip) based on the user's prompt.
Use Case: Best for complex, multi-step tasks where the "right" answer depends on context and nuance.

