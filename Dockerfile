# Use official base image for Python web apps, e.g., Flask
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements (if present) and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . .

# Expose the port (update to your web server's port, e.g., 5000 for Flask)
EXPOSE 5000

# Start the application (adjust as per your entry point)
CMD ["python", "app.py"]
