#!/bin/bash

echo "🚀 Setting up Nurtured Heart Compliment Generator..."

# Create .env files from examples
echo "📝 Creating environment files..."

# Check if .env files already exist
if [ -f "backend/.env" ]; then
  echo "⚠️  backend/.env already exists, skipping..."
else
  cp backend/.env.example backend/.env
  echo "✅ Created backend/.env from .env.example"
fi

if [ -f "frontend/.env" ]; then
  echo "⚠️  frontend/.env already exists, skipping..."
else
  cp frontend/.env.example frontend/.env
  echo "✅ Created frontend/.env from .env.example"
fi

echo "✅ Environment files ready!"
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

