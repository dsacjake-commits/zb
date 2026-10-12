FROM python:3.10-slim

# Instalamos FFmpeg y fuentes TrueType esenciales para el letrero de texto
RUN apt-get update && apt-get install -y ffmpeg fonts-liberation && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

CMD ["python", "main.py"]
