# Use official slim Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements from the project subfolder
COPY requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# start gunicon server
CMD python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput && \
    gunicorn emis.wsgi:application --bind 0.0.0.0:8000