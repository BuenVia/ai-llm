import json
import os
import ollama
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = "gpt-4o-mini"
open_ai = OpenAI()

def run_openai():
    question = """Please explain what this code does and why:
    yield from {book.get("author") for book in books if book.get("author")}
    """
    response = open_ai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful software development assistant"},
            {"role": "user", "content": question}
        ],
    )
    return response.choices[0].message.content
    
def run_ollama():
    question = """Please explain what this code does and why:
    yield from {book.get("author") for book in books if book.get("author")}
    """ 
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful software development assistant"},
            {"role": "user", "content": question}
        ]
    )
    return response['message']['content']

# x = run_openai()
x = run_ollama()

print(x)
with open("answer-1.md", "w") as f:
    f.write(x)