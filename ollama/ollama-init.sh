#!/bin/bash

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until curl -f http://localhost:11434/api/tags > /dev/null 2>&1; do
    echo "Ollama not ready yet, waiting..."
    sleep 2
done

echo "Ollama is ready! Checking for llama3.2:1b model..."

# Check if llama3.2:1b is already installed
if ollama list | grep -q "llama3.2:1b"; then
    echo "llama3.2:1b model is already installed"
else
    echo "Installing llama3.2:1b model..."
    ollama pull llama3.2:1b
    echo "llama3.2:1b model installed successfully!"
fi

echo "Ollama setup complete!"
