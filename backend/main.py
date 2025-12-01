import os
import tomllib
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from email_service import email_service
from llm_service import llm_service
from models import ComplimentRequest, EmailRequest

# Load environment variables
load_dotenv()

# Read version from pyproject.toml
def get_version() -> str:
  """Read version from pyproject.toml."""
  try:
    pyproject_path = Path(__file__).parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
      pyproject_data = tomllib.load(f)
    return pyproject_data.get("project", {}).get("version", "unknown")
  except Exception:
    return "unknown"

VERSION = get_version()

app = FastAPI(
    title="Nurtured Heart Compliment Generator API",
    description="Generate heartfelt compliments using AI and the Nurtured Heart Approach",
    version=VERSION
)

# CORS configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Nurtured Heart Compliment Generator API",
        "version": VERSION,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Check the health of the API and LLM model.

    Returns:

        {
            "api": string containing the API status,
            "version": string containing the API version,
            "llm": dictionary containing the LLM model configuration,
            "email_service": dictionary containing the email service configuration,
        }
    """
    model_status = await llm_service.check_model_availability()
    email_config = email_service.get_config()

    return {
        "api": "healthy",
        "version": VERSION,
        "llm": model_status,
        "email_service": email_config
    }

@app.post("/api/generate", response_model=dict)
async def generate_compliment(request: ComplimentRequest):
    """Generate a nurtured heart compliment.
    
    Args:

        {
            "recipient_name": string containing the recipient name,
            "relationship": string containing the relationship,
            "qualities": list of strings containing the qualities,
            "context": string containing the context,
            "tone": string containing the tone,
        }

    Returns:
        
        {
            "success": boolean containing the success status,
            "data": dictionary containing the generated compliment,
                "compliment": string containing the generated compliment,
                "generated_at": string containing the generated at timestamp,
        }
    """
    try:
        result = await llm_service.generate_compliment(request)
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/send-email")
async def send_compliment_email(request: EmailRequest):
    """Send a compliment via email.
    
    Args:

        {
            "recipient_email": string containing the recipient email,
            "recipient_name": string containing the recipient name,
            "sender_name": string containing the sender name,
            "compliment": string containing the compliment,
        }

    Returns:

        {
            "success": boolean containing the success status,
            "message": string containing the email sent,
        }
    """
    try:
        result = await email_service.send_compliment(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/models")
async def list_models():
    """List available LLM models.
    
    Returns:

        {
            "service": string containing the LLM service,
            "available": boolean containing whether the LLM model is available,
            "installed_models": list of strings containing the installed LLM models,
            "required_model": string containing the required LLM model,
        }
    """
    return await llm_service.check_model_availability()

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host=host, port=port)

