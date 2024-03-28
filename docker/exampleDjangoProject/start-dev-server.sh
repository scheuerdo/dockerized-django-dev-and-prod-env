#!/bin/sh
echo "Running datasbase migrations..."
python manage.py migrate
echo "Starting development server (manage.py runserver)..."
python manage.py runserver 0.0.0.0:8000