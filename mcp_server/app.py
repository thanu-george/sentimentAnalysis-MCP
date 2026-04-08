import gradio as gr
from shared.utils import summarize, sentiment_analysis
import json

def summarize_tool(text: str) -> str:
    """Summarizes the input text.""" # Docstrings help the Agent understand the tool!
    return summarize(text)

def sentiment_tool(text: str) -> str:
    """Analyzes sentiment of the input text."""
    return json.dumps(sentiment_analysis(text))

# Note: In newer Gradio versions, you register tools like this for MCP:
demo = gr.Interface(
    fn=summarize_tool, # Standard Gradio
    inputs="text",
    outputs="text"
)

if __name__ == "__main__":
    # This exposes all functions in the file as MCP tools
    demo.launch(mcp_server=True)