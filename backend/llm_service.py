import os
from datetime import datetime

import ollama

from models import ComplimentRequest, ComplimentResponse
from prompts import create_nurtured_heart_prompt


class LLMService:
    def __init__(self):
        self.model = os.getenv("DEFAULT_MODEL", "llama3.2:1b")
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

        # Configure ollama client
        ollama._client._base_url = self.ollama_host

    async def generate_compliment(self, request: ComplimentRequest) -> ComplimentResponse:
        """Generate a nurtured heart compliment using the local LLM."""

        # Create the prompt
        prompt = create_nurtured_heart_prompt(
            recipient_name=request.recipient_name,
            relationship=request.relationship,
            qualities=request.qualities,
            context=request.context,
            tone=request.tone
        )

        try:
            # Call Ollama
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={
                    "temperature": self.temperature,
                    "top_p": 0.9,
                }
            )

            compliment_text = response['response'].strip()

            return ComplimentResponse(
                compliment=compliment_text,
                generated_at=datetime.utcnow().isoformat()
            )

        except Exception as e:
            raise Exception(f"Failed to generate compliment: {e!s}")

    async def check_model_availability(self) -> dict:
        """Check if the required model is available."""
        try:
            models = ollama.list()
            # Handle the ListResponse object format
            if hasattr(models, 'models'):
                model_names = [m.model for m in models.models]
            elif isinstance(models, dict) and 'models' in models:
                model_names = [m['name'] for m in models['models']]
            elif isinstance(models, list):
                model_names = [m['name'] for m in models]
            else:
                model_names = []

            return {
                "available": self.model in model_names,
                "installed_models": model_names,
                "required_model": self.model
            }
        except Exception as e:
            return {
                "available": False,
                "error": str(e)
            }

llm_service = LLMService()

