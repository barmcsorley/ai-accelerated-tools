# Use a slim Python image to keep size down
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system build tools (required for ChromaDB's core libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code (ingest.py) into the container
COPY src/ .

# Command to run the ingestion script
CMD ["python", "ingest.py"]