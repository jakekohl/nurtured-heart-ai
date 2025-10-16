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
- 📧 Optional email delivery

## 🛠️ Tech Stack

**Backend:**
- Python 3.11+ / FastAPI
- AI Services: Ollama (local) or Google Gemini (cloud)

**Frontend:**
- Vue.js 3 / PrimeVue / Vite

---

## 🚀 Quick Start

### Prerequisites

Choose one AI service option:

**Option 1: Local Models with Ollama**
```bash
# Install Ollama
brew install ollama  # macOS

# Pull a model
ollama serve
ollama pull llama3.2:1b
```

**Option 2: Cloud API with Google Gemini**
- Get API key from [Google AI Studio](https://aistudio.google.com/)
- No local installation needed - works great for development!

**Common Requirements:**
- Python 3.11+
- Node.js 18+

---

### Installation

#### Automated Setup (Recommended)

```bash
./setup.sh
```

This creates environment files, installs dependencies, and sets up both backend and frontend.

#### Manual Setup

**1. Environment Files**

Backend (`backend/.env`):
```env
# AI Service: Choose "ollama" or "gemini"
AI_SERVICE=ollama

# For Ollama (local)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b

# For Gemini (cloud) - also works locally!
# AI_SERVICE=gemini
# GEMINI_API_KEY=your_api_key_here
# GEMINI_MODEL=gemini-2.5-flash-lite

# Server settings
TEMPERATURE=0.7
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:5173

# Email (optional - leave empty to disable)
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
FROM_EMAIL=
```

Frontend (`frontend/.env`):
```env
VITE_API_URL=http://localhost:8000
```

Or copy from examples:
```bash
cd backend && cp .env.example .env
cd ../frontend && cp .env.example .env
```

**2. Install Dependencies**

```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

---

### Running the Application

**Option 1: Using Helper Scripts**
```bash
# Terminal 1
./start-backend.sh

# Terminal 2
./start-frontend.sh
```

**Option 2: Manual Start**
```bash
# Terminal 1 - Ollama (if using local models)
ollama serve

# Terminal 2 - Backend
cd backend
source venv/bin/activate
python main.py

# Terminal 3 - Frontend
cd frontend
npm run dev
```

**Option 3: Docker**
```bash
docker-compose up
```

> 💡 **Local Docker Customization:** For personal Docker settings (email credentials, different AI models, etc.), create a `docker-compose.override.yml` file:
> ```bash
> cp docker-compose.override.yml.example docker-compose.override.yml
> # Edit docker-compose.override.yml with your settings
> docker-compose up  # Automatically merges both files
> ```
> Your override file won't be committed to git, so you can safely add credentials and personal preferences.

**Open your browser:** http://localhost:5173

---

## 🎯 Usage

1. **Enter a name:** e.g., "Jordan"
2. **Select relationship:** e.g., "student"
3. **Add qualities:** "creative", "persistent", "thoughtful"
4. **Add context:** "completed a challenging art project"
5. **Choose tone:** warm, enthusiastic, calm, professional
6. **Generate Compliment** and copy or share!

### Test the API

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

**API Documentation:** http://localhost:8000/docs

---

## 🧪 Testing

### End-to-End Tests with Cypress

```bash
# Start the application first
docker-compose up
# Or start frontend and backend separately

# Run tests
cd frontend
npm run test              # Headless
npm run test:open         # Interactive
npm run test:headed       # Headed mode
```

See [Frontend Testing Guide](frontend/README.md#-testing) for details.

---

## 🛠️ Development

Both frontend and backend support hot reload for rapid development.

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

**Backend (Python):**
```bash
cd backend
ruff check .          # Check for issues
ruff check --fix .    # Auto-fix
ruff format .         # Format code
```

**Frontend (JavaScript/Vue):**
```bash
cd frontend
npm run lint          # Check
npm run lint:fix      # Auto-fix
```

See **[LINTING.md](LINTING.md)** for complete linting documentation.

---

## 🐛 Troubleshooting

### Backend Not Connecting
```bash
# Check backend health
curl http://localhost:8000/health

# If using Ollama, verify it's running
curl http://localhost:11434/api/tags

# Pull model if missing
ollama pull llama3.2:1b
```

### Frontend Not Loading
```bash
# Check for port conflicts
lsof -i :5173

# Try different port
npm run dev -- --port 3000

# Verify backend URL in frontend/.env
cat frontend/.env
```

### Port Already in Use
```bash
# Find process
lsof -i :8000

# Kill it (replace PID)
kill -9 <PID>
```

For detailed troubleshooting, see:
- [Backend Troubleshooting](backend/README.md#-troubleshooting)
- [Frontend Troubleshooting](frontend/README.md#-troubleshooting)

---

## 🚀 Deployment

### Quick Deployment Overview

**Backend Options:**
- **Vercel/Railway/Render** (serverless with Google Gemini)
- **Docker on VM** (self-hosted with Ollama)

**Frontend Options:**
- **Vercel/Netlify** (recommended)
- **GitHub Pages** (static hosting)
- **Self-hosted** (Nginx/Apache)

**See the complete [DEPLOYMENT.md](DEPLOYMENT.md) guide** for:
- Platform-specific instructions
- Environment variable setup
- Production configurations
- Security best practices
- Monitoring and troubleshooting

---

## 📖 About Nurtured Heart Approach

The Nurtured Heart Approach focuses on recognizing and celebrating inner greatness, positive qualities, and success in meaningful, specific ways. This approach:

- Emphasizes what's going right rather than what's going wrong
- Recognizes effort and character, not just outcomes
- Uses specific, authentic language
- Celebrates inner qualities and values
- Builds self-worth and positive identity

---

## 📚 Documentation

- **[Deployment Guide](DEPLOYMENT.md)** - Production deployment for all platforms
- **[Backend Documentation](backend/README.md)** - API reference, code structure, development
- **[Frontend Documentation](frontend/README.md)** - Components, architecture, development
- **[Linting Guide](LINTING.md)** - Code quality and style enforcement
- **[API Docs](http://localhost:8000/docs)** - Interactive API documentation (when running)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What does this mean?

✅ **You can:**
- Use commercially
- Modify and distribute
- Use privately
- Sublicense

❗ **You must:**
- Include the original copyright and license

🚫 **This software comes with:**
- NO warranty or liability

---

## 🙋 Need Help?

- **Backend logs:** Terminal where backend is running
- **Frontend errors:** Browser console (F12)
- **API documentation:** http://localhost:8000/docs
- **Configuration:** Check `.env` files in `backend/` and `frontend/`

---

**Happy compliment generating! 💙**
