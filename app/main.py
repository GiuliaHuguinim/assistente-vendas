from fastapi import FastAPI, HTTPException
from .schemas import AIRequest, AIResponse
from .clients.gemini_client import ask_gemini
from .clients.groq_client import ask_groq

app = FastAPI(title="Petlove Assistente de Vendas")

@app.post("/api/question-and-answer", response_model=AIResponse)
def qa_endpoint(req: AIRequest):
    try:
        return {"response": ask_gemini(req.question)}
    except Exception:
        try:
            return {"response": ask_groq(req.question)}
        except Exception as e:
            raise HTTPException(
                status_code=502,
                detail=f"Erro ao consultar serviços de IA: {str(e)}"
            )
