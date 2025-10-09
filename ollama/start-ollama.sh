#!/bin/bash

# Start Ollama in the background
echo "Starting Ollama server..."
/usr/bin/ollama serve &

# Store the PID of Ollama
OLLAMA_PID=$!

# Run the init script
/ollama-init.sh

# Wait for Ollama to finish
wait $OLLAMA_PID
