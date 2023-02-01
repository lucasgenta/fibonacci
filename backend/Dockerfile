FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script to the working directory
COPY fibonacci.py .

# Expose the port
EXPOSE 5000

# Run the command
CMD ["python", "fibonacci.py"]

