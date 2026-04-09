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

## Key Learning
| Feature      | FastAPI (Hardcoded)              | MCP Agent (Ollama/Qwen)                     |
|--------------|----------------------------------|---------------------------------------------|
| Logic        | Executes raw Python `utils.py`   | Interprets tool results through LLM reasoning |
| Summary      | Simple string slicing (`text[:80]`) | Context-aware summarization and formatting |
| Flexibility  | Rigorous / Rigid                | Adaptive / Intelligent                      |

Insight: In the MCP setup, the Agent doesn't just call a function. If the tool provides a raw or truncated result, the Agent's reasoning loop polishes that data into a user-friendly response, effectively upgrading the quality of the underlying code.

## Tech Stack
Frameworks: FastAPI, Streamlit, Gradio
AI Orchestration: MCP (Model Context Protocol), smolagents
Models: Ollama (Qwen2.5-coder)
NLP: TextBlob, Python
