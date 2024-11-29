# Use the Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first
COPY app/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY app/ .

# Expose the app port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

