# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

