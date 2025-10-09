#!/bin/bash

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until curl -f http://localhost:11434/api/tags > /dev/null 2>&1; do
    echo "Ollama not ready yet, waiting..."
    sleep 2
done

echo "Ollama is ready! Checking for llama3.2 model..."

# Check if llama3.2 is already installed
if ollama list | grep -q "llama3.2"; then
    echo "llama3.2 model is already installed"
else
    echo "Installing llama3.2 model..."
    ollama pull llama3.2
    echo "llama3.2 model installed successfully!"
fi

echo "Ollama setup complete!"
