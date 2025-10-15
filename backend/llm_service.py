import os
from datetime import datetime
from typing import Optional

import ollama
import google.generativeai as genai

from models import ComplimentRequest, ComplimentResponse
from prompts import create_nurtured_heart_prompt


class LLMService:
    def __init__(self):
        self.ai_service = os.getenv("AI_SERVICE", "ollama")  # Default to ollama for local dev
        
        if self.ai_service == "ollama":
            self._setup_ollama()
        elif self.ai_service == "gemini":
            self._setup_gemini()
        else:
            raise ValueError(f"Unknown AI service: {self.ai_service}")

    def _setup_ollama(self):
        """Setup Ollama configuration for local development."""
        self.model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        
        # Configure ollama client
        ollama._client._base_url = self.ollama_host

    def _setup_gemini(self):
        """Setup Google Gemini configuration for production."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required for Gemini service")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-pro"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))

    async def generate_compliment(self, request: ComplimentRequest) -> ComplimentResponse:
        """Generate a nurtured heart compliment using the configured AI service."""
        
        # Create the prompt
        prompt = create_nurtured_heart_prompt(
            recipient_name=request.recipient_name,
            relationship=request.relationship,
            qualities=request.qualities,
            context=request.context,
            tone=request.tone
        )

        try:
            if self.ai_service == "ollama":
                return await self._generate_with_ollama(prompt)
            elif self.ai_service == "gemini":
                return await self._generate_with_gemini(prompt)
        except Exception as e:
            raise Exception(f"Failed to generate compliment: {e!s}")

    async def _generate_with_ollama(self, prompt: str) -> ComplimentResponse:
        """Generate compliment using Ollama."""
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

    async def _generate_with_gemini(self, prompt: str) -> ComplimentResponse:
        """Generate compliment using Google Gemini."""
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=self.temperature,
                top_p=0.9,
                max_output_tokens=1000,
            )
        )
        
        compliment_text = response.text.strip()
        
        return ComplimentResponse(
            compliment=compliment_text,
            generated_at=datetime.utcnow().isoformat()
        )

    async def check_model_availability(self) -> dict:
        """Check if the required model/service is available."""
        try:
            if self.ai_service == "ollama":
                return await self._check_ollama_availability()
            elif self.ai_service == "gemini":
                return await self._check_gemini_availability()
        except Exception as e:
            return {
                "available": False,
                "error": str(e),
                "service": self.ai_service
            }

    async def _check_ollama_availability(self) -> dict:
        """Check Ollama model availability."""
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
            "service": "ollama",
            "available": self.model in model_names,
            "installed_models": model_names,
            "required_model": self.model
        }

    async def _check_gemini_availability(self) -> dict:
        """Check Gemini service availability."""
        try:
            # Try to list available models to verify API key works
            models = list(genai.list_models())
            model_names = [m.name for m in models]
            
            return {
                "service": "gemini",
                "available": True,
                "installed_models": model_names,
                "required_model": self.model.model_name if hasattr(self.model, 'model_name') else str(self.model)
            }
        except Exception as e:
            return {
                "service": "gemini",
                "available": False,
                "error": str(e)
            }


llm_service = LLMService()

