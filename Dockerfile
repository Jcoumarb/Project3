#python latest image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the project directory to /app on the container
COPY . /app

# Install poetry
run pip install poetry

# Install project dependencies using poetry
RUN poetry install

# Expose port 8000 for uvicorn
EXPOSE 8000

# Make the entrypoint our uvicorn command to launch the server
CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
