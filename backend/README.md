# Backend - Nurtured Heart Compliment Generator

FastAPI backend service for generating Nurtured Heart compliments using Ollama (local LLM).

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern web framework
- **Ollama** - Local LLM interface
- **Pydantic** - Data validation
- **SMTP** - Email sending (optional)

## 📋 Requirements

- Python 3.11 or higher
- Ollama installed and running
- At least one LLM model pulled (e.g., `llama3.2`)

## 🚀 Setup

### 1. Create Virtual Environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Environment File

Create a `.env` file in the `backend/` directory:

```bash
cat > .env << 'EOF'
# Server Settings
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:5173

# AI Service Configuration
AI_SERVICE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b
TEMPERATURE=0.7

# Email Configuration (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=your-email@gmail.com
EOF
```

## ⚙️ Configuration Options

### Server Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host address |
| `PORT` | `8000` | Server port |
| `CORS_ORIGINS` | `http://localhost:5173` | Allowed CORS origins (comma-separated) |

### Ollama Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `AI_SERVICE` | `ollama` | AI service to use: `ollama` or `gemini` |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `llama3.2:1b` | Ollama model to use |
| `TEMPERATURE` | `0.7` | LLM temperature (0.0-1.0, higher = more creative) |

### Email Configuration (Optional)

| Variable | Description |
|----------|-------------|
| `SMTP_HOST` | SMTP server hostname |
| `SMTP_PORT` | SMTP server port (587 for TLS) |
| `SMTP_USER` | SMTP username/email |
| `SMTP_PASSWORD` | SMTP password or app password |
| `FROM_EMAIL` | Email address for "From" field |

## 🎮 Running the Server

### Development Mode (with auto-reload)

```bash
source venv/bin/activate
uvicorn main:app --reload
```

### Production Mode

```bash
source venv/bin/activate
python main.py
```

### Using Helper Script

```bash
cd ..  # Go to project root
./start-backend.sh
```

Server will run at: **http://localhost:8000**

## 📚 API Documentation

Once running, access the interactive API documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🔌 API Endpoints

### Health Check

```bash
GET /health
```

Returns server and Ollama status.

### Generate Compliment

```bash
POST /api/generate
```

**Request Body:**
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
  "compliment": "Emma, I see such creativity and persistence...",
  "recipient_name": "Emma"
}
```

### Send Email

```bash
POST /api/send-email
```

**Request Body:**
```json
{
  "to_email": "recipient@example.com",
  "compliment": "Your compliment text here",
  "recipient_name": "Emma"
}
```

## 🤖 LLM Models

### Recommended Models

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| `llama3.2:latest` | ~2GB | Medium | High | Production |
| `llama3.2:1b` | ~1GB | Fast | Medium | Testing/Development |
| `mistral:latest` | ~4GB | Medium | High | Alternative option |
| `phi3:latest` | ~2GB | Fast | Good | Smaller deployments |

### Pull a Model

```bash
ollama pull llama3.2
ollama pull mistral
ollama pull phi3
```

### Switch Models

1. Pull the desired model
2. Update `.env`:
   ```env
   OLLAMA_MODEL=mistral:latest
   ```
3. Restart the server

### Model Parameters

**Temperature** (`0.0` - `1.0`):
- `0.0-0.3`: Focused, consistent, predictable
- `0.4-0.7`: Balanced (recommended)
- `0.8-1.0`: Creative, varied, unpredictable

## 📧 Email Setup (Optional)

### Gmail Setup

1. **Enable 2-Factor Authentication** in your Google Account
2. **Generate App Password:**
   - Go to: https://myaccount.google.com/security
   - Security → 2-Step Verification → App passwords
   - Generate new password for "Mail"
3. **Update `.env`:**
   ```env
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=youremail@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   FROM_EMAIL=youremail@gmail.com
   ```
4. **Restart the server**

### Other Email Providers

**Outlook/Office 365:**
```env
SMTP_HOST=smtp.office365.com
SMTP_PORT=587
```

**Yahoo:**
```env
SMTP_HOST=smtp.mail.yahoo.com
SMTP_PORT=587
```

**Custom SMTP:**
```env
SMTP_HOST=your-smtp-server.com
SMTP_PORT=587  # or 465 for SSL
```

## 🛠️ Development

### Project Structure

```
backend/
├── main.py           # FastAPI app & endpoints
├── models.py         # Pydantic models
├── prompts.py        # LLM prompt templates
├── llm_service.py    # Ollama integration
├── email_service.py  # Email functionality
├── requirements.txt  # Python dependencies
├── .env             # Configuration (create this)
└── Dockerfile       # Docker configuration
```

### Customize Prompts

Edit `prompts.py` to modify how compliments are generated:

```python
def get_compliment_prompt(data: ComplimentRequest) -> str:
    # Your custom prompt logic
    return prompt
```

### Add New Endpoints

In `main.py`:

```python
@app.post("/api/your-endpoint")
async def your_endpoint():
    # Your logic here
    pass
```

## 🐛 Troubleshooting

### Ollama Not Ready

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama
ollama serve

# Verify model is installed
ollama list
```

### Import Errors

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use

```bash
# Find process on port 8000
lsof -i :8000

# Kill it (replace PID)
kill -9 <PID>

# Or use a different port in .env
PORT=8001
```

### Email Not Sending

1. Check SMTP credentials in `.env`
2. Verify app password (not regular password)
3. Check firewall/network settings
4. Test SMTP connection:
   ```bash
   python -c "import smtplib; smtplib.SMTP('smtp.gmail.com', 587).starttls()"
   ```

## 🧪 Testing

### Health Check

```bash
curl http://localhost:8000/health
```

### Generate Compliment

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

### Send Email

```bash
curl -X POST http://localhost:8000/api/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to_email": "recipient@example.com",
    "compliment": "Your personalized compliment here",
    "recipient_name": "Jordan"
  }'
```

## 🚀 Deployment

### Using Docker

```bash
docker build -t nurtured-heart-backend .
docker run -p 8000:8000 --env-file .env nurtured-heart-backend
```

### Environment Variables for Production

```env
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
OLLAMA_HOST=http://ollama-service:11434
```

### Deployment Platforms

- **Railway:** Deploy with Dockerfile
- **Render:** Python app with Ollama
- **Fly.io:** Docker deployment
- **AWS/GCP/Azure:** VM with Ollama installed
- **Self-hosted:** Any server with Docker

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

