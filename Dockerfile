FROM python:3.11-slim

# Install FFmpeg + system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Ollama (for local AI)
RUN curl -fsSL https://ollama.com/install.sh | sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-pull default model (optional, remove if you want to pull manually)
# RUN ollama serve & sleep 5 && ollama pull llama3.3:latest

EXPOSE 11434

CMD ["python", "main.py"]
