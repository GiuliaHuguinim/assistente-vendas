from pydantic import BaseModel

class AIRequest(BaseModel):
    question: str

class AIResponse(BaseModel):
    response: str