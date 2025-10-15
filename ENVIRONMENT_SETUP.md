# Environment Variables Setup

## Local Development (.env file in backend directory)

Create a `.env` file in the `backend/` directory with the following content:

```env
# AI Service Configuration
AI_SERVICE=ollama

# Ollama Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b

# General AI Settings
TEMPERATURE=0.7

# CORS Configuration
CORS_ORIGINS=http://localhost:5173

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

## Production (Vercel Environment Variables)

In your Vercel dashboard, add the following environment variables:

### Required Variables:
- `AI_SERVICE` = `gemini`
- `GEMINI_API_KEY` = `your_actual_api_key_from_google_ai_studio`
- `GEMINI_MODEL` = `gemini-2.5-flash-lite`
- `CORS_ORIGINS` = `your_frontend_vercel_url`

### Optional Variables:
- `TEMPERATURE` = `0.7`
- `EMAIL_ENABLED` = `false` (or configure email settings if needed)

## Getting Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key"
4. Create a new API key
5. Copy the API key and add it to your Vercel environment variables as `GEMINI_API_KEY`

## Docker Compose

The `docker-compose.yml` file is already configured with the correct environment variables for local development with Ollama.
