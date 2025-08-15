# Using Python 3.13 base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Installing required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copies all application files to the working directory
COPY . .

# Tells Docker which port to use
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]