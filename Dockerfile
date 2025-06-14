# Stage 1: Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install production dependencies
# --no-cache-dir: Disables the cache, resulting in a smaller image size
# --trusted-host pypi.python.org: Can help avoid SSL issues in some networks
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
# Use gunicorn for a production-ready server, but for simplicity, we'll use flask's built-in server.
# For production, you would use: CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
CMD ["flask", "run", "--host=0.0.0.0"]