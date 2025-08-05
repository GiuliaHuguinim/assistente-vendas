# Petlove Assistente de Vendas

## Descrição

API que integra com Gemini e Groq para responder perguntas sobre produtos.

## Tecnologias

* Python 3.10+
* FastAPI
* google-genai (Gemini)
* groq (Groq)

## Instalação

```bash
git clone <repo>
cd petlove-assistente
python -m venv venv
```

### No Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### No Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

### No macOS/Linux

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Configuração

Copie o arquivo `.env.example` para `.env` e preencha suas chaves:

```env
GEMINI_API_KEY=sua_chave_api_gemini
GROQ_API_KEY=sua_chave_api_groq
```

## Uso

```bash
uvicorn app.main:app --reload --port 3000
```

Faça uma requisição de teste:

```bash
curl -X POST http://localhost:3000/api/question-and-answer \
  -H "Content-Type: application/json" \
  -d '{"question":"qual a melhor ração para golden?"}'
```
