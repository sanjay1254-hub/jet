import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Welcome to your ChatGPT-like bot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    print("Bot:", response.choices[0].message['content'].strip())