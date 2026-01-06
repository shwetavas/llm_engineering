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

system_prompt = """
You are a career advisor. The user will provide their background, skills, and goals. You need to advise them on the best career path for them.
"""

user_prompt = input("Please provide your background, skills, and goals and I will advise you on the best career path for you: ")

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