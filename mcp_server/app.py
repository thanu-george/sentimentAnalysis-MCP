import json
import gradio as gr
from shared.utils import summarize, sentiment_analysis

# Tool 1
def summarize_tool(text: str) -> str:
    return summarize(text)

# Tool 2
def sentiment_tool(text: str) -> str:
    return json.dumps(sentiment_analysis(text))

demo = gr.Interface(
    fn=sentiment_tool,
    inputs=gr.Textbox(label="Enter review"),
    outputs=gr.Textbox(label="Sentiment"),
    title="MCP Review Tools"
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)