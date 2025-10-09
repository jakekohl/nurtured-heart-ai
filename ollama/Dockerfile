FROM ollama/ollama:latest

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy the init script
COPY ollama-init.sh /ollama-init.sh
RUN chmod +x /ollama-init.sh

# Create a startup script that runs both Ollama and the init script
COPY start-ollama.sh /start-ollama.sh
RUN chmod +x /start-ollama.sh

# Override the entrypoint
ENTRYPOINT []
CMD ["/start-ollama.sh"]
