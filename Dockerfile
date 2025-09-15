# Use the official Python image for best compatibility and security
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port that Gunicorn will serve on
EXPOSE 8000

# Default command: Gunicorn as WSGI server
# If your Flask app entry point is app.py and 'app' is the Flask instance, adjust as follows:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "apps:app"]
