# Use official Python image as base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY ./app ./app

# Expose port for FastAPI (default 8000)
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
