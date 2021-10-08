#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python manage.py makemigrations
python manage.py migrate
gunicorn --worker-tmp-dir /dev/shm core.wsgi:application --reload --bind 0.0.0.0:8000

exec "$@"
