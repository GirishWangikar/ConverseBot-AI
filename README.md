# ConverseBot AI

ConverseBot AI is an interactive chatbot application powered by the llama-3.1-8B-Instant model. It provides a user-friendly interface for engaging in high-quality, reasoning-rich conversations on a wide range of topics.

## Features

- **Advanced Language Model**: Utilizes the llama-3.1-8B-Instant model for intelligent and context-aware responses.
- **Interactive Chat Interface**: Built with Gradio for a smooth and responsive user experience.
- **Customizable Parameters**: Adjust system prompts, temperature, and max tokens to fine-tune the AI's behavior.
- **Example Prompts**: Pre-loaded examples to help users get started quickly.
- **Stream Responses**: Responses are streamed in real-time for a more natural conversation flow.
- **Stylish UI**: Features a dark mode theme for comfortable usage.

## Prerequisites

Before running this application, ensure you have the following:

- Python 3.7+
- Gradio
- LangChain

## Installation

1. Clone this repository:
git clone https://github.com/GirishWangikar/ConverseBot-AI
cd conversebot-ai


2. Install the required packages:
pip install gradio langchain-groq


3. Set up your Groq API key as an environment variable:
export API_KEY='your_api_key_here'


## Usage

1. Run the application:
python app.py

2. Open your web browser and navigate to the URL provided in the console output.

3. Start chatting with the AI by typing your message in the input box and pressing Enter.

4. Explore the example prompts for inspiration on what to ask the AI.

5. Adjust the parameters in the "⚙️ Parameters" accordion for a customized experience.

## Customization

- **System Prompt**: Modify the default system prompt to change the AI's persona or behavior.
- **Temperature**: Adjust the randomness of the AI's responses (0 for more deterministic, 1 for more creative).
- **Max Tokens**: Set the maximum length of the AI's responses.

## Contact

Created by Girish Wangikar

Check out more on [LinkedIn](https://www.linkedin.com/in/girish-wangikar/) | [Portfolio](https://girishwangikar.github.io/Girish_Wangikar_Portfolio.github.io/)
