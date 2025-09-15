# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port for Gunicorn
EXPOSE 8000

# Run Gunicorn for Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
