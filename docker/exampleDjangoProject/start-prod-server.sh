#!/bin/sh
echo "Running database migrations..."
python manage.py migrate
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Starting production application server (Gunicorn)..."
gunicorn exampleDjangoProject.wsgi --bind 0.0.0.0:8000 -w 2 --timeout 60 --access-logfile - --error-logfile -