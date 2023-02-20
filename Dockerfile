# syntax=docker/dockerfile:1

# Python base image to be able to run our project
FROM python:3.11

# Copy of all project code inside docker to be able to run it in Docker containers
COPY . /opt/pdf2xlsx

# Establishment of the working directory
WORKDIR /opt/pdf2xlsx

# Installation of project requirements
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean;
RUN pip install -r requirements.txt

# Execution of the main project file
CMD ["python", "main.py"]
