import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set")
    exit(1)
else:
    print("OPENAI_API_KEY is set")
    
system_prompt = input("Please provide the role that you want the AI to play (e.g., professional editor, technical writer, or simplifier): ")
user_prompt = input("Please provide the text that you want to rewrite: ")

print("requesting response from AI...")

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-5-nano",
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)