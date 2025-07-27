from google import genai
from ..config import settings

client = genai.Client(api_key=settings.gemini_api_key)

def ask_gemini(question: str) -> str:
    prompt = f"{settings.sales_assistant_context}\nUsuário: {question}"
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=prompt
    )
    return response.text
