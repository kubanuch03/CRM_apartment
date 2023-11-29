# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY req.txt /app/

# Install dependencies
RUN pip install gunicorn
RUN pip install --no-cache-dir -r req.txt
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
# Copy the project code
COPY . /app/
