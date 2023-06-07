
# Denne filen er definisjonen på hvordan docker imaget blir bygd


# Use an official Python runtime as the base image
#DOCKER MENER JEG SKAL BRUKE DENNE
FROM python:3.9-slim
# FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY flask_server .

# Expose the port that your Flask application listens on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=server.py

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]