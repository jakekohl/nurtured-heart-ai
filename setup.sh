#!/bin/bash

echo "🚀 Setting up Nurtured Heart Compliment Generator..."

# Create .env files
echo "📝 Creating environment files..."

# Backend .env
cat > backend/.env << 'EOF'
# Backend Configuration
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# LLM Configuration
OLLAMA_HOST=http://localhost:11434
DEFAULT_MODEL=llama3.2:latest
TEMPERATURE=0.7

# Email Configuration (optional - for sending compliments)
# Uncomment and configure if you want to enable email sending
#SMTP_HOST=smtp.gmail.com
#SMTP_PORT=587
#SMTP_USER=your-email@gmail.com
#SMTP_PASSWORD=your-app-password
#FROM_EMAIL=your-email@gmail.com
EOF

# Frontend .env
cat > frontend/.env << 'EOF'
VITE_API_URL=http://localhost:8000
EOF

echo "✅ Environment files created!"
echo ""
echo "📦 Installing dependencies..."

# Backend setup
echo "Setting up backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Frontend setup
echo "Setting up frontend..."
cd frontend
npm install
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Next steps:"
echo "1. Install Ollama: https://ollama.ai/download"
echo "2. Pull a model: ollama pull llama3.2"
echo "3. Start Ollama: ollama serve"
echo "4. Start backend: cd backend && source venv/bin/activate && python main.py"
echo "5. Start frontend: cd frontend && npm run dev"
echo "6. Open browser: http://localhost:5173"
echo ""
echo "Happy coding! 💙"

