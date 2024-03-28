#!/bin/bash

# Wait until the Postgres container is ready by trying to connect to the database with python
function postgres_container_ready(){
python << END
import sys
import psycopg2
try:
    print("Trying to connect to database '$DB_NAME' on host '$DB_HOST'..")
    conn = psycopg2.connect(dbname="$DB_NAME", user="$DB_USER", password="$DB_PASSWORD", host="$DB_HOST")
except psycopg2.OperationalError as e:
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}

# Running a loop to check if the Postgres container is ready
until postgres_container_ready; do
  >&2 echo "Postgres is unavailable, will try again in 1 second..."
  sleep 1
done

>&2 echo "Postgres is up! Starting the Django application..."

exec "$@"