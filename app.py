import os
import gradio as gr
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

# Set up environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Set up LLM client
llm = ChatGroq(temperature=0, model_name='llama-3.1-8B-Instant', groq_api_key=GROQ_API_KEY)

# Chatbot function
def stream_chat(
    message: str,
    history: list,
    system_prompt: str,
    temperature: float = 0.5,
    max_tokens: int = 1024,
):
    conversation = [SystemMessage(content=system_prompt)]
    for prompt, answer in history:
        conversation.extend([
            HumanMessage(content=prompt),
            SystemMessage(content=answer),
        ])
    conversation.append(HumanMessage(content=message))

    # Update LLM parameters
    llm.temperature = temperature
    llm.max_tokens = max_tokens

    response = llm.stream(conversation)

    partial_message = ""
    for chunk in response:
        if chunk.content:
            partial_message += chunk.content
            yield partial_message

# Gradio Interface
CSS = """
.duplicate-button {
    margin: auto !important;
    color: white !important;
    background: black !important;
    border-radius: 100vh !important;
}
h3, p, h1 {
    text-align: center;
    color: white;
}
footer {
    text-align: center;
    padding: 10px;
    width: 100%;
    background-color: rgba(240, 240, 240, 0.8);
    z-index: 1000;
    position: relative;
    margin-top: 10px;
    color: black;
}
"""

PLACEHOLDER = """
<center>
<p>Hello! I'm here to assist you. Ask me anything :)</p>
</center>
"""

TITLE = "<h1><center>ConverseBot AI</center></h1>"

EXPLANATION = """
<div style="text-align: center; margin-top: 20px;">
    <p>This app uses the llama-3.1-8B model, a powerful language model designed for high-quality, reasoning-rich interactions.</p>
</div>
"""

FOOTER_TEXT = """<footer> <p>If you enjoyed the functionality of the app, please leave a like!<br> Check out more on <a href="https://www.linkedin.com/in/girish-wangikar/" target="_blank">LinkedIn</a> | <a href="https://girishwangikar.github.io/Girish_Wangikar_Portfolio.github.io/" target="_blank">Portfolio</a></p></footer>"""

# Gradio app
with gr.Blocks(css=CSS, theme="Nymbo/Nymbo_Theme") as demo:
    gr.HTML(TITLE)
    gr.HTML(EXPLANATION)
    gr.DuplicateButton(value="Duplicate Space for private use", elem_classes="duplicate-button")
    chatbot = gr.Chatbot(height=600, placeholder=PLACEHOLDER)
    gr.ChatInterface(
        fn=stream_chat,
        chatbot=chatbot,
        fill_height=True,
        additional_inputs_accordion=gr.Accordion(label="⚙️ Parameters", open=False, render=False),
        additional_inputs=[
            gr.Textbox(
                value="You are a helpful assistant",
                label="System Prompt",
                render=False,
            ),
            gr.Slider(
                minimum=0,
                maximum=1,
                step=0.1,
                value=0.5,
                label="Temperature",
                render=False,
            ),
            gr.Slider(
                minimum=128,
                maximum=8192,
                step=1,
                value=1024,
                label="Max tokens",
                render=False,
            ),
        ],
        examples=[
            ["What are some tips for mastering machine learning algorithms?"],
            ["What's a simple recipe for a healthy dinner?"],
            ["What are the benefits of meditation and how do I begin?"],
            ["Can you recommend some classic novels to read?"],
        ],
        cache_examples=False,
    )
    
    gr.HTML(FOOTER_TEXT)

# Launch the app
demo.launch(debug=True)
