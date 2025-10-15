# Environment Setup Guide

This project uses environment variables to manage configuration for both local development and production deployments.

## Quick Start

### Backend Setup

1. Copy the example file:
   ```bash
   cd backend
   cp .env.example .env
   ```

2. Configure your AI service by setting the `AI_SERVICE` variable:
   - **For local models:** `AI_SERVICE=ollama` (default)
   - **For cloud API:** `AI_SERVICE=gemini` (works locally and in production)

3. (Optional) Configure email service by updating these variables in `.env`:
   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   FROM_EMAIL=your-email@gmail.com
   ```

### Frontend Setup

1. Copy the example file:
   ```bash
   cd frontend
   cp .env.example .env
   ```

2. The default `.env` file points to `http://localhost:8000` which is correct for local development.

## Environment Variables Reference

### Backend Variables

| Variable | Description | Default (Local) | Example (Production) |
|----------|-------------|-----------------|---------------------|
| `AI_SERVICE` | AI service to use: `ollama` or `gemini` | `ollama` | `gemini` |
| `HOST` | Server host address | `0.0.0.0` | `0.0.0.0` |
| `PORT` | Server port | `8000` | `8000` |
| `CORS_ORIGINS` | Allowed CORS origins (comma-separated) | `http://localhost:5173,http://localhost:3000` | `https://yourdomain.com` |
| `OLLAMA_HOST` | Ollama API endpoint (for local dev) | `http://localhost:11434` | `http://ollama:11434` |
| `OLLAMA_MODEL` | Ollama model to use (for local dev) | `llama3.2:1b` | `llama3.2:1b` |
| `GEMINI_API_KEY` | Google Gemini API key (for hosted) | (empty) | `your_api_key_here` |
| `GEMINI_MODEL` | Gemini model to use (for hosted) | (empty) | `gemini-2.5-flash-lite` |
| `TEMPERATURE` | LLM temperature setting | `0.7` | `0.7` |
| `SMTP_HOST` | SMTP server hostname | (empty - disabled) | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP server port | `587` | `587` |
| `SMTP_USER` | SMTP username | (empty - disabled) | `user@domain.com` |
| `SMTP_PASSWORD` | SMTP password | (empty - disabled) | `your-password` |
| `FROM_EMAIL` | Email sender address | (empty - disabled) | `noreply@domain.com` |

### Frontend Variables

| Variable | Description | Default (Local) | Example (Production) |
|----------|-------------|-----------------|---------------------|
| `VITE_API_URL` | Backend API URL (also used for API docs link) | `http://localhost:8000` | `https://nurtured-heart-ai-backend.vercel.app` |
| `VITE_APP_TITLE` | Application title | `Nurtured Heart AI` | `Nurtured Heart AI` |
| `VITE_APP_VERSION` | Application version | `1.0.0` | `1.0.0` |

**Note:** The `VITE_API_URL` is used to construct the API Documentation link in the footer (appends `/docs` to the URL).

## AI Service Configuration

This application supports two AI service configurations that can both be used locally:

### Local Models (Ollama)
Set `AI_SERVICE=ollama` and configure:
```env
AI_SERVICE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b
TEMPERATURE=0.7
```

**Requirements:**
- Ollama installed locally
- Model downloaded (e.g., `ollama pull llama3.2:1b`)
- Ollama server running (`ollama serve`)

**Benefits:** Complete privacy, works offline, open-source models

### Cloud API (Google Gemini)
Set `AI_SERVICE=gemini` and configure:
```env
AI_SERVICE=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
TEMPERATURE=0.7
```

**Requirements:**
- Google AI Studio API key from [aistudio.google.com](https://aistudio.google.com/)
- Internet connection

**Benefits:** Easy setup, powerful models, works great for local development too!

## Production Deployment

### Backend Production Setup

1. Copy the production template:
   ```bash
   cd backend
   cp .env.prd .env
   ```

2. Update the following values:
   - `AI_SERVICE`: Choose `ollama` or `gemini` (both work in production)
   - `GEMINI_API_KEY`: Add your Google AI Studio API key (if using Gemini)
   - `CORS_ORIGINS`: Set to your production frontend URL(s)
   - Email configuration: Add your production SMTP credentials

### Frontend Production Setup

1. Copy the production template:
   ```bash
   cd frontend
   cp .env.prd .env
   ```

2. Update `VITE_API_URL` to point to your production backend API.

## Security Notes

⚠️ **Important Security Considerations:**

- **Never commit `.env`, `.env.local`, or `.env.prd` files to version control**
- These files are already excluded in `.gitignore`
- Only commit `.env.example` files as templates
- Use secure password management for SMTP credentials
- For Gmail, use [App Passwords](https://support.google.com/accounts/answer/185833) instead of your regular password
- Rotate credentials regularly, especially if they may have been exposed

## Email Service Configuration Examples

### Gmail
```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-16-char-app-password
FROM_EMAIL=your-email@gmail.com
```

### Outlook/Office 365
```
SMTP_HOST=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USER=your-email@outlook.com
SMTP_PASSWORD=your-password
FROM_EMAIL=your-email@outlook.com
```

### SendGrid
```
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASSWORD=your-sendgrid-api-key
FROM_EMAIL=verified-sender@yourdomain.com
```

## Docker Compose

When using Docker Compose, environment variables are already configured in `docker-compose.yml`. However, you can override them by:

1. Creating a `.env` file in the project root
2. Docker Compose will automatically load variables from this file
3. Example root `.env`:
   ```
   OLLAMA_HOST=http://ollama:11434
   CORS_ORIGINS=http://localhost:5173
   ```

## Troubleshooting

### Backend won't start
- Ensure all required variables are set in `.env`
- Check that `OLLAMA_HOST` is accessible
- Verify `PORT` is not already in use

### Frontend can't connect to backend
- Verify `VITE_API_URL` in frontend `.env` matches your backend URL
- Check CORS settings in backend `.env`
- Ensure backend is running and accessible

### Email not working
- Verify all SMTP variables are set correctly
- Check firewall/network allows outbound SMTP connections
- For Gmail, ensure "Less secure app access" is enabled or use App Passwords
- Test SMTP credentials using a simple email client first

## Environment Variable Loading

### Backend (Python/FastAPI)
- Uses `python-dotenv` package
- Automatically loads `.env` file from backend directory
- Variables accessed via `os.getenv()`

### Frontend (Vue/Vite)
- Vite automatically loads `.env` files
- Only variables prefixed with `VITE_` are exposed to the client
- Variables accessed via `import.meta.env.VITE_*`

