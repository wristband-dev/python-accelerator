FROM python:3.11-slim

WORKDIR /app

# Copy requirements and application code
COPY backend/pyproject.toml backend/run.py /app/
COPY backend/src/ /app/src/
COPY config.yml /app/config.yml

# Install pip and dependencies
RUN pip install .

# Expose port
EXPOSE 6001

# Run the application
CMD ["python", "run.py"] 