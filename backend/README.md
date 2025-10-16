# Backend - Nurtured Heart Compliment Generator

FastAPI backend service for generating Nurtured Heart compliments using AI (Ollama or Google Gemini).

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern async web framework
- **Ollama** - Local LLM interface
- **Google Generative AI** - Cloud LLM API
- **Pydantic** - Data validation
- **aiosmtplib** - Async email sending

---

## 📁 Project Structure

```
backend/
├── main.py              # FastAPI app, endpoints, CORS
├── models.py            # Pydantic request/response models
├── prompts.py           # LLM prompt templates
├── llm_service.py       # AI service abstraction (Ollama/Gemini)
├── email_service.py     # Email functionality
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Ruff linter configuration
├── vercel.json          # Vercel deployment config
├── Dockerfile           # Docker configuration
└── .env                 # Environment variables (create from .env.example)
```

---

## 🔌 API Endpoints

### Health Check

**`GET /health`**

Returns server status and AI service availability.

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "api": "healthy",
  "llm": {
    "service": "ollama",
    "available": true,
    "installed_models": ["llama3.2:1b", "mistral:latest"],
    "required_model": "llama3.2:1b"
  },
  "email_service": false
}
```

---

### Generate Compliment

**`POST /api/generate`**

Generates a Nurtured Heart compliment.

**Request:**
```json
{
  "recipient_name": "Emma",
  "relationship": "student",
  "qualities": ["creative", "persistent"],
  "context": "finished a challenging project",
  "tone": "warm"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "compliment": "Emma, I see such creativity and persistence...",
    "generated_at": "2024-10-16T10:30:00.000Z"
  }
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_name": "Jordan",
    "relationship": "student",
    "qualities": ["creative", "determined"],
    "context": "completed a challenging project",
    "tone": "warm"
  }'
```

---

### Send Email

**`POST /api/send-email`**

Sends a compliment via email (if SMTP configured).

**Request:**
```json
{
  "recipient_email": "user@example.com",
  "recipient_name": "Emma",
  "sender_name": "Mr. Smith",
  "compliment": "Your personalized compliment text here"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Compliment sent to user@example.com"
}
```

---

### List Models

**`GET /api/models`**

Returns available AI models (Ollama only).

```bash
curl http://localhost:8000/api/models
```

---

## 📚 Interactive API Documentation

FastAPI auto-generates interactive docs:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

These allow you to test endpoints directly in the browser!

---

## 🤖 AI Service Configuration

The backend supports two AI services via the `AI_SERVICE` environment variable.

### Ollama (Local Models)

**Best for:** Privacy, offline, self-hosted

**Environment variables:**
```env
AI_SERVICE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b
TEMPERATURE=0.7
```

**Recommended models:**

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| `llama3.2:1b` | ~1GB | Fast | Good | Development/testing |
| `llama3.2:latest` | ~2GB | Medium | High | Production |
| `mistral:latest` | ~4GB | Medium | High | Alternative |
| `phi3:latest` | ~2GB | Fast | Good | Smaller deployments |

**Pull models:**
```bash
ollama pull llama3.2
ollama pull mistral
ollama pull phi3
```

**Switch models:** Update `OLLAMA_MODEL` in `.env` and restart server.

---

### Google Gemini (Cloud API)

**Best for:** Easy deployment, powerful models, serverless

**Environment variables:**
```env
AI_SERVICE=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
TEMPERATURE=0.7
```

**Get API key:** [Google AI Studio](https://aistudio.google.com/)

**Available models:**
- `gemini-2.5-flash-lite` - Fast, efficient (recommended)
- `gemini-pro` - More powerful, slower

---

### Temperature Settings

Controls randomness/creativity in responses:

- `0.0-0.3`: Focused, consistent, predictable
- `0.4-0.7`: Balanced (recommended: **0.7**)
- `0.8-1.0`: Creative, varied, less predictable

---

## 🛠️ Development

### Running the Server

**Development mode (auto-reload):**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
uvicorn main:app --reload
```

**Production mode:**
```bash
python main.py
```

Server runs at: http://localhost:8000

---

### Customizing Prompts

Edit `prompts.py` to modify how compliments are generated:

```python
def create_nurtured_heart_prompt(
    recipient_name: str,
    relationship: str,
    qualities: list[str],
    context: Optional[str] = None,
    tone: str = "warm"
) -> str:
    """
    Customize the prompt template here.
    """
    # Your custom logic
    return prompt_text
```

**Tips:**
- Add more context about Nurtured Heart principles
- Adjust tone variations
- Include examples for few-shot learning
- Experiment with different prompt structures

---

### Adding New Endpoints

In `main.py`:

```python
@app.post("/api/your-endpoint")
async def your_endpoint(request: YourRequestModel):
    """Your endpoint logic."""
    try:
        result = await your_service.do_something(request)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

Define models in `models.py`:

```python
class YourRequestModel(BaseModel):
    field1: str
    field2: Optional[int] = None
```

---

### Code Quality

**Linting with Ruff:**
```bash
# Check for issues
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code
ruff format .

# Or use the script
./lint.sh
```

**Configuration:** `pyproject.toml`
- Line length: 100 characters
- Indentation: 2 spaces
- Rules: pycodestyle, pyflakes, isort, pep8-naming

See [LINTING.md](../LINTING.md) for details.

---

## 🧪 Testing

### Manual Testing

**Health check:**
```bash
curl http://localhost:8000/health
```

**Generate compliment:**
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_name": "Test",
    "relationship": "friend",
    "qualities": ["kind"],
    "context": "helping out",
    "tone": "warm"
  }'
```

**Test email (if configured):**
```bash
curl -X POST http://localhost:8000/api/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_email": "test@example.com",
    "recipient_name": "Test",
    "sender_name": "Your Name",
    "compliment": "Test compliment"
  }'
```

---

### End-to-End Testing

The project includes Cypress tests in the frontend that test the full stack.

See [Frontend Testing Guide](../frontend/README.md#-testing).

---

## 🐛 Troubleshooting

### Ollama Not Available

**Check if Ollama is running:**
```bash
curl http://localhost:11434/api/tags
```

**Start Ollama:**
```bash
ollama serve
```

**Verify model is installed:**
```bash
ollama list
```

**Pull model:**
```bash
ollama pull llama3.2:1b
```

---

### Gemini API Errors

**"GEMINI_API_KEY environment variable is required"**
- Ensure `GEMINI_API_KEY` is set in `.env`
- Restart the server after setting it

**"Invalid API key"**
- Verify key is correct in [Google AI Studio](https://aistudio.google.com/)
- Check for extra spaces in `.env` file

**Rate limit errors:**
- Free tier: 15 requests/minute, 1500/day
- Monitor usage in Google AI Studio
- Consider upgrading plan if needed

---

### Import Errors

**"Module not found"**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

---

### Port Already in Use

```bash
# Find process on port 8000
lsof -i :8000

# Kill it (replace PID)
kill -9 <PID>

# Or use different port
PORT=8001 python main.py
```

---

### CORS Errors

**Update `CORS_ORIGINS` in `.env`:**
```env
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

For production, set to your frontend URL:
```env
CORS_ORIGINS=https://yourdomain.com
```

---

### Email Not Sending

**Check configuration:**
```bash
# Verify all SMTP variables are set
grep SMTP .env
```

**For Gmail:**
- Use App Password, not regular password
- Enable 2-Factor Authentication first
- Generate at: https://myaccount.google.com/security

**Test SMTP connection:**
```bash
python -c "import smtplib; smtplib.SMTP('smtp.gmail.com', 587).starttls(); print('OK')"
```

---

## 🚀 Deployment

For production deployment, see the [DEPLOYMENT.md](../DEPLOYMENT.md) guide which covers:
- Vercel, Railway, Render (serverless)
- Docker + VM (self-hosted)
- Environment variables for production
- Monitoring and troubleshooting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
