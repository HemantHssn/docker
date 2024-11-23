# Use a base image with Python and Bash
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the scripts into the container
COPY hello.sh /app/hello.sh
COPY hii.py /app/hii.py

# Make the shell script executable
RUN chmod +x /app/hello.sh

# Default command to run both scripts
CMD ["bash", "-c", "./hello.sh && python3 hii.py"]
