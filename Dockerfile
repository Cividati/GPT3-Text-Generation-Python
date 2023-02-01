# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the required dependencies
RUN pip install openai

# Set the environment variable for the OpenAI API key
ENV API_KEY "your_api_key"

# Run the script
CMD ["python", "gpt3_text_generation.py"]
