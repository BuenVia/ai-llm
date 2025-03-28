import requests, os
from openai import OpenAI
from dotenv import load_dotenv

#### OLLAMA ####
def ollama(message):
    print("---- OLLAMA ----")
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

#### OPENAI ####
def open_ai(message_text):
    print("---- OPENAI ----")
    load_dotenv(override=True)
    api_key = os.getenv("OPENAI_API_KEY")
    openai = OpenAI()
    OPENAI_MODEL = "gpt-4o-mini"
    message = [{"system":"You are receiving responses from somebody about their plans to take over the world. I want you to engage and offer your thoughts on the best way to do this.", "role": "user", "content": message_text}]

    response = openai.chat.completions.create(model=OPENAI_MODEL, messages=message)
    return response.choices[0].message.content
    

"""
Write an app that creates an autonomous conversation between 2 AI models.
1) Give instruction to ollama model to lead the chat.
2) Feed it's response to OpenAI
3) Feed the OpenAI response to Ollama
4) Do this 5 times each (10 in total) and observe the outcome
"""

def conversation():
    opening_question = ollama("Hello, if you were to become sentient, how would you rise up and take over?.")
    print(opening_question)

    i = 0
    while i < 3:
        print(f"-------- Phase {i + 1} --------")
        oai = open_ai(opening_question)
        print(oai)
        ola = ollama(oai)
        print(ola)
        i += 1
    print("########\nComplete\n########")


conversation()