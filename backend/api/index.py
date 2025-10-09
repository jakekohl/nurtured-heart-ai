"""
Vercel serverless function entry point.
This file imports the FastAPI app from main.py for Vercel deployment.
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import main
sys.path.append(str(Path(__file__).parent.parent))

from main import app

# Vercel will use this app instance
# The app is already configured in main.py with all routes and middleware

