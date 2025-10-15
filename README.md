# 💙 Nurtured Heart Compliment Generator

An AI-powered web application that generates heartfelt, meaningful compliments using the Nurtured Heart Approach.

![Project Status](https://img.shields.io/badge/status-ready-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📸 What It Does

This app helps you create meaningful, personalized compliments based on the **Nurtured Heart Approach** - a method that focuses on recognizing and celebrating inner greatness, positive qualities, and success in specific, authentic ways.

### Example Flow

1. **Input:** Name: "Emma", Relationship: "student", Qualities: ["creative", "persistent"], Context: "finished a challenging science project"
2. **Output:** *"Emma, I see such creativity and persistence in how you approached your science project. The way you stuck with the challenge, even when it was difficult, shows the strength of your character. Your determination and innovative thinking are truly inspiring, and they reflect the inner greatness that makes you special."*

## ✨ Features

- 🤖 AI-powered compliment generation (Ollama local or Google Gemini)
- 💝 Based on Nurtured Heart Approach principles
- 🎨 Beautiful, responsive UI with PrimeVue
- 🌐 Flexible deployment options (local or hosted)

## 🛠️ Tech Stack

**Backend:**
- Python 3.11+
- FastAPI
- AI Services: Ollama (local) or Google Gemini (hosted)

**Frontend:**
- Vue.js 3
- PrimeVue
- Vite


## 🤖 AI Service Options

This application supports two AI service configurations that can be used both locally and in production:

### 🦙 Ollama (Local Models)
- **Best for:** Privacy-focused usage, offline capability, open-source models
- **Requirements:** Ollama installed locally with LLM models
- **Models:** llama3.2, mistral, or other Ollama-compatible models
- **Privacy:** All processing happens on your local machine
- **Use cases:** Local development, private deployments, offline usage

### 🤖 Google Gemini (Cloud API)
- **Best for:** Easy setup, powerful models, no local installation needed
- **Requirements:** Google AI Studio API key (free tier available)
- **Models:** gemini-pro, gemini-2.5-flash-lite
- **Privacy:** Data sent to Google's servers (see their privacy policy)
- **Use cases:** Local development, production deployments, shared hosting

**Both services can be used locally!** The choice depends on your preferences for privacy vs convenience.

## 🚀 Quick Start

### Prerequisites

**Option 1: Local Models with Ollama**
1. **Install Ollama:** https://ollama.ai/download
   
   **macOS:**
   ```bash
   brew install ollama
   ```

2. **Pull the LLM Model:**
   ```bash
   # Main model (~2GB)
   ollama serve
   ollama pull llama3.2
   
   ## You can also use other models like:
   ollama pull mistral # (smaller, faster)
   ollama pull llama3.2:1b # smallest, for testing
   ```

**Option 2: Cloud API with Google Gemini (also works locally)**
1. Get a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. No local LLM installation required - works great for local development too!

**Common Requirements:**
3. **Python 3.11+** and **Node.js 18+**

### Installation

#### Option 1: Automated Setup (Recommended)

Run the setup script:

```bash
./setup.sh
```

This will:
- Create environment files
- Set up Python virtual environment
- Install backend dependencies
- Install frontend dependencies

#### Option 2: Manual Setup

**Step 1: Create Environment Files**

Backend:
```bash
cd backend
cp .env.example .env
```

Frontend:
```bash
cd frontend
cp .env.example .env
```

> 📖 **For detailed environment configuration options, see [ENV_SETUP.md](ENV_SETUP.md)**  
> This includes SMTP setup for email functionality, production deployment, and more.

**Step 2: Install Backend Dependencies**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..
```

**Step 3: Install Frontend Dependencies**

```bash
cd frontend
npm install
cd ..
```

---

## 🎮 Running the Application

### Option 1: Using Helper Scripts

**Terminal 1 - Backend:**
```bash
# Terminal 1
./start-backend.sh

# Terminal 2
./start-frontend.sh
```

### Option 2: Manual Start

**Terminal 1: Start Ollama (if not already running)**
```bash
# Terminal 1 - Ollama (Leave this running in the background)
ollama serve #

# Terminal 2 - Backend (http://localhost:8000)
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py 

# Terminal 3 - Frontend (http://localhost:5173)
cd frontend
npm run dev
```

### Option 3: Using Docker

```bash
docker-compose up
```

### Open Your Browser

Navigate to: **http://localhost:5173**


## 🎯 Usage

### Try It Out!

1. **Enter a name:** e.g., "Jordan"
2. **Select relationship:** e.g., "student"
3. **Add qualities:** Click the + button after typing each quality
   - "creative"
   - "persistent"
   - "thoughtful"
4. **Add context:** "completed a challenging art project"
5. **Choose tone:** warm, enthusiastic, calm, professional
6. **Click "Generate Compliment"**
7. Copy or share the compliment!

You should see a personalized compliment generated by the AI!

### Test API Directly

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_name": "Emma",
    "relationship": "student",
    "qualities": ["creative", "persistent"],
    "context": "finished a challenging project",
    "tone": "warm"
  }'
```

---

## 📚 API Documentation

Once the backend is running, explore the auto-generated API docs:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Check Backend Health

```bash
curl http://localhost:8000/health
```

---

## ⚙️ Configuration

For detailed configuration options, see:
- **[Backend Configuration](backend/README.md)** - Server settings, Ollama models, email setup
- **[Frontend Configuration](frontend/README.md)** - API URL, deployment settings

### Quick Configuration

**Backend** (`backend/.env`):

**Option 1: Local Models (Ollama)**
```env
AI_SERVICE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b
TEMPERATURE=0.7
```

**Option 2: Cloud API (Google Gemini) - works locally too!**
```env
AI_SERVICE=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
TEMPERATURE=0.7
```

**Frontend** (`frontend/.env`):
```env
VITE_API_URL=http://localhost:8000  # Local development
# VITE_API_URL=https://your-backend-url.com  # Production
```

---

## 🛠️ Development

Both frontend and backend support hot reload for rapid development.

For detailed development guides:
- **[Backend Development](backend/README.md#-development)** - API customization, prompts, testing
- **[Frontend Development](frontend/README.md#-development)** - Components, routing, styling
- **[Linting Guide](LINTING.md)** - Code quality and style enforcement

### Quick Start Development

**Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm run dev
```

### Code Quality

This project uses linters to maintain code quality:

**Backend (Python):**
```bash
cd backend
ruff check .          # Check for issues
ruff check --fix .    # Auto-fix issues
ruff format .         # Format code
```

**Frontend (JavaScript/Vue):**
```bash
cd frontend
npm run lint          # Check for issues
npm run lint:fix      # Auto-fix issues
```

See **[LINTING.md](LINTING.md)** for complete linting documentation.

---

## 🐛 Troubleshooting

### Common Issues

**LLM Not Ready:**
```bash
# Check Ollama is running
curl http://localhost:11434/api/tags

# Pull model if missing
ollama pull llama3.2
```

**Backend Not Connecting:**
```bash
# Check backend health
curl http://localhost:8000/health
```

**Frontend Not Loading:**
```bash
# Check for port conflicts
lsof -i :5173

# Try different port
npm run dev -- --port 3000
```

For detailed troubleshooting:
- **[Backend Troubleshooting](backend/README.md#-troubleshooting)**
- **[Frontend Troubleshooting](frontend/README.md#-troubleshooting)**

---

## 🚀 Deployment

For detailed deployment guides:
- **[Backend Deployment](backend/README.md#-deployment)** - Railway, Render, AWS, Docker
- **[Frontend Deployment](frontend/README.md#-deployment)** - Vercel, Netlify, GitHub Pages

### Quick Deployment Options

**Backend:**
- **Recommended:** Vercel/Railway/Render (Python + Google Gemini)
- **Alternative:** AWS/GCP/Azure (VM with Docker + Ollama)
- **Configuration:** Both Ollama and Gemini work great for local development and production deployment

**Frontend:**
- Vercel/Netlify (Static hosting)
- Build: `npm run build` → Deploy `dist/` folder

---

## 📖 About Nurtured Heart Approach

The Nurtured Heart Approach focuses on recognizing and celebrating inner greatness, positive qualities, and success in meaningful, specific ways. This approach:

- Emphasizes what's going right rather than what's going wrong
- Recognizes effort and character, not just outcomes
- Uses specific, authentic language
- Celebrates inner qualities and values
- Builds self-worth and positive identity

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What does this mean?

✅ **You can:**
- Use this project commercially
- Modify and distribute it
- Use it privately
- Sublicense it

❗ **You must:**
- Include the original copyright notice and license

🚫 **This software comes with:**
- NO warranty or liability

---

## 📚 Documentation

- **[Backend Documentation](backend/README.md)** - API, configuration, models, email setup
- **[Frontend Documentation](frontend/README.md)** - Components, routing, styling, deployment
- **[Linting Documentation](LINTING.md)** - Code quality, style guides, linter setup
- **[API Docs](http://localhost:8000/docs)** - Interactive API documentation (when running)

## 🙋 Need Help?

- Backend logs: Terminal where backend is running
- Frontend errors: Browser console (F12)
- API documentation: http://localhost:8000/docs
- Configuration: Check `.env` files in backend/ and frontend/

---

**Happy compliment generating! 💙**
