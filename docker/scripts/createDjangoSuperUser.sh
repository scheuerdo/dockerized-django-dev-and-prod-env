#!/bin/bash

# Get the directory of the script and using that the path of the docker-compose.dev.yaml file
script_dir="$(dirname "$(readlink -f "$0")")"
docker_compose_dev_file_path="$script_dir/../docker-compose.dev.yaml"

# Create Django Admin User/Super User inside the Django container ms_django (service name in docker-compose.dev.yaml file)
echo "Creating Django Super User..."
docker compose -f $docker_compose_dev_file_path run ms_django python manage.py createsuperuser