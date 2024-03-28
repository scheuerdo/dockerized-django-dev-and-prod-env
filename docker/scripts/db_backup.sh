#!/bin/bash

DATE=$(date +"%Y%m%d%H%M%S")

# Hard coded Docker Compose service names
DB_SERVICE_NAME="ms_django_db"
DJANGO_SERVICE_NAME="ms_django"

# Check if the script is being run from the directory containing the .env file with the required database environment variables
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs -d '\n')
else
  echo "Error: .env file db with environment variables not found."
  exit 1
fi

echo "Backing up database $DB_NAME from $DB_SERVICE_NAME service..."

# Create a directory to store the backup files
BACKUP_DIR="./db_backups"
mkdir -p "$BACKUP_DIR"

# Creating the backup file using the PostgreSQL pg_dump command
docker exec "$DB_SERVICE_NAME" pg_dump -U "$DB_USER" -d "$DB_NAME" > "$BACKUP_DIR/db_backup_$DATE.sql"

# Output the backup file path to the terminal
echo "Backup completed and saved to $BACKUP_DIR/db_backup_$DATE.sql"
