#!/bin/bash

echo "Waiting for database to be ready..."

while ! pg_isready -h db -p 5432 -U postgres; do
    echo "Database not ready yet, waiting..."
    sleep 2
done

echo "Database is ready!"
echo "Running migrations..."
alembic upgrade head
echo "Starting server..."
uvicorn main:app --host 0.0.0.0 --port 8000