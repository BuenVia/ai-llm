import requests, os
from openai import OpenAI
from dotenv import load_dotenv

#### OLLAMA ####
def ollama(message):
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    MODEL = "llama3.2"

    messages = [
        {"role": "user", "content": "Describe some business application of Generative AI"}
    ]

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    return response.json()["message"]["content"]

#### OPENAI ####
def open_ai(message_text):
    load_dotenv(override=True)
    api_key = os.getenv("OPENAI_API_KEY")
    openai = OpenAI()
    OPENAI_MODEL = "gpt-4o-mini"
    message = [{"role": "user", "content": message_text}]

    response = openai.chat.completions.create(model=OPENAI_MODEL, messages=message)
    return response.choices[0].message.content
    

"""
Write an app that creates an autonomous conversation between 2 AI models.
1) Give instruction to ollama model to lead the chat.
2) Feed it's response to OpenAI
3) Feed the OpenAI response to Ollama
4) Do this 5 times each (10 in total) and observe the outcome
"""

