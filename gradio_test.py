import os
import json
import requests
import ollama
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
from dotenv import load_dotenv

import gradio as gr

# system_message = "You are a helpful assistant."

# def message_gpt(prompt):
#     load_dotenv(override=True)
#     api_key = os.getenv('OPENAI_API_KEY')
#     MODEL = "gpt-4o-mini"
#     open_ai = OpenAI()

#     messages = [
#         {"role": "system", "content": system_message},
#         {"role": "system", "content": prompt}
#     ]
#     completion = open_ai.chat.completions.create(
#         model=MODEL,
#         messages=messages
#     )
#     return completion.choices[0].message.content

# print(message_gpt("What is today's date?"))

# def shout(text):
#     print(f"Shout has been called with input {text}")
#     return text.upper()

# shout("hello")

def message_ollama(message):
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    MODEL = "llama3.2"
    messages = [
        {"role": "user", "content": message}
    ]
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }
    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    return response.json()["message"]["content"]

gr.Interface(fn=message_ollama, inputs=[gr.Textbox(label="Your message:", lines=6)], outputs=[gr.Textbox(label="Response:", lines=8)], allow_flagging="never").launch()