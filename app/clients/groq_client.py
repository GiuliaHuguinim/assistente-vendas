import os
from groq import Groq
from ..config import settings

client = Groq(api_key=settings.groq_api_key)

def ask_groq(question: str) -> str:
    messages = [
        {"role": "system",  "content": settings.sales_assistant_context},
        {"role": "user",    "content": question},
    ]
    chat = client.chat.completions.create(
        messages=messages,
        model=settings.groq_model
    )
    return chat.choices[0].message.content
