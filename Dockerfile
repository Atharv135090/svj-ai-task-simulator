FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Default command to run
CMD ["python", "inference.py"]
